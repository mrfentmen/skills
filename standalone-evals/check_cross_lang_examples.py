#!/usr/bin/env python3
"""Rhythm gate for cross-language (JS/Rust/Go/bash) examples in SKILL.md.

Mirrors the Python counting convention exactly: whitespace-separated groups
per logic line; blank lines, full-line comments, and language ceremony
(imports, `use`, `fn main() {`, `}`, `package`, `#!`) are free; inline
trailing comments count as tokens. Every documented cross-language example
must match the skill's structural target (line count, stanza shape) and,
where the form has a token profile, land within +/-2 of it — same standard
as the Python examples, so a model copying any example inherits a correct
shape.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKILLS = ['choka', 'dodoitsu', 'gogyohka', 'haibun', 'haiku', 'katauta', 'lunes',
          'monoku', 'renga', 'sedoka', 'senryu', 'sijo', 'tanka', 'kyoka', 'somonka',
          'bussokusekika', 'imayo', 'kanshi', 'zappai', 'waka', 'renshi', 'sonnet',
          'villanelle', 'cinquain', 'ryuka', 'fibonacci', 'limerick', 'etheree']

# (kind, profile_target) mirroring each skill's rhythm_check.py
PROFILES = {
    'dodoitsu': [7, 7, 7, 5], 'gogyohka': [5, 7, 5, 7, 7], 'haiku': [5, 7, 5],
    'katauta': [5, 7, 7], 'lunes': [5, 3, 5], 'senryu': [5, 7, 5],
    'tanka': [5, 7, 5, 7, 7], 'kyoka': [5, 7, 5, 7, 7], 'bussokusekika': [5, 7, 5, 7, 7, 7],
    'imayo': [7, 7, 7, 7], 'kanshi': [7, 7, 7, 7], 'zappai': [5, 7, 5],
    'waka': [5, 7, 5, 7, 7], 'ryuka': [8, 8, 8, 8], 'cinquain': [2, 4, 6, 8, 2],
    'limerick': [8, 8, 5, 5, 8], 'sonnet': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    'villanelle': [10] * 19, 'etheree': list(range(1, 11)),
}

# Per-skill token tolerance, mirroring each skill's rhythm_check.py TOL exactly.
TOLS = {
    'sonnet': 2, 'villanelle': 3, 'etheree': 1, 'cinquain': 1, 'fibonacci': 1,
    'imayo': 4, 'sedoka': 2, 'somonka': 2,
}
STRUCT = {
    'choka': ('choka', None), 'haibun': ('haibun', None), 'monoku': ('monoku', None),
    'renga': ('renga', None), 'sedoka': ('sedoka', [5, 7, 5, 7, 7, 7]),
    'sijo': ('sijo', None), 'renshi': ('renshi', None), 'fibonacci': ('fibonacci', None),
    'somonka': ('somonka', [5, 7, 5, 7, 7]),
}

CEREMONY = {
    'javascript': (lambda s: s.startswith('import ') or s.startswith('from ')),
    'rust': (lambda s: s.startswith('fn ') or s.startswith('use ')
             or s.startswith('}') or s.startswith('{')),
    'go': (lambda s: s.startswith('package ') or s.startswith('import ')
           or s.startswith('func ') or s.startswith('}') or s.startswith('{')),
    'bash': (lambda s: s.startswith('#')),
}


def logic_lines(code, lang):
    out = []
    for raw in code.splitlines():
        s = raw.strip()
        if not s:
            continue
        if s.startswith('//') or s.startswith('/*') or s.startswith('*'):
            continue
        if CEREMONY[lang](s):
            continue
        if lang == 'bash' and s.startswith('#!'):
            continue
        out.append(s)
    return out


def tok(line):
    return len(line.split())


def check_block(skill, lang, code):
    """Return (ok, messages)."""
    lines = logic_lines(code, lang)
    msgs = []
    profile = [tok(l) for l in lines]
    target = PROFILES.get(skill) or (STRUCT.get(skill, (None, None))[1])
    kind = STRUCT.get(skill, (None, None))[0] if skill not in PROFILES else 'profile'
    tol = TOLS.get(skill, 2)

    if kind == 'profile':
        want = PROFILES[skill]
        if len(lines) != len(want):
            msgs.append(f'{len(lines)} lines, need {len(want)}')
            return False, msgs
        for i, (t, w) in enumerate(zip(profile, want), 1):
            if abs(t - w) > tol:
                msgs.append(f'line {i}: {t} tokens, target {w} +/-{tol}')
        if skill == 'villanelle':
            a_pos = [1, 6, 12, 18]
            b_pos = [3, 9, 15, 19]
            if len(profile) >= 19:
                a_toks = [profile[i - 1] for i in a_pos]
                b_toks = [profile[i - 1] for i in b_pos]
                if max(a_toks) - min(a_toks) > 3:
                    msgs.append(f'refrain A not repeated at {a_pos}: {a_toks}')
                if max(b_toks) - min(b_toks) > 3:
                    msgs.append(f'refrain B not repeated at {b_pos}: {b_toks}')
                if abs(sum(a_toks) / 4 - sum(b_toks) / 4) < 2:
                    msgs.append(f'refrains A and B not distinct ({a_toks} vs {b_toks})')
                # Refrain text must repeat, not just size: heavy token overlap
                # with the first occurrence at each position (inline comments
                # stripped for both // and #).
                def norm(l):
                    return re.split(r'//|#', l)[0].split()
                a_lines = [norm(lines[i - 1]) for i in a_pos]
                b_lines = [norm(lines[i - 1]) for i in b_pos]
                a0, b0 = set(a_lines[0]), set(b_lines[0])
                if not all(len(a0 & set(ln)) / max(1, len(a0)) >= 0.6
                           for ln in a_lines[1:]):
                    msgs.append(f'refrain A text drifts across {a_pos}: {a_lines}')
                if not all(len(b0 & set(ln)) / max(1, len(b0)) >= 0.6
                           for ln in b_lines[1:]):
                    msgs.append(f'refrain B text drifts across {b_pos}: {b_lines}')
    elif kind == 'choka':
        if len(lines) < 6:
            msgs.append(f'{len(lines)} lines, need >=6')
        if len(lines) >= 2 and not (abs(profile[-1] - 7) <= 2 and abs(profile[-2] - 7) <= 2):
            msgs.append(f'closing couplet not ~7-7: {profile[-2:]}')
        if not (any(t < 5 for t in profile) and any(t > 5 for t in profile)):
            msgs.append(f'no short/long alternation in {profile}')
    elif kind == 'haibun':
        comments = sum(1 for l in code.splitlines()
                       if l.strip().startswith('//') or l.strip().startswith('#'))
        if comments < 2:
            msgs.append(f'need narrative comments, got {comments}')
        if len(lines) < 5:
            msgs.append(f'{len(lines)} logic lines, need >=5')
    elif kind == 'monoku':
        if len(lines) != 1:
            msgs.append(f'{len(lines)} logic lines, need 1')
    elif kind == 'renga':
        if len(lines) < 5:
            msgs.append(f'{len(lines)} logic lines, need >=5')
    elif kind == 'renshi':
        if len(lines) < 4:
            msgs.append(f'{len(lines)} logic lines, need >=4')
    elif kind == 'sedoka':
        if len(lines) != 6:
            msgs.append(f'{len(lines)} lines, need 6')
        else:
            for i, (t, w) in enumerate(zip(profile, target), 1):
                if abs(t - w) > tol:
                    msgs.append(f'line {i}: {t} tokens, target {w} +/-{tol}')
            if not re.search(r'reverse|back|mirror|\.rev\(\)|\[::-1\]|reverse\(\)', code):
                msgs.append('second stanza not a mirror')
    elif kind == 'sijo':
        if len(lines) != 3:
            msgs.append(f'{len(lines)} lines, need 3')
        if lines and not all(t >= 12 for t in profile):
            msgs.append(f'lines not long enough: {profile}')
    elif kind == 'fibonacci':
        if not (6 <= len(lines) <= 8):
            msgs.append(f'{len(lines)} lines, need 6-8')
        fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, t in enumerate(profile, 1):
            if not any(abs(t - f) <= 1 for f in fibs):
                msgs.append(f'line {i}: {t} tokens not a fibonacci count (+/-1)')
    elif kind == 'somonka':
        groups = []
        for group in code.split('\n\n'):
            stanza = [l for l in group.splitlines()
                      if l.strip() and not l.strip().startswith('//')
                      and not CEREMONY[lang](l.strip())]
            if stanza:
                groups.append(stanza)
        if len(groups) != 2:
            msgs.append(f'{len(groups)} stanzas, need 2')
            return False, msgs
        for i, st in enumerate(groups, 1):
            if len(st) != 5:
                msgs.append(f'stanza {i}: {len(st)} lines, need 5')
                continue
            for j, (t, w) in enumerate(zip([tok(l) for l in st], target), 1):
                if abs(t - w) > tol:
                    msgs.append(f'stanza {i} line {j}: {t} tokens, target {w} +/-{tol}')
    return not msgs, msgs


def extract_blocks(md):
    """Return [(lang, code, index)] for every cross-language block in a SKILL.md."""
    out = []
    for m in re.finditer(r'```(javascript|rust|go|bash)\n(.*?)```', md, re.DOTALL):
        out.append((m.group(1), m.group(2), len(out)))
    return out


def run_gate(verbose=True):
    fails = []
    checked = 0
    for skill in SKILLS:
        md = (ROOT / skill / 'SKILL.md').read_text(encoding='utf-8', errors='replace')
        for lang, code, _ in extract_blocks(md):
            checked += 1
            ok, msgs = check_block(skill, lang, code)
            if not ok:
                fails.append(f'{skill} [{lang}]: ' + '; '.join(msgs))
    if fails:
        if verbose:
            print('\n'.join(fails))
            print(f'FAIL cross-language gate: {len(fails)} problem block(s) of {checked}')
        return False, fails
    if verbose:
        print(f'PASS cross-language gate: {checked} cross-language example blocks match their form')
    return True, []


if __name__ == '__main__':
    sys.exit(0 if run_gate()[0] else 1)
