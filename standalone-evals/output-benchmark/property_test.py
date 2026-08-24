#!/usr/bin/env python3
"""
Differential property-based tester for the output benchmark.

The single-input grader (grade_output.py) only checks one fixed input per
skill, so a program can pass by memorizing the example or special-casing that
input. This tester runs the candidate AND the verified reference on N random
inputs per skill and requires the candidate's output to match the reference's
on every one of them (same token-subset semantics as grade_output.out_ok).

A program that hardcodes the answer for the fixed input fails here the moment
the input changes. This is the anti-memorization / anti-gaming gate.

Usage:
    python3 property_test.py --dir <dir> [--n 8] [--seed 42]
    # --dir defaults to references (self-check: references must pass 28/28)
"""
from __future__ import annotations

import argparse
import json
import random
import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
MANIFEST = json.loads((BASE / 'e3-manifest.json').read_text())
REFS = BASE / 'references'

# Input-shape generators, one per skill. Each returns a string that the
# reference program is guaranteed to handle (non-empty, sane ranges, no
# division-by-zero, etc.).
WORDS = ['the', 'quick', 'brown', 'fox', 'jumps', 'lazy', 'dog', 'sun',
         'moon', 'star', 'wind', 'rain', 'night', 'dawn', 'sea', 'hill']


def gen_numbers(rng: random.Random, neg: bool = False) -> str:
    n = rng.randint(2, 8)
    lo, hi = (-20, 20) if neg else (1, 20)
    vals = [rng.randint(lo, hi) for _ in range(n)]
    if neg:
        # guarantee at least one positive and one negative so up/down both appear
        vals[0] = rng.randint(1, 20)
        vals[1] = rng.randint(-20, -1)
    return ' '.join(str(v) for v in vals) + '\n'


def gen_words(rng: random.Random) -> str:
    n = rng.randint(2, 8)
    return ' '.join(rng.choice(WORDS) for _ in range(n)) + '\n'


def gen_log(rng: random.Random) -> str:
    n = rng.randint(3, 8)
    kinds = ['INFO ok', 'ERROR bad', 'WARN slow', 'ERROR worse', 'INFO fine', 'WARN meh']
    # guarantee at least one ERROR so error-count references stay meaningful
    lines = [rng.choice(kinds) for _ in range(n)]
    lines[0] = 'ERROR bad'
    return '\n'.join(lines) + '\n'


def gen_single(rng: random.Random) -> str:
    return str(rng.randint(1, 20)) + '\n'


# skill -> generator. Skills not listed here are skipped (no safe random shape).
GENERATORS = {
    'choka': gen_numbers, 'dodoitsu': gen_numbers, 'haiku': gen_numbers,
    'katauta': gen_numbers, 'lunes': gen_numbers, 'monoku': gen_numbers,
    'renga': gen_numbers, 'sedoka': gen_numbers, 'sijo': gen_numbers,
    'tanka': gen_numbers, 'kyoka': gen_numbers, 'somonka': gen_numbers,
    'bussokusekika': gen_numbers, 'imayo': gen_numbers, 'kanshi': gen_numbers,
    'zappai': gen_numbers, 'waka': gen_numbers, 'sonnet': gen_numbers,
    'fibonacci': gen_numbers, 'limerick': gen_numbers, 'etheree': gen_words,
    'gogyohka': gen_words, 'renshi': gen_words, 'cinquain': gen_words,
    'ryuka': lambda r: gen_numbers(r, neg=True),
    'senryu': gen_single,
    'haibun': gen_log, 'villanelle': gen_log,
}


def run(pid: str, path: Path, input_text: str) -> tuple[int, str, str]:
    try:
        p = subprocess.run([sys.executable, str(path)], input=input_text,
                           capture_output=True, text=True, timeout=15,
                           cwd=str(path.parent))
        return p.returncode, p.stdout, p.stderr
    except Exception as e:  # noqa: BLE001
        return -2, '', str(e)


def tokens(text: str) -> set[str]:
    return set(re.findall(r'[a-zA-Z0-9]+', text.lower()))


def nums(text: str) -> set[str]:
    return set(re.findall(r'\d+', text))


def matches(ref_out: str, cand_out: str) -> tuple[bool, str]:
    """Anti-gaming differential check, focused on the COMPUTATIONAL content.

    The reference and candidate are different poems, so their decorative words
    legitimately differ. What must match is the numbers the task actually
    computes: the candidate's numeric output must contain every number the
    reference reports (no missing result) and no number the reference does not
    report on the same input (no hallucinated/extra result). Word-level poetry
    is free to differ.

    This is what kills memorization: a hardcoded `sum 14` either misses the
    real sum on a different input (missing number) or reports 14 when the
    reference does not (extra number).
    """
    ref_n = nums(ref_out)
    cand_n = nums(cand_out)
    missing = ref_n - cand_n
    if missing:
        return False, f'missing numbers {sorted(missing)}'
    extra = cand_n - ref_n
    if extra:
        return False, f'unexpected numbers {sorted(extra)}'
    return True, ''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', default='references')
    ap.add_argument('--n', type=int, default=8, help='random inputs per skill')
    ap.add_argument('--seed', type=int, default=42)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    fails = []
    tested = passed = skipped = 0
    for item in MANIFEST['items']:
        pid = item['skill']
        gen = GENERATORS.get(pid)
        cand = BASE / args.dir / f'{pid}.py'
        ref = REFS / f'{pid}.py'
        if not gen or not cand.is_file() or not ref.is_file():
            continue
        head = cand.read_text(encoding='utf-8', errors='replace').splitlines()[:1]
        if head and head[0].strip() == '# MODEL CALL FAILED':
            # a quota placeholder is not real code; report it separately
            skipped += 1
            continue
        tested += 1
        # verify the reference itself runs on all generated inputs (it must —
        # if it doesn't, our generator is wrong, not the candidate)
        ref_ok = True
        for _ in range(args.n):
            inp = gen(rng)
            rrc, rso, _ = run(pid, ref, inp)
            if rrc != 0:
                ref_ok = False
                break
        if not ref_ok:
            fails.append(f'{pid}: reference failed a generated input (bad generator)')
            continue
        # now test the candidate against the reference on N fresh inputs
        rng.seed(args.seed)  # same inputs for ref and candidate
        skill_fail = None
        for i in range(args.n):
            inp = gen(rng)
            rrc, rso, _ = run(pid, ref, inp)
            crc, cso, cse = run(pid, cand, inp)
            if crc != 0:
                skill_fail = f'input {i}: RUNTIME FAIL ({crc})'
                break
            ok, msg = matches(rso, cso)
            if not ok:
                skill_fail = f'input {i}: {msg}'
                break
        if skill_fail:
            fails.append(f'{pid}: {skill_fail}')
        else:
            passed += 1
            print(f'PASS property {pid} ({args.n} random inputs)')
    print(f'\nPROPERTY GATE: {passed}/{tested} passed (differential vs reference, '
          f'{args.n} inputs/skill, seed {args.seed}, {skipped} quota placeholders skipped)')
    if fails:
        print('FAILURES:')
        for f in fails:
            print('  ' + f)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
