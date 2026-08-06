#!/usr/bin/env python3
"""Run a deliberately simple, non-AI held-out routing baseline.

The router reads only SKILL.md text and prompts to produce predictions. It does
not use held-out targets during prediction. Targets are used afterward only to
print diagnostics. This is a mechanical baseline, not an independent AI
quality result.
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
STOPWORDS = set("""a an and are as at be been being by can code do does for from has have how
if in into is it its line lines of on or program that the their then this to use
using was what where with write build implement make create every each one two three
four five""".split())
GENERIC = set("""actually activation activate boundary complete computation contract deliverable
example explicit generic logic runnable skill scope task requirements request result
output work""".split())


def tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z][a-z0-9-]+", text.lower())
        if len(token) >= 4 and token not in STOPWORDS and token not in GENERIC
    }


def frontmatter_description(text: str) -> str:
    match = re.search(r"^description:\s*(?:>[-]?\s*)?\n((?:\s{2,}.+\n?)+)", text, re.M)
    if match:
        return " ".join(line.strip() for line in match.group(1).splitlines())
    scalar = re.search(r"^description:\s*(.+)$", text, re.M)
    return scalar.group(1).strip() if scalar else ""


def predict(prompt: str, features: dict[str, set[str]]) -> tuple[str, int, list[str]]:
    prompt_tokens = tokens(prompt)
    scores = {skill: len(prompt_tokens & terms) for skill, terms in features.items()}
    best = max(scores.values(), default=0)
    if best == 0:
        return "none", 0, []
    candidates = sorted(skill for skill, score in scores.items() if score == best)
    return candidates[0], best, candidates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dataset", type=Path, default=Path(__file__).with_name("current_scope_heldout_v1.json"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    data = json.loads(args.dataset.resolve().read_text(encoding="utf-8"))
    records = data["records"]
    features: dict[str, set[str]] = {}
    for skill in SKILLS:
        text = (root / skill / "SKILL.md").read_text(encoding="utf-8")
        description = frontmatter_description(text)
        without_name = re.sub(r"(?i)" + re.escape(skill), " ", description + "\n" + text)
        features[skill] = tokens(without_name)

    rows = []
    for record in records:
        predicted, score, candidates = predict(record["prompt"], features)
        rows.append({
            "id": record["id"],
            "predicted": predicted,
            "score": score,
            "ties": candidates,
            "target": record["target"],
            "type": record["type"],
        })

    by_type: dict[str, list[dict]] = {}
    for row in rows:
        by_type.setdefault(row["type"], []).append(row)
    print("CURRENT HELD-OUT BASELINE (full SKILL.md token overlap; mechanical, not an independent AI evaluation)")
    print(f"records: {len(rows)}")
    for kind in sorted(by_type):
        subset = by_type[kind]
        correct = sum(row["predicted"] == row["target"] for row in subset)
        print(f"{kind}: {correct}/{len(subset)} = {correct / len(subset):.3f}")
    correct = sum(row["predicted"] == row["target"] for row in rows)
    print(f"all: {correct}/{len(rows)} = {correct / len(rows):.3f}")
    confusion = Counter((row["target"], row["predicted"]) for row in rows if row["target"] != row["predicted"])
    print("top confusions:")
    for (target, predicted), count in confusion.most_common(12):
        print(f"  {target} -> {predicted}: {count}")
    report = {
        "version": "current-scope-heldout-v1-baseline",
        "method": "full-SKILL.md-token-overlap",
        "independent_ai_score": False,
        "records": rows,
        "accuracy": correct / len(rows),
        "by_type": {
            kind: {
                "correct": sum(row["predicted"] == row["target"] for row in subset),
                "total": len(subset),
                "accuracy": sum(row["predicted"] == row["target"] for row in subset) / len(subset),
            }
            for kind, subset in sorted(by_type.items())
        },
        "confusions": [
            {"target": target, "predicted": predicted, "count": count}
            for (target, predicted), count in confusion.most_common()
        ],
    }
    if args.output:
        args.output.resolve().parent.mkdir(parents=True, exist_ok=True)
        args.output.resolve().write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
