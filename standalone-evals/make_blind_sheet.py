#!/usr/bin/env python3
"""Generate a blind routing sheet from the current standalone benchmark.

The output intentionally omits every record's target and type. Give only this
sheet to an independent scorer; keep the source benchmark private until scoring
is complete.
"""
from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

SKILL_NAMES = [
    "choka", "dodoitsu", "god", "gogyohka", "haibun", "haiku",
    "katauta", "lunes", "monoku", "no-bullshit", "psych", "renga",
    "sedoka", "senryu", "sijo", "smoker", "tanka", "terry-davis",
]


def frontmatter_description(text: str) -> str:
    match = re.search(r"^---\s*\n(.*?)\n---", text, re.MULTILINE | re.DOTALL)
    if not match:
        raise ValueError("SKILL.md has no frontmatter")
    body = match.group(1)
    block = re.search(r"(?m)^description:\s*[>|]?-?\s*\n((?:  .*\n?)*)", body)
    if block:
        return " ".join(line.strip() for line in block.group(1).splitlines() if line.strip())
    scalar = re.search(r"(?m)^description:\s*(.+)$", body)
    if scalar:
        return scalar.group(1).strip()
    raise ValueError("SKILL.md has no description")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--benchmark", type=Path, default=Path(__file__).resolve().with_name("standalone_trigger_benchmark_v1.json"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20260806)
    args = parser.parse_args()
    root = args.root.resolve()
    data = json.loads(args.benchmark.resolve().read_text(encoding="utf-8"))
    if data.get("skills") != SKILL_NAMES or len(data.get("records", [])) != 180:
        raise SystemExit("benchmark is not the expected standalone-trigger-v1 dataset")
    descriptions = []
    for skill in SKILL_NAMES:
        path = root / skill / "SKILL.md"
        descriptions.append({"name": skill, "description": frontmatter_description(path.read_text(encoding="utf-8"))})
    records = [{"id": record["id"], "prompt": record["prompt"]} for record in data["records"]]
    random.Random(args.seed).shuffle(records)
    output = {
        "version": "standalone-trigger-v1-blind",
        "seed": args.seed,
        "skills": descriptions,
        "records": records,
        "gold": "omitted; score with score_blind_decisions.py after independent decisions are complete",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote blind sheet: {args.output} ({len(records)} prompts; gold omitted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
