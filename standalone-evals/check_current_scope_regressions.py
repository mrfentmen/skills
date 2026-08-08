#!/usr/bin/env python3
"""Run the versioned current-scope regression checks.

This is the modern replacement for the old cross-scope legacy checks. It never
reads or mutates the frozen external evals-infra artifacts. It validates the
current 28-skill trigger dataset and executable E3 arms, plus the deliberately
frozen 18-skill held-out comparison artifact.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

EXPECTED_SKILLS = [
    "choka", "dodoitsu", "gogyohka", "haibun", "haiku", "katauta", "lunes",
    "monoku", "renga", "sedoka", "senryu", "sijo", "tanka", "kyoka", "somonka",
    "bussokusekika", "imayo", "kanshi", "zappai", "waka", "renshi", "sonnet",
    "villanelle", "cinquain", "ryuka", "fibonacci", "limerick", "etheree",
]
HELDOUT_SKILLS = [
    "choka", "dodoitsu", "god", "gogyohka", "haibun", "haiku", "katauta",
    "lunes", "monoku", "no-bullshit", "psych", "renga", "sedoka", "senryu",
    "sijo", "smoker", "tanka", "terry-davis",
]


def run(command: list[str], cwd: Path) -> tuple[int, str]:
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=180,
        )
    except subprocess.TimeoutExpired:
        raise
    except OSError as exc:
        return 127, f"could not execute {command[0]!r}: {exc}"
    return result.returncode, (result.stdout or "") + (result.stderr or "")


def fail(message: str) -> int:
    print(f"FAIL: current-scope regression gate: {message}")
    return 1


def check_json_contract(root: Path) -> str | None:
    evals = root / "standalone-evals"
    try:
        trigger = json.loads((evals / "standalone_trigger_benchmark_v1.json").read_text(encoding="utf-8"))
        held = json.loads((evals / "current_scope_heldout_v1.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return f"cannot load current datasets: {exc}"

    if trigger.get("skills") != EXPECTED_SKILLS:
        return "trigger benchmark skill list does not match current 28-skill scope"
    if len(trigger.get("records", [])) != 250:
        return f"trigger benchmark has {len(trigger.get('records', []))} records, expected 250"

    records = held.get("records", [])
    if held.get("version") != "current-scope-heldout-v1" or held.get("scope") != "18 current standalone skills":
        return "held-out artifact has an unexpected version or scope"
    if len(records) != 54:
        return f"held-out benchmark has {len(records)} records, expected 54"
    targets = {record.get("target") for record in records}
    if not targets.issubset(set(HELDOUT_SKILLS) | {"none"}):
        return "held-out benchmark contains a target outside its declared frozen 18-skill scope"
    if targets - {"none"} != set(HELDOUT_SKILLS):
        return "held-out benchmark does not cover all 18 declared historical skills"
    return None


def check_output_arms(root: Path) -> str | None:
    base = root / "standalone-evals" / "output-benchmark"
    try:
        manifest = json.loads((base / "e3-manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return f"cannot load E3 manifest: {exc}"
    items = manifest.get("items")
    ids = [item.get("id") for item in items] if isinstance(items, list) else []
    if ids != EXPECTED_SKILLS:
        return "E3 manifest is not exactly the current 28-skill order"

    for arm in ("references", "without_skill"):
        directory = base / arm
        actual = sorted(path.stem for path in directory.glob("*.py")) if directory.is_dir() else []
        if sorted(actual) != sorted(EXPECTED_SKILLS):
            return f"{arm} arm does not contain exactly one file for each current skill"
        command = [sys.executable, str(base / "grade_output.py"), "--dir", arm]
        try:
            code, output = run(command, root)
        except subprocess.TimeoutExpired:
            return f"{arm} grader exceeded 180 seconds"
        expected = "PASS 28/28 (run + correct output + form)" if arm == "references" else "PASS 1/28 (run + correct output + form)"
        if code != 0 or expected not in output:
            return f"{arm} grader did not produce expected {expected!r}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    evals = root / "standalone-evals"

    for command in (
        [sys.executable, str(evals / "validate_standalone_benchmark.py"), "--root", str(root)],
        [sys.executable, str(evals / "validate_current_heldout.py"), "--dataset", str(evals / "current_scope_heldout_v1.json")],
    ):
        try:
            code, output = run(command, root)
        except subprocess.TimeoutExpired:
            return fail(f"{Path(command[1]).name} exceeded 180 seconds")
        if code != 0:
            print(output.rstrip())
            return fail(f"{Path(command[1]).name} failed")

    error = check_json_contract(root)
    if error:
        return fail(error)
    error = check_output_arms(root)
    if error:
        return fail(error)

    print("PASS: current-scope regressions; 250 trigger records, frozen 54 held-out records, 28/28 references, 1/28 frozen control baseline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
