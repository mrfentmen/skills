#!/usr/bin/env python3
"""
Generate the README.md for a per-skill GitHub repo: not just the
description, but a demo: a realistic usage prompt plus a taste of the
code style straight from the skill's own SKILL.md.

Usage:
  python3 ci/generate_repo_readme.py <skill-dir> [out-file]

Reads:
  - <skill-dir>/SKILL.md            frontmatter description + first
                                    "Core Patterns" code block (style sample)
  - evals-infra/legacy/trigger_eval_queries.json   first should_trigger
                                    query for the skill = the usage prompt

If out-file is omitted, prints the README to stdout.
"""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# The benchmark harness is kept outside the skill tree so generated skill
# repos do not carry workspaces or evaluator history.
HARNESS = Path(os.environ.get(
    "EVALS_INFRA_ROOT", str(ROOT / "evals-infra")))
QUERIES = HARNESS / "legacy" / "trigger_eval_queries.json"

# GitHub owner for the per-repo Actions badge. Defaults to the account that
# owns the skill repos (mrfentmen); overridable via the GITHUB_REPOSITORY_OWNER
# env var (GitHub Actions sets it automatically), so the generator stays
# portable if the repos ever move accounts.
OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "mrfentmen")

# Workflow file name inside every per-skill repo (see push_all_skills.sh).
WORKFLOW_FILE = "audit-and-package.yml"

MAX_SAMPLE_LINES = 20


def frontmatter_desc(text: str) -> str:
    # NOTE: keep the description-parsing logic in sync with
    # evals-infra/static_skill_audit.py (both stay standalone because they
    # are snapshotted into per-repo .github/scripts/).
    m = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return ""
    parts, in_desc = [], False
    for line in m.group(1).split("\n"):
        stripped = line.strip()
        if stripped.startswith("description:"):
            in_desc = True
            continue
        if in_desc:
            if line.startswith("  ") or stripped == "":
                parts.append(stripped)
            else:
                break
    return " ".join(p for p in parts if p).strip()


def style_sample(text: str) -> tuple[str, str]:
    """First fenced code block after a 'Core Patterns' heading (fallback:
    first fenced block anywhere). Returns (lang, code)."""
    core = re.search(r"^#+.*core patterns", text, re.MULTILINE | re.IGNORECASE)
    cutoff = core.start() if core else 0
    blocks = list(re.finditer(r"^```(\w*)\s*\n(.*?)^```",
                              text, re.MULTILINE | re.DOTALL))
    if not blocks:
        return "", ""
    # prefer real code blocks; "text"/un-tagged blocks are often anti-examples
    CODE_LANGS = {"python", "py", "javascript", "js", "typescript", "ts",
                  "rust", "rs", "c", "cpp", "go", "bash", "sh", "ruby"}
    code_blocks = [b for b in blocks if b.group(1).lower() in CODE_LANGS]
    pool = code_blocks or blocks
    chosen = next((b for b in pool if b.start() >= cutoff), pool[0])
    lang, code = chosen.group(1), chosen.group(2).rstrip()
    code_lines = code.split("\n")
    if len(code_lines) > MAX_SAMPLE_LINES:
        # language-agnostic truncation marker (not a comment char, which
        # would be invalid syntax in half the languages)
        code = "\n".join(code_lines[:MAX_SAMPLE_LINES]) + "\n…"
    return lang or "text", code


def usage_prompt(skill: str) -> str:
    try:
        data = json.loads(QUERIES.read_text())
        for q in data["skills"][skill]["eval_queries"]:
            if q["should_trigger"]:
                return q["query"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
        print(f"warning: usage prompt fallback for {skill} ({e})",
              file=sys.stderr)
    return f"Write a {skill.replace('-', ' ')} program"


def build(skill_dir: Path) -> str:
    name = skill_dir.name
    skill_md = (skill_dir / "SKILL.md")
    text = skill_md.read_text(errors="ignore") if skill_md.exists() else ""
    desc = frontmatter_desc(text)
    lang, code = style_sample(text)
    prompt = usage_prompt(name)

    # Audit & Package status badge: native GitHub workflow badge (renders for
    # the signed-in owner on private repos; the image is fetched with the
    # viewer's session cookie) linking to the repo's Actions tab.
    badge = (f"[![Audit & Package](https://github.com/{OWNER}/{name}/actions/workflows/"
             f"{WORKFLOW_FILE}/badge.svg)]"
             f"(https://github.com/{OWNER}/{name}/actions)")

    out = [f"# {name}", ""]
    out.append(badge)
    out.append("")
    out.append(f"A coding skill: {desc}")
    out.append("")
    out.append("## Usage")
    out.append("")
    out.append("Ask your AI to write code in this style. For example:")
    out.append("")
    out.append(f"> {prompt}")
    out.append("")
    if code:
        out.append("A taste of what it produces (from the skill's own examples):")
        out.append("")
        out.append(f"```{lang}")
        out.append(code)
        out.append("```")
    else:
        out.append("(see `SKILL.md` for full examples and minimum requirements)")
        out.append("")
    out.append("")
    out.append("## What's inside")
    out.append("")
    out.append("- `SKILL.md`: the skill definition (philosophy, patterns,"
               " boundaries, checkable requirements)")
    out.append("- `evals/`: eval cases")
    out.append(f"- `{name}.skill`: packaged single-file skill")
    out.append("- `shared/`: helper modules (ASCII canvas, box drawing, RNG)")
    out.append("- `.github/workflows/audit-and-package.yml`: CI: static audit"
               " + repackage on every push (bad quality fails the run;"
               " refreshed artifacts are committed back). Status is shown by"
               " the badge at the top of this README.")
    out.append("")
    out.append("## Install")
    out.append("")
    out.append("Place this folder in your skills directory, or load the "
               f"packaged `{name}.skill`:")
    out.append("")
    out.append("- **Codex**: `.codex/skills/`")
    out.append("- **Freebuff**: `.agents/skills/`")
    out.append("")
    return "\n".join(out) + "\n"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: python3 ci/generate_repo_readme.py <skill-dir> [out-file]")
    skill_dir = Path(sys.argv[1])
    readme = build(skill_dir)
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(readme)
        print(f"wrote {Path(sys.argv[2])} ({len(readme)} bytes)")
    else:
        print(readme, end="")


if __name__ == "__main__":
    main()
