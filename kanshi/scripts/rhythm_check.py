#!/usr/bin/env python3
"""Rhythm checker for the {skill} skill.

Prints the token profile of a code {skill} and fails any line outside the
form's target with the documented tolerance. Mirrors the benchmark grader's
counting convention exactly (whitespace tokens; imports, comments, and
docstring openers are free ceremony), so a pass here means a pass in the
mechanical form check. Rhythm is adjusted honestly: never pad with filler
statements to hit a count.

Usage:
    python3 scripts/rhythm_check.py solve.py          # check a file
    python3 scripts/rhythm_check.py                   # defaults to ./solve.py
"""

import argparse
import re
import sys
from pathlib import Path

SKILL = "kanshi"
KIND = "profile"
TARGET = [7, 7, 7, 7]
LINES = 4
TOL = 2


def logic_lines(path):
    """Logic-carrying lines only: blank, full-line comments, docstring openers,
    and imports are free; inline trailing comments count as tokens, mirroring
    the benchmark grader exactly."""
    out = []
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith('"""') or s.startswith(chr(39) * 3):
            continue
        if re.match(r"^(import|from) ", s):
            continue
        out.append(s)
    return out


def tok(line):
    return len(line.split())


def within(a, b):
    return abs(a - b) <= TOL


def stanza_sizes(path):
    raw = Path(path).read_text(encoding="utf-8", errors="replace")
    sizes = []
    for group in raw.split("\n\n"):
        if not group.strip():
            continue
        lg = [l for l in group.splitlines()
              if l.strip() and not l.strip().startswith("#")]
        if lg:
            sizes.append(len(lg))
    return sizes


