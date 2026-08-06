#!/usr/bin/env python3
"""Validate the versioned standalone trigger benchmark.

This validator deliberately does not read or mutate the historical evaluation
artifacts.  It checks the current standalone contract only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKILLS = [
    "choka", "dodoitsu", "gogyohka", "haibun", "haiku",
    "katauta", "lunes", "monoku", "renga",
    "sedoka", "senryu", "sijo", "tanka",
]
EXPECTED_TYPES = {"explicit_or_signature", "boundary", "none", "trap"}
EXPECTED_FIELDS = {"id", "prompt", "target", "type"}
ALIASES = {}
for _skill in SKILLS:
    ALIASES.setdefault(_skill, (_skill,))


def token_pattern(token: str) -> re.Pattern[str]:
    return re.compile(r"(?<![a-z0-9])" + re.escape(token.lower()) + r"(?![a-z0-9])")


TOKEN_PATTERNS = {
    skill: tuple(token_pattern(alias) for alias in aliases)
    for skill, aliases in ALIASES.items()
}


def mentions(text: str, skill: str) -> bool:
    lowered = text.lower()
    return any(pattern.search(lowered) for pattern in TOKEN_PATTERNS[skill])


def mentioned_skills(text: str) -> list[str]:
    return [skill for skill in SKILLS if mentions(text, skill)]


def load(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("top level must be an object")
    return value


def validate(data: dict, root: Path) -> list[str]:
    errors: list[str] = []
    if data.get("version") != "standalone-trigger-v1":
        errors.append("version must be standalone-trigger-v1")
    if data.get("skills") != SKILLS:
        errors.append("skills must exactly match the current 13-skill order")
    records = data.get("records")
    if not isinstance(records, list):
        return errors + ["records must be a list"]
    expected_total = len(SKILLS) * 7 + 36 + 18  # per-skill 5+2, plus global none/trap
    if len(records) != expected_total:
        errors.append(f"expected {expected_total} records, found {len(records)}")
    expected_ids = [f"standalone-v1-{index:03d}" for index in range(1, expected_total + 1)]
    actual_ids = [record.get("id") if isinstance(record, dict) else None for record in records]
    if actual_ids != expected_ids:
        errors.append(f"record IDs must be standalone-v1-001 through standalone-v1-{expected_total:03d} in order")

    type_counts = {kind: 0 for kind in EXPECTED_TYPES}
    per_skill: dict[str, dict[str, int]] = {
        skill: {"explicit": 0, "signature": 0, "boundary": 0}
        for skill in SKILLS
    }
    none_counts = {"none": 0, "trap": 0}
    prompts: set[str] = set()
    for index, record in enumerate(records, 1):
        label = f"record {index}"
        if not isinstance(record, dict):
            errors.append(f"{label}: must be an object")
            continue
        if set(record) != EXPECTED_FIELDS:
            errors.append(f"{label}: fields must be exactly {sorted(EXPECTED_FIELDS)}")
            continue
        prompt = record["prompt"]
        target = record["target"]
        kind = record["type"]
        if not isinstance(kind, str):
            errors.append(f"{label}: type must be a string")
            continue
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{label}: prompt must be a non-empty string")
            continue
        normalized = prompt.strip()
        if normalized in prompts:
            errors.append(f"{label}: duplicate prompt")
        prompts.add(normalized)
        if any(ord(char) < 32 and char not in "\t\n\r" for char in prompt):
            errors.append(f"{label}: prompt contains a control character")
        if kind not in EXPECTED_TYPES:
            errors.append(f"{label}: invalid type {kind!r}")
            continue
        type_counts[kind] += 1
        if not isinstance(target, str):
            errors.append(f"{label}: target must be a string")
            continue
        if target != "none" and target not in SKILLS:
            errors.append(f"{label}: invalid target {target!r}")
        if kind in {"explicit_or_signature", "boundary"} and target not in SKILLS:
            continue
        if kind in {"none", "trap"} and target != "none":
            errors.append(f"{label}: {kind} target must be none")
        found = mentioned_skills(prompt)
        if kind == "explicit_or_signature":
            if target not in SKILLS:
                continue
            if mentions(prompt, target):
                per_skill[target]["explicit"] += 1
                if any(skill != target for skill in found):
                    errors.append(f"{label}: explicit prompt names another skill: {found}")
            else:
                per_skill[target]["signature"] += 1
                if found:
                    errors.append(f"{label}: signature prompt names skill(s): {found}")
        elif kind == "boundary":
            if target in SKILLS:
                per_skill[target]["boundary"] += 1
            if found:
                errors.append(f"{label}: boundary prompt must contain no skill-name tokens: {found}")
        elif kind in {"none", "trap"}:
            if found:
                errors.append(f"{label}: {kind} prompt must contain no skill-name tokens: {found}")
            none_counts[kind] += 1
        if re.search(r"(?i)benchmark|evaluator|trigger\s+set|ground\s+truth|test\s+case", prompt):
            errors.append(f"{label}: prompt leaks evaluation terminology")

    expected_types = {"explicit_or_signature": len(SKILLS) * 5, "boundary": len(SKILLS) * 2,
                      "none": 36, "trap": 18}
    if type_counts != expected_types:
        errors.append(f"type counts are {type_counts}, expected {expected_types}")
    if none_counts != {"none": 36, "trap": 18}:
        errors.append(f"none/trap counts are {none_counts}, expected 36/18")
    for skill in SKILLS:
        counts = per_skill[skill]
        if counts["explicit"] != 3 or counts["signature"] != 2:
            errors.append(f"{skill}: expected 3 explicit and 2 signature prompts, got {counts}")
        if counts["boundary"] != 2:
            errors.append(f"{skill}: expected 2 boundary prompts, got {counts['boundary']}")

    for skill in SKILLS:
        skill_file = root / skill / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing local skill file: {skill_file}")
            continue
        text = skill_file.read_text(encoding="utf-8", errors="replace")
        if not re.search(r"^---\s*\n.*?\n---", text, re.DOTALL):
            errors.append(f"{skill}: SKILL.md has no frontmatter")
        if not re.search(r"(?m)^description:\s*", text):
            errors.append(f"{skill}: SKILL.md has no frontmatter description")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--benchmark", type=Path, default=Path(__file__).resolve().with_name("standalone_trigger_benchmark_v1.json"))
    args = parser.parse_args()
    try:
        data = load(args.benchmark.resolve())
        errors = validate(data, args.root.resolve())
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("FAIL: standalone benchmark validation")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: standalone-trigger-v1; 180 records; 18 skills; 90 explicit/signature, 36 boundary, 36 none, 18 trap")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
