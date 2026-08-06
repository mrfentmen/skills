#!/usr/bin/env python3
"""Validate the current-scope held-out routing dataset.

This dataset is an experiment artifact, not the 180-record release benchmark.
The validator checks scope, counts, uniqueness, and skill-name leakage so a
held-out score cannot be inflated by malformed prompts.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

SKILLS = [
    "choka", "dodoitsu", "god", "gogyohka", "haibun", "haiku", "katauta",
    "lunes", "monoku", "no-bullshit", "psych", "renga", "sedoka", "senryu",
    "sijo", "smoker", "tanka", "terry-davis",
]
SKILL_ALIASES = {
    "terry-davis": ("terry-davis", "terry davis"),
    "no-bullshit": ("no-bullshit", "no bullshit"),
}
TYPES = {"paraphrase", "boundary", "trap", "none"}
EXPECTED_TYPES = {"paraphrase": 18, "boundary": 18, "trap": 9, "none": 9}


def mentioned(prompt: str) -> list[str]:
    found = []
    for skill in SKILLS:
        aliases = SKILL_ALIASES.get(skill, (skill,))
        if any(re.search(r"(?<![a-z0-9])" + re.escape(alias) + r"(?![a-z0-9])", prompt, re.I) for alias in aliases):
            found.append(skill)
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=Path, default=Path(__file__).with_name("current_scope_heldout_v1.json"))
    args = parser.parse_args()
    try:
        data = json.loads(args.dataset.resolve().read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read dataset: {exc}")
        return 1

    errors: list[str] = []
    if data.get("version") != "current-scope-heldout-v1":
        errors.append("wrong dataset version")
    if data.get("scope") != "18 current standalone skills":
        errors.append("wrong dataset scope")
    records = data.get("records")
    benchmark_path = args.dataset.resolve().with_name("standalone_trigger_benchmark_v1.json")
    benchmark_prompts: set[str] = set()
    if not benchmark_path.exists():
        errors.append(f"release benchmark is missing: {benchmark_path}")
    else:
        try:
            benchmark = json.loads(benchmark_path.read_text(encoding="utf-8"))
            benchmark_prompts = {record["prompt"] for record in benchmark.get("records", [])}
        except (OSError, UnicodeDecodeError, json.JSONDecodeError, TypeError, KeyError) as exc:
            errors.append(f"cannot inspect release benchmark for overlap: {exc}")
    if not isinstance(records, list):
        errors.append("records must be a list")
        records = []
    if len(records) != 54:
        errors.append(f"expected 54 records, found {len(records)}")

    ids: set[str] = set()
    prompts: set[str] = set()
    type_counts: Counter[str] = Counter()
    target_counts: Counter[str] = Counter()
    per_skill_intent: Counter[str] = Counter()
    for index, record in enumerate(records, 1):
        label = f"record {index}"
        if set(record) != {"id", "prompt", "target", "type"}:
            errors.append(f"{label}: fields must be id/prompt/target/type")
            continue
        record_id, prompt, target, kind = (record[key] for key in ("id", "prompt", "target", "type"))
        if not isinstance(record_id, str) or not record_id:
            errors.append(f"{label}: invalid id")
        elif record_id in ids:
            errors.append(f"{label}: duplicate id {record_id}")
        else:
            ids.add(record_id)
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{label}: empty prompt")
        elif prompt in prompts:
            errors.append(f"{label}: duplicate prompt")
        else:
            prompts.add(prompt)
        if prompt in benchmark_prompts:
            errors.append(f"{label}: prompt overlaps the 180-record release benchmark")
        if target != "none" and target not in SKILLS:
            errors.append(f"{label}: invalid target {target!r}")
        if kind not in TYPES:
            errors.append(f"{label}: invalid type {kind!r}")
        else:
            type_counts[kind] += 1
        target_counts[target] += 1
        if kind in {"paraphrase", "boundary"} and target != "none":
            per_skill_intent[target] += 1
        found = mentioned(prompt)
        if found:
            errors.append(f"{label}: prompt leaks skill name(s): {found}")

    if dict(type_counts) != EXPECTED_TYPES:
        errors.append(f"type counts are {dict(type_counts)}, expected {EXPECTED_TYPES}")
    if any(per_skill_intent[skill] != 2 for skill in SKILLS):
        errors.append(f"each skill needs exactly two intent prompts: {dict(per_skill_intent)}")
    if target_counts["none"] != 9:
        errors.append(f"expected 9 none prompts, found {target_counts['none']}")

    if errors:
        print(f"FAIL: current held-out dataset has {len(errors)} issue(s)")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("PASS: current-scope-heldout-v1; 54 records; 18 skills; 18 paraphrase, 18 boundary, 9 trap, 9 none; no skill-name leakage")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
