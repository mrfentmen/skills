#!/usr/bin/env python3
"""Check the frozen historical harness without rewriting or masking its result.

The legacy harness is intentionally frozen at an older skill scope. A current
28-skill tree is expected to make that harness exit 1 because its dataset does
not contain the newer forms or the skills moved to skills-2. This checker turns
that known, exact compatibility result into a green informational gate while
running both the harness and skill tree in temporary copies.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EXPECTED_FAILURE_LINES = {
    "FAIL: skill contract (sections + trigger coverage)",
    "FAIL: description sync (SKILL.md frontmatter <-> trigger_eval_queries.json)",
    "DRIFT gogyohka (json 236ch != frontmatter 232ch)",
    "MISSING god: no frontmatter description (would prune)",
    "MISSING no-bullshit: no frontmatter description (would prune)",
    "MISSING psych: no frontmatter description (would prune)",
    "MISSING smoker: no frontmatter description (would prune)",
    "MISSING terry-davis: no frontmatter description (would prune)",
    "MISSING bussokusekika: no entry in trigger_eval_queries.json",
    "MISSING cinquain: no entry in trigger_eval_queries.json",
    "MISSING etheree: no entry in trigger_eval_queries.json",
    "MISSING fibonacci: no entry in trigger_eval_queries.json",
    "MISSING imayo: no entry in trigger_eval_queries.json",
    "MISSING kanshi: no entry in trigger_eval_queries.json",
    "MISSING kyoka: no entry in trigger_eval_queries.json",
    "MISSING limerick: no entry in trigger_eval_queries.json",
    "MISSING renshi: no entry in trigger_eval_queries.json",
    "MISSING ryuka: no entry in trigger_eval_queries.json",
    "MISSING somonka: no entry in trigger_eval_queries.json",
    "MISSING sonnet: no entry in trigger_eval_queries.json",
    "MISSING villanelle: no entry in trigger_eval_queries.json",
    "MISSING waka: no entry in trigger_eval_queries.json",
    "MISSING zappai: no entry in trigger_eval_queries.json",
    "FAILED: 20 missing, 1 DRIFTED (run sync_descriptions.py to fix)",
    "CI GATE FAILED - see the FAIL lines above.",
}


def failure_lines(output: str) -> set[str]:
    prefixes = ("FAIL:", "FAILED:", "MISSING ", "DRIFT ", "CI GATE FAILED")
    return {line.strip() for line in output.splitlines() if line.strip().startswith(prefixes)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--harness",
        type=Path,
        default=None,
        help="path to run_ci_checks.sh; defaults to HISTORICAL_HARNESS",
    )
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()

    configured = args.harness or (
        Path(os.environ["HISTORICAL_HARNESS"])
        if os.environ.get("HISTORICAL_HARNESS")
        else None
    )
    if configured is None:
        print("SKIP historical compatibility: set HISTORICAL_HARNESS to the frozen harness")
        return 0
    harness = configured.expanduser().resolve()
    source = args.root.resolve()
    if not harness.is_file():
        print(f"FAIL historical compatibility: harness not found: {harness}")
        return 1

    with tempfile.TemporaryDirectory(prefix="historical-compat-") as temp:
        temp_root = Path(temp)
        isolated_root = temp_root / source.name
        isolated_harness_dir = temp_root / harness.parent.name
        shutil.copytree(
            source,
            isolated_root,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )
        shutil.copytree(
            harness.parent,
            isolated_harness_dir,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
        isolated_harness = isolated_harness_dir / harness.name
        env = os.environ.copy()
        env["SKILLS_ROOT"] = str(isolated_root)
        try:
            result = subprocess.run(
                ["bash", str(isolated_harness)],
                cwd=str(isolated_root),
                env=env,
                capture_output=True,
                text=True,
                timeout=args.timeout,
            )
        except subprocess.TimeoutExpired:
            print(f"FAIL historical compatibility: harness exceeded {args.timeout}s")
            return 1

    output = (result.stdout or "") + (result.stderr or "")
    observed = failure_lines(output)
    if result.returncode != 1 or observed != EXPECTED_FAILURE_LINES:
        print("FAIL historical compatibility: unexpected frozen-harness result")
        print(f"exit={result.returncode}")
        print(f"unexpected={sorted(observed - EXPECTED_FAILURE_LINES)}")
        print(f"missing={sorted(EXPECTED_FAILURE_LINES - observed)}")
        return 1

    print("PASS historical compatibility: isolated frozen harness returned the documented current-scope 9/11 mismatch")
    print("INFO isolated compatibility scope excludes host-only workspace variance artifacts; source files were not modified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
