#!/usr/bin/env python3
"""Score decisions produced from a blind standalone routing sheet.

Decision JSON must be an object mapping every benchmark record ID to either a
skill name or ``none``. The scorer joins those IDs to the private benchmark only
after routing decisions have been produced. Explicit-name records are reported
separately because they are activation-contract checks, not semantic discovery.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

SKILLS = {
    "bussokusekika", "choka", "cinquain", "dodoitsu", "etheree",
    "fibonacci", "gogyohka", "haibun", "haiku", "imayo", "kanshi",
    "katauta", "kyoka", "limerick", "lunes", "monoku", "renga",
    "renshi", "ryuka", "sedoka", "senryu", "sijo", "somonka",
    "sonnet", "tanka", "villanelle", "waka", "zappai", "none",
}
EXPECTED_TYPES = {"explicit_or_signature", "boundary", "none", "trap"}
EXPECTED_FIELDS = {"id", "prompt", "target", "type"}
EXPECTED_SKILLS = [
    "choka", "dodoitsu", "gogyohka", "haibun", "haiku", "katauta",
    "lunes", "monoku", "renga", "sedoka", "senryu", "sijo", "tanka",
    "kyoka", "somonka", "bussokusekika", "imayo", "kanshi", "zappai",
    "waka", "renshi", "sonnet", "villanelle", "cinquain", "ryuka",
    "fibonacci", "limerick", "etheree",
]
EXPECTED_TYPE_COUNTS = {"explicit_or_signature": 140, "boundary": 56, "none": 36, "trap": 18}


def read_json(path: Path, label: str) -> Any:
    try:
        return json.loads(path.resolve().read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {label}: {exc}") from exc


def validate_benchmark(value: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, dict):
        return ["benchmark must be a JSON object"]
    if value.get("version") != "standalone-trigger-v1":
        errors.append("benchmark version must be standalone-trigger-v1")
    if value.get("skills") != EXPECTED_SKILLS:
        errors.append("benchmark skills do not match the expected 18-skill order")
    records = value.get("records")
    if not isinstance(records, list) or not records:
        return errors + ["benchmark records must be a non-empty list"]
    if len(records) != 250:
        errors.append(f"benchmark must contain exactly 250 records, found {len(records)}")
    expected_ids = {f"standalone-v1-{index:03d}" for index in range(1, 251)}
    ids: set[str] = set()
    type_counts: Counter[str] = Counter()
    for index, record in enumerate(records, 1):
        if not isinstance(record, dict):
            errors.append(f"benchmark record {index} must be an object")
            continue
        if set(record) != EXPECTED_FIELDS:
            errors.append(f"benchmark record {index} has invalid fields")
            continue
        record_id, prompt, target, kind = (record[field] for field in ("id", "prompt", "target", "type"))
        if not isinstance(record_id, str) or not record_id:
            errors.append(f"benchmark record {index}: id must be a non-empty string")
        elif record_id in ids:
            errors.append(f"benchmark record {index}: duplicate id {record_id!r}")
        else:
            ids.add(record_id)
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"benchmark record {index}: prompt must be a non-empty string")
        if not isinstance(target, str) or target not in SKILLS:
            errors.append(f"benchmark record {index}: invalid target")
        if not isinstance(kind, str) or kind not in EXPECTED_TYPES:
            errors.append(f"benchmark record {index}: invalid type")
        else:
            type_counts[kind] += 1
    if ids != expected_ids:
        errors.append("benchmark IDs must be standalone-v1-001 through standalone-v1-250")
    if dict(type_counts) != EXPECTED_TYPE_COUNTS:
        errors.append(f"benchmark type counts are {dict(type_counts)}, expected {EXPECTED_TYPE_COUNTS}")
    return errors


def validate_decisions(value: Any, expected_ids: set[str]) -> list[str]:
    if not isinstance(value, dict):
        return ["decisions must be a JSON object mapping IDs to labels"]
    actual_ids = set(value)
    errors: list[str] = []
    missing = sorted(expected_ids - actual_ids)
    extra = sorted(actual_ids - expected_ids)
    if missing:
        errors.append(f"missing decision IDs: {missing[:5]}")
    if extra:
        errors.append(f"unexpected decision IDs: {extra[:5]}")
    invalid = {
        record_id: label
        for record_id, label in value.items()
        if not isinstance(record_id, str) or not isinstance(label, str) or label not in SKILLS
    }
    if invalid:
        errors.append(f"invalid decision labels or IDs: {list(invalid.items())[:5]}")
    return errors


def is_explicit(record: dict[str, str]) -> bool:
    target = record["target"].lower()
    prompt = record["prompt"].lower()
    aliases = (target, "terry davis") if target == "terry-davis" else (target,)
    return any(re.search(r"(?<![a-z0-9])" + re.escape(alias) + r"(?![a-z0-9])", prompt) for alias in aliases)


def metric_rows(records: list[dict[str, str]], decisions: dict[str, str]) -> tuple[int, dict[str, dict[str, int | float]], Counter[tuple[str, str]]]:
    correct = 0
    grouped: dict[str, Counter[str]] = defaultdict(Counter)
    by_target: dict[str, Counter[str]] = defaultdict(Counter)
    confusion: Counter[tuple[str, str]] = Counter()
    for record in records:
        gold = record["target"]
        predicted = decisions[record["id"]]
        is_correct = predicted == gold
        correct += int(is_correct)
        kind = record["type"]
        metric_kind = "explicit" if kind == "explicit_or_signature" and is_explicit(record) else "signature" if kind == "explicit_or_signature" else kind
        grouped[metric_kind]["correct"] += int(is_correct)
        grouped[metric_kind]["total"] += 1
        by_target[gold]["correct"] += int(is_correct)
        by_target[gold]["total"] += 1
        if not is_correct:
            confusion[(gold, predicted)] += 1
    def render(groups: dict[str, Counter[str]]) -> dict[str, dict[str, int | float]]:
        return {
            key: {
                "correct": counts["correct"],
                "total": counts["total"],
                "accuracy": counts["correct"] / counts["total"] if counts["total"] else 0.0,
            }
            for key, counts in sorted(groups.items())
        }
    return correct, {"by_type": render(grouped), "by_target": render(by_target)}, confusion


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark", type=Path, default=Path(__file__).resolve().with_name("standalone_trigger_benchmark_v1.json"))
    parser.add_argument("--decisions", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        benchmark = read_json(args.benchmark, "benchmark")
        decisions = read_json(args.decisions, "decisions")
        benchmark_errors = validate_benchmark(benchmark)
        if benchmark_errors:
            raise ValueError("; ".join(benchmark_errors[:8]))
        records = benchmark["records"]
        expected_ids = {record["id"] for record in records}
        decision_errors = validate_decisions(decisions, expected_ids)
        if decision_errors:
            raise ValueError("; ".join(decision_errors))
        correct, grouped, confusion = metric_rows(records, decisions)
        report = {
            "version": "standalone-trigger-v1-scored",
            "total": len(records),
            "correct": correct,
            "accuracy": correct / len(records),
            "by_type": grouped["by_type"],
            "by_target": grouped["by_target"],
            "confusion": [
                {"gold": gold, "predicted": predicted, "count": count}
                for (gold, predicted), count in confusion.most_common()
            ],
            "interpretation": {
                "explicit": "explicit-name rows measure contract recall",
                "signature": "signature rows measure contract recognition without a name",
                "boundary": "semantic boundary discrimination",
                "trap": "negative semantic precision under a nearby request",
                "none": "ordinary-request abstention",
            },
            "independent_scorer_required": True,
        }
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1
    try:
        if args.output:
            args.output.resolve().parent.mkdir(parents=True, exist_ok=True)
            args.output.resolve().write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"FAIL: cannot write report: {exc}")
        return 1
    print(f"Accuracy: {correct}/{len(records)} = {report['accuracy']:.3f}")
    for kind, values in report["by_type"].items():
        print(f"{kind}: {values['correct']}/{values['total']} = {values['accuracy']:.3f}")
    if confusion:
        print("Top confusion pairs:")
        for item in report["confusion"][:10]:
            print(f"  {item['gold']} -> {item['predicted']}: {item['count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
