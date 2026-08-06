#!/usr/bin/env python3
"""Generate a blind scoring sheet for the current-scope held-out set.

The sheet contains the 18 skill descriptions and the 54 prompts in a
deterministic shuffled order, with NO gold labels. Give this to an independent
scorer (a human or a model) and collect their decisions as a JSON object
mapping prompt IDs to skill names or "none".
"""
from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

SKILLS = [
    "choka", "dodoitsu", "god", "gogyohka", "haibun", "haiku", "katauta",
    "lunes", "monoku", "no-bullshit", "psych", "renga", "sedoka", "senryu",
    "sijo", "smoker", "tanka", "terry-davis",
]


def frontmatter_description(text: str) -> str:
    match = re.search(r"^---\s*\n(.*?)\n---", text, re.MULTILINE | re.DOTALL)
    if not match:
        raise ValueError("SKILL.md has no frontmatter")
    body = match.group(1)
    lines = body.splitlines()
    desc_lines: list[str] = []
    in_desc = False
    for line in lines:
        if line.startswith("description:"):
            in_desc = True
        elif in_desc and line.startswith("  "):
            desc_lines.append(line.strip())
        elif in_desc and line.strip() and not line.startswith("  "):
            in_desc = False
    if desc_lines:
        return " ".join(desc_lines)
    scalar = re.search(r"(?m)^description:\s*(.+)$", body)
    if scalar:
        return scalar.group(1).strip()
    raise ValueError("SKILL.md has no description")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dataset", type=Path, default=Path(__file__).with_name("current_scope_heldout_v1.json"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20260806)
    args = parser.parse_args()
    root = args.root.resolve()
    data = json.loads(args.dataset.resolve().read_text(encoding="utf-8"))
    records = data["records"]
    if len(records) != 54:
        raise SystemExit("expected 54 held-out records")
    descriptions = []
    for skill in SKILLS:
        text = (root / skill / "SKILL.md").read_text(encoding="utf-8")
        descriptions.append((skill, frontmatter_description(text)))
    shuffled = list(records)
    random.Random(args.seed).shuffle(shuffled)
    lines = [
        "# Current-Scope Held-Out Routing Sheet (blind)",
        "",
        f"Below are all {len(SKILLS)} skill descriptions. Then {len(records)}",
        "prompts, numbered, in a scrambled order. For each prompt, pick the ONE",
        "skill whose description best fits the request - or `none` if no skill",
        "fits at all. This is routing: the winning skill must fire on that",
        "prompt and no other skill should.",
        "",
        "## Available skills",
        "",
    ]
    for name, description in descriptions:
        lines.append(f"**{name}:** {description}")
        lines.append("")
    lines.append("## Prompts")
    lines.append("")
    for index, record in enumerate(shuffled, 1):
        lines.append(f"{index}. ({record['id']}) {record['prompt']}")
    lines.append("")
    lines.append("## How to submit decisions")
    lines.append("")
    lines.append("Return a JSON object mapping every prompt ID to a skill name or")
    lines.append("'none', e.g.: {\"heldout-v1-001\": \"haiku\", \"heldout-v1-046\": \"none\", ...}")
    args.output.resolve().parent.mkdir(parents=True, exist_ok=True)
    args.output.resolve().write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote blind sheet: {args.output} ({len(records)} prompts, no gold labels)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
