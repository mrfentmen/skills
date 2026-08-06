#!/usr/bin/env python3
"""Conservative, non-destructive smoke check for skill examples.

This is intentionally not a runtime-quality oracle. It syntax-checks Python and
JavaScript examples when the relevant interpreter is available, inventories all
other fenced blocks, and records skips explicitly rather than pretending they
were executed.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SKILLS = [
    "choka", "dodoitsu", "gogyohka", "haibun", "haiku",
    "katauta", "lunes", "monoku", "renga",
    "sedoka", "senryu", "sijo", "tanka",
    "kyoka", "somonka", "bussokusekika", "imayo",
    "kanshi", "zappai", "waka", "renshi", "sonnet",
]
BLOCK_RE = re.compile(r"^```([A-Za-z0-9+#-]*)\s*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)
SUPPORTED = {"python", "py", "javascript", "js"}
INTERACTIVE_MARKERS = (
    "input(", "serve_forever", "turtle.", "tkinter", "readline(",
    "process.stdin", "prompt(", "httpserver", "http.server",
)


def check_python(source: str, filename: str) -> tuple[str, str]:
    try:
        compile(source, filename, "exec")
    except SyntaxError as exc:
        return "fail", f"line {exc.lineno}: {exc.msg}"
    return "pass", "syntax compiled"


def check_javascript(source: str) -> tuple[str, str]:
    node = shutil.which("node")
    if not node:
        return "skip", "node is not installed"
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".mjs", encoding="utf-8") as handle:
            handle.write(source)
            handle.flush()
            result = subprocess.run(
                [node, "--check", handle.name],
                text=True,
                capture_output=True,
                timeout=10,
            )
    except subprocess.TimeoutExpired:
        return "fail", "node --check timed out after 10 seconds"
    except OSError as exc:
        return "fail", f"could not invoke node: {exc}"
    if result.returncode:
        detail = (result.stderr or result.stdout).strip().splitlines()
        return "fail", detail[-1] if detail else "node --check failed"
    return "pass", "node --check passed"


def inspect_skill(root: Path, skill: str) -> tuple[list[dict], list[str]]:
    path = root / skill / "SKILL.md"
    if not path.is_file():
        return [], [f"{skill}: missing SKILL.md"]
    results: list[dict] = []
    errors: list[str] = []
    blocks = BLOCK_RE.findall(path.read_text(encoding="utf-8", errors="replace"))
    supported_seen = False
    for number, (language, source) in enumerate(blocks, 1):
        normalized = language.lower() or "text"
        item = {"skill": skill, "block": number, "language": normalized}
        if normalized not in SUPPORTED:
            item.update(status="skip", detail="language is inventoried but not syntax-checked")
        elif any(marker in source.lower() for marker in INTERACTIVE_MARKERS):
            item.update(status="skip", detail="interactive or server example is not executed")
            supported_seen = True
        elif normalized in {"python", "py"}:
            item["status"], item["detail"] = check_python(source, f"{skill}/SKILL.md:block-{number}")
            supported_seen = True
        else:
            item["status"], item["detail"] = check_javascript(source)
            supported_seen = True
        if item["status"] == "fail":
            errors.append(f"{skill} block {number} ({normalized}): {item['detail']}")
        results.append(item)
    if not blocks:
        errors.append(f"{skill}: no fenced examples found")
    if not supported_seen:
        errors.append(f"{skill}: no Python/JavaScript example available for smoke checking")
    return results, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", type=Path, help="write the non-authoritative result outside the repo or to an explicit path")
    args = parser.parse_args()
    root = args.root.resolve()
    all_results: list[dict] = []
    errors: list[str] = []
    for skill in SKILLS:
        results, skill_errors = inspect_skill(root, skill)
        all_results.extend(results)
        errors.extend(skill_errors)
        counts = {status: sum(item["status"] == status for item in results) for status in ("pass", "skip", "fail")}
        print(f"{skill}: {counts['pass']} pass, {counts['skip']} skip, {counts['fail']} fail")
    summary = {
        "skills": len(SKILLS),
        "blocks": len(all_results),
        "pass": sum(item["status"] == "pass" for item in all_results),
        "skip": sum(item["status"] == "skip" for item in all_results),
        "fail": sum(item["status"] == "fail" for item in all_results),
        "errors": errors,
        "results": all_results,
        "scope": "syntax-only for Python/JavaScript; unsupported and interactive blocks are explicit skips",
    }
    if args.json:
        args.json.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    if errors:
        print("FAIL: example smoke check")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(SKILLS)} skills; {summary['pass']} syntax checks; {summary['skip']} explicit skips; 0 failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
