#!/usr/bin/env python3
"""Rhythm gate: every documented example and every E3 reference must pass its own rhythm_check.py.

This locks in the agentic contract: the worked example in each SKILL.md demonstrates
the exact form the checker enforces, so a model that copies the example starts from
a known-pass shape and only has to refine its own task code.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKILLS = ['choka', 'dodoitsu', 'gogyohka', 'haibun', 'haiku', 'katauta', 'lunes',
          'monoku', 'renga', 'sedoka', 'senryu', 'sijo', 'tanka', 'kyoka', 'somonka',
          'bussokusekika', 'imayo', 'kanshi', 'zappai', 'waka', 'renshi', 'sonnet',
          'villanelle', 'cinquain', 'ryuka', 'fibonacci', 'limerick', 'etheree']
E3_SKILLS = ['choka', 'dodoitsu', 'gogyohka', 'haibun', 'haiku', 'katauta', 'lunes',
             'monoku', 'renga', 'sedoka', 'senryu', 'sijo', 'tanka']


def run_checker(skill, paths, cwd):
    script = ROOT / skill / 'scripts' / 'rhythm_check.py'
    if not script.exists():
        return False, f'missing {script}'
    r = subprocess.run([sys.executable, str(script), *paths],
                       capture_output=True, text=True, cwd=str(cwd))
    out = (r.stdout or r.stderr).strip()
    last = out.splitlines()[-1][:110] if out else 'no output'
    return r.returncode == 0, last


fails = []
with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    for skill in SKILLS:
        md = (ROOT / skill / 'SKILL.md').read_text(encoding='utf-8', errors='replace')
        blocks = re.findall(r'```python\n(.*?)```', md, re.DOTALL)
        if not blocks:
            fails.append(f'{skill}: no python example block in SKILL.md')
            continue
        if skill == 'somonka':
            if len(blocks) < 2:
                fails.append('somonka: needs two python blocks (solve + reply)')
                continue
            (td / 'solve.py').write_text(blocks[0])
            (td / 'reply.py').write_text(blocks[1])
            ok, msg = run_checker(skill, ['solve.py', 'reply.py'], td)
        else:
            (td / f'{skill}.py').write_text(blocks[0])
            ok, msg = run_checker(skill, [f'{skill}.py'], td)
        if ok:
            print(f'PASS example {skill}')
        else:
            fails.append(f'{skill} example: {msg}')

    refdir = ROOT / 'standalone-evals' / 'output-benchmark' / 'references'
    for skill in E3_SKILLS:
        ref = refdir / f'{skill}.py'
        if not ref.exists():
            fails.append(f'{skill}: E3 reference missing')
            continue
        ok, msg = run_checker(skill, [f'{skill}.py'], refdir)
        if ok:
            print(f'PASS reference {skill}')
        else:
            fails.append(f'{skill} reference: {msg}')

if fails:
    print('\n'.join(fails))
    print(f'FAIL rhythm gate: {len(fails)} problem(s)')
    sys.exit(1)
print(f'PASS rhythm gate: {len(SKILLS)} documented examples + {len(E3_SKILLS)} E3 references pass their own checkers')
