#!/usr/bin/env python3
"""Rhythm checker for the senryu skill.

Prints the token profile of a code senryu and fails any line outside +/-2 of
the 5-7-5 silhouette. The budget is conserved when fewer lines are used: three
lines ~5/7/5, two lines ~12/5 (setup+turn, then the punchline landing), one
line ~17. Rhythm is not optional at any line count, and the landing stays the
short ~5. Mirrors the benchmark grader's counting convention exactly
(whitespace tokens; imports, comments, and docstring openers are free
ceremony), so a pass here means a pass in the mechanical form check.

Usage:
    python3 scripts/rhythm_check.py solve.py          # check a file
    python3 scripts/rhythm_check.py                   # defaults to ./solve.py
"""
import argparse
import re
import sys
from pathlib import Path

DEFAULT_TARGET = [5, 7, 5]
TOL = 2


def logic_lines(path):
    """Logic-carrying lines only: blank, comments, docstring openers, imports free."""
    out = []
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith('"""') or s.startswith("'''"):
            continue
        if re.match(r"^(import|from) ", s):
            continue
        out.append(s)
    return out


def silhouette(target, n):
    """Collapse the 5-7-5 target to n logic lines (conserved token budget)."""
    if n == 3:
        return target
    if n == 2:
        return [target[0] + target[1], target[2]]
    if n == 1:
        return [sum(target)]
    return target


def main():
    ap = argparse.ArgumentParser(
        description="Print the 5-7-5 token silhouette of a code senryu and fail any line outside +/-2."
    )
    ap.add_argument("path", nargs="?", default="solve.py",
                    help="Python file to check (default: solve.py)")
    ap.add_argument("--target", default=",".join(map(str, DEFAULT_TARGET)),
                    help="target token profile, comma-separated (default 5,7,5)")
    args = ap.parse_args()

    target = [int(x) for x in args.target.split(",")]
    lines = logic_lines(args.path)
    profile = [len(l.split()) for l in lines]
    want = silhouette(target, len(profile))

    print(f"logic lines: {len(lines)} (imports/comments/docstrings are free)")
    for i, line in enumerate(lines, 1):
        t = len(line.split())
        w = want[min(i, len(want)) - 1]
        flag = "OK" if abs(t - w) <= TOL else f"OFF (target {w} +/-{TOL})"
        print(f"  line {i}: {t} tokens  {flag}  | {line.strip()}")

    fails = []
    if not profile:
        fails.append("no logic lines found")
    elif len(profile) > 3:
        fails.append(f"more than 3 logic lines ({len(profile)})")
    else:
        for i, (t, w) in enumerate(zip(profile, want), 1):
            if abs(t - w) > TOL:
                fails.append(f"line {i}: {t} tokens, target {w} +/-{TOL}")

    if fails:
        print(f"FAIL rhythm: {'; '.join(fails)}")
        print(f"profile {profile} vs silhouette {want} +/-{TOL} (from {target})")
        sys.exit(1)
    if len(profile) == 3:
        print(f"PASS rhythm: profile {profile} within +/-{TOL} of {target}")
    else:
        print(f"PASS rhythm: profile {profile} within +/-{TOL} of collapsed "
              f"silhouette {want} (from {target})")
    sys.exit(0)


if __name__ == "__main__":
    main()
