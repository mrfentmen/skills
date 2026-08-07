#!/usr/bin/env python3
"""Shape-convergence analysis for E3 model arms.

Measures how close each arm gets to each form's *shape* (line counts, stanza
structure, silhouette) WITHOUT the strict token-profile ±2 bar. This is the
honest "does the skill change output structure" lens, comparable across the
pre-agentic (13-skill) and agentic (28-skill) runs.
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

# form shape spec: (label, predicate on logic-lines token profile)
# predicate returns (bool, detail)
TARGETS = {
    "choka": ("alternating 5/7-ish, >=6 lines",
              lambda p: len(p) >= 6 and min(p) <= 7 and max(p) >= 6),
    "dodoitsu": ("4 lines", lambda p: len(p) == 4),
    "gogyohka": ("5 lines", lambda p: len(p) == 5),
    "haibun": ("body + 3-line landing", lambda p: len(p) >= 4),
    "haiku": ("1-3 lines (silhouette 5-7-5 conserved)",
              lambda p: len(p) <= 3),
    "katauta": ("3 lines", lambda p: len(p) == 3),
    "lunes": ("3 lines, short middle", lambda p: len(p) == 3),
    "monoku": ("1 line", lambda p: len(p) == 1),
    "renga": ("3+ stanzas of 2-3", lambda p: len(p) >= 6),
    "sedoka": ("6 lines (2x3)", lambda p: len(p) == 6),
    "senryu": ("1-3 lines", lambda p: len(p) <= 3),
    "sijo": ("3 long lines", lambda p: len(p) == 3 and min(p) >= 6),
    "tanka": ("5 lines", lambda p: len(p) == 5),
    "kyoka": ("5 lines", lambda p: len(p) == 5),
    "somonka": ("10 lines (2x5)", lambda p: len(p) == 10),
    "bussokusekika": ("6 lines", lambda p: len(p) == 6),
    "imayo": ("4 lines ~12", lambda p: len(p) == 4),
    "kanshi": ("4 lines", lambda p: len(p) == 4),
    "zappai": ("1-3 lines", lambda p: len(p) <= 3),
    "waka": ("5 lines", lambda p: len(p) == 5),
    "renshi": ("3-6 stages x 2-3", lambda p: len(p) >= 6 and len(p) <= 18),
    "sonnet": ("14 lines", lambda p: len(p) == 14),
    "villanelle": ("19 lines", lambda p: len(p) == 19),
    "cinquain": ("5 lines", lambda p: len(p) == 5),
    "ryuka": ("4 lines", lambda p: len(p) == 4),
    "fibonacci": ("6-8 lines", lambda p: 6 <= len(p) <= 8),
    "limerick": ("5 lines", lambda p: len(p) == 5),
    "etheree": ("10 lines", lambda p: len(p) == 10),
}


def logic_lines(src: str):
    """Match the grader: strip full-line comments and imports; count the rest."""
    lines = []
    for raw in src.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("import ") or line.startswith("from "):
            continue
        # collapse block strings? The grader strips them via ast; approximate:
        lines.append(line)
    return lines


def profile(src: str):
    return [len(l.split()) for l in logic_lines(src)]


def shape_ok(skill: str, src: str) -> tuple[bool, str]:
    p = profile(src)
    label, pred = TARGETS[skill]
    try:
        return pred(p), f"{label} got {len(p)} lines [{','.join(map(str,p[:10]))}]"
    except Exception as e:
        return False, f"err {e}"


def main():
    roots = sys.argv[1:]
    for root in roots:
        root = Path(root)
        print(f"\n=== {root.name} ===")
        total = 0
        hits = 0
        for skill, (label, _) in sorted(TARGETS.items()):
            f = root / f"{skill}.py"
            if not f.is_file():
                continue
            src = f.read_text(encoding="utf-8")
            if src.strip().startswith("# MODEL CALL FAILED"):
                continue
            total += 1
            ok, detail = shape_ok(skill, src)
            hits += ok
            print(f"  {'PASS' if ok else 'fail'} {skill:16s} {detail}")
        print(f"shape: {hits}/{total}")


if __name__ == "__main__":
    main()