def check_one(path):
    """Return (fails, lines, profile) for a single file."""
    src = Path(path).read_text(encoding="utf-8", errors="replace")
    lines = logic_lines(path)
    profile = [tok(l) for l in lines]
    fails = []

    def need(cond, msg):
        if not cond:
            fails.append(msg)

    if KIND == "profile":
        need(len(lines) == LINES,
             f"need exactly {LINES} logic lines, got {len(lines)}")
        for i, (t, tgt) in enumerate(zip(profile, TARGET), 1):
            need(within(t, tgt), f"line {i}: {t} tokens, target {tgt} +/-{TOL}")
    elif KIND == "lines":
        need(len(lines) == LINES,
             f"need exactly {LINES} logic lines, got {len(lines)}")
    elif KIND == "silhouette":
        need(0 < len(profile) <= 3,
             f"need 1-3 logic lines, got {len(profile)}")
        if 1 <= len(profile) <= 3:
            want = {3: TARGET, 2: [TARGET[0] + TARGET[1], TARGET[2]],
                    1: [sum(TARGET)]}[len(profile)]
            for i, (t, tgt) in enumerate(zip(profile, want), 1):
                need(within(t, tgt),
                     f"line {i}: {t} tokens, target {tgt} +/-{TOL} "
                     f"(silhouette {want} from {TARGET})")
    elif KIND == "choka":
        need(len(lines) >= 6, f"need >=6 logic lines, got {len(lines)}")
        need(len(lines) >= 2 and within(tok(lines[-1]), 7) and within(tok(lines[-2]), 7),
             f"closing couplet not ~7-7: {profile[-2:] if len(profile) >= 2 else profile}")
        need(any(t < 5 for t in profile) and any(t > 5 for t in profile),
             f"no short/long alternation in {profile}")
        runs = 1
        for a, b in zip(profile, profile[1:]):
            same = (a < 5 and b < 5) or (a > 7 and b > 7)
            runs = runs + 1 if same else 1
            need(runs < 3, f"too many consecutive like-sized lines: {profile}")
    elif KIND == "haibun":
        comments = sum(1 for l in Path(path).read_text(encoding="utf-8",
                       errors="replace").splitlines() if l.strip().startswith("#"))
        need(comments >= 2, f"need narrative comments, got {comments}")
        need(len(lines) >= 5, f"need body + 3-line landing, got {len(lines)} logic lines")
    elif KIND == "lunes":
        need(len(lines) == 3, f"need exactly 3 logic lines, got {len(lines)}")
        for i, (t, tgt) in enumerate(zip(profile, TARGET), 1):
            need(within(t, tgt), f"line {i}: {t} tokens, target {tgt} +/-{TOL}")
        if len(profile) == 3:
            need(profile[1] < profile[0] and profile[1] <= profile[2],
                 "middle line not visibly shortest")
    elif KIND == "monoku":
        need(len(lines) == 1, f"need exactly 1 logic line, got {len(lines)}")
    elif KIND == "renga":
        sizes = stanza_sizes(path)
        need(len(sizes) >= 3, f"need >=3 stanzas, got {sizes}")
        if len(sizes) >= 3:
            need(all(s in (2, 3) for s in sizes), f"stanza sizes not 2/3: {sizes}")
            need(sizes[0] == 3 and sizes[1] == 2 and sizes[2] == 3,
                 f"alternation wrong: {sizes}")
    elif KIND == "sedoka":
        sizes = stanza_sizes(path)
        need(sizes == [3, 3], f"need two 3-line stanzas, got {sizes}")
        for i, (t, tgt) in enumerate(zip(profile, TARGET), 1):
            need(within(t, tgt), f"line {i}: {t} tokens, target {tgt} +/-{TOL}")
        need(bool(re.search(r"reverse|back|mirror|\[::-1\]", src)),
             "second stanza not a mirror")
    elif KIND == "sijo":
        need(len(lines) == 3, f"need exactly 3 logic lines, got {len(lines)}")
        need(all(t >= 12 for t in profile), f"lines not long enough: {profile}")
        if len(lines) == 3:
            need(bool(re.search(r"\b(yet|but|however|still|despite|instead|although)\b",
                                lines[2])),
                 "third line missing twist marker (yet/but/however/still/despite/instead/although)")
    elif KIND == "villanelle":
        need(len(lines) == 19, f"need 19 logic lines, got {len(lines)}")
        for i, t in enumerate(profile, 1):
            need(within(t, 10), f"line {i}: {t} tokens, target ~10 +/-{TOL}")
        a_pos = [1, 6, 12, 18]
        b_pos = [3, 9, 15, 19]
        if len(profile) >= 19:
            a_toks = [profile[i - 1] for i in a_pos]
            b_toks = [profile[i - 1] for i in b_pos]
            need(max(a_toks) - min(a_toks) <= 3,
                 f"refrain A not repeated at {a_pos}: {a_toks}")
            need(max(b_toks) - min(b_toks) <= 3,
                 f"refrain B not repeated at {b_pos}: {b_toks}")
            need(abs(sum(a_toks) / 4 - sum(b_toks) / 4) >= 2,
                 f"refrains A and B not distinct ({a_toks} vs {b_toks})")
    elif KIND == "fibonacci":
        need(6 <= len(lines) <= 8, f"need 6-8 logic lines, got {len(lines)}")
        fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, t in enumerate(profile, 1):
            need(any(abs(t - f) <= 1 for f in fibs),
                 f"line {i}: {t} tokens not a fibonacci count (+/-1)")
        for i in range(2, len(profile)):
            need(abs(profile[i] - (profile[i - 1] + profile[i - 2])) <= 3,
                 f"line {i + 1}: {profile[i]} is not the sum of "
                 f"{profile[i - 2]} and {profile[i - 1]} (+/-3)")
        need(profile[-1] >= 5, "final line too small to carry the result")
    elif KIND == "renshi":
        sizes = stanza_sizes(path)
        need(3 <= len(sizes) <= 6, f"need 3-6 stages, got {len(sizes)}")
        need(all(s in (2, 3) for s in sizes), f"stage sizes not 2-3 lines: {sizes}")
    return fails, lines, profile


def report(path, lines, profile, fails):
    print(f"logic lines: {len(lines)} (imports/comments/docstrings are free)")
    for i, line in enumerate(lines, 1):
        print(f"  line {i}: {len(line.split())} tokens  | {line.strip()}")
    if fails:
        print(f"FAIL rhythm ({SKILL}): {'; '.join(fails)}")
        print(f"profile {profile}")
        return 1
    print(f"PASS rhythm ({SKILL}): profile {profile}")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description=f"Check the {SKILL} rhythm (token profile) of a Python file.")
    ap.add_argument("paths", nargs="+", default=["solve.py"],
                    help="file(s) to check (default: solve.py)")
    args = ap.parse_args()

    paths = args.paths
    if len(paths) == 1:
        paths = [paths[0]]
    if KIND == "somonka":
        if len(paths) < 2:
            paths = [paths[0], "reply.py"]
            print("somonka: checking solve.py and reply.py")
        rc = 0
        for p in paths:
            fails, lines, profile = check_one(p)
            rc = max(rc, report(p, lines, profile, fails))
        sys.exit(rc)

    fails, lines, profile = check_one(paths[0])
    sys.exit(report(paths[0], lines, profile, fails))


if __name__ == "__main__":
    main()
