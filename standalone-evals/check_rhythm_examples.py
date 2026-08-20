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
             'monoku', 'renga', 'sedoka', 'senryu', 'sijo', 'tanka', 'kyoka', 'somonka',
             'bussokusekika', 'imayo', 'kanshi', 'zappai', 'waka', 'renshi', 'sonnet',
             'villanelle', 'cinquain', 'ryuka', 'fibonacci', 'limerick', 'etheree']


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
            # Somonka is one deliverable with two blank-line-separated
            # stanzas. Every python block with two non-empty stanza groups
            # must pass the checker; single-stanza fragments are not full
            # somonka and are skipped (the ten-slot template is one of the
            # two-stanza blocks).
            block_fails = []
            two_stanza = [b for b in blocks
                          if len([g for g in b.split('\n\n') if g.strip()]) >= 2]
            if not two_stanza:
                fails.append('somonka: needs at least one two-stanza python block')
                continue
            for i, block in enumerate(two_stanza):
                (td / 'somonka.py').write_text(block)
                ok, msg = run_checker(skill, ['somonka.py'], td)
                if not ok:
                    block_fails.append(f'two-stanza block {i}: {msg}')
            if block_fails:
                fails.append(f'somonka example(s): ' + ' | '.join(block_fails))
            else:
                print(f'PASS example {skill} ({len(two_stanza)} two-stanza blocks)')
        else:
            # Every documented example block must pass its own checker, not
            # just the first: a model told to copy an example inherits the
            # shape it demonstrates, so a broken example teaches a broken form.
            block_fails = []
            for i, block in enumerate(blocks):
                (td / f'{skill}.py').write_text(block)
                ok, msg = run_checker(skill, [f'{skill}.py'], td)
                if not ok:
                    block_fails.append(f'block {i}: {msg}')
            if block_fails:
                fails.append(f'{skill} example(s): ' + ' | '.join(block_fails))
            else:
                print(f'PASS example {skill} ({len(blocks)} blocks)')

    refdir = ROOT / 'standalone-evals' / 'output-benchmark' / 'references'
    for skill in E3_SKILLS:
        ref = refdir / f'{skill}.py'
        if not ref.exists():
            fails.append(f'{skill}: E3 reference missing')
            continue
        if skill == 'somonka':
            # E3 somonka reference is one file with two blank-line-separated
            # 5-line stanzas (the skill's rhythm_check takes two files instead).
            raw = ref.read_text(encoding='utf-8')
            groups = [g.splitlines() for g in raw.split('\n\n') if g.strip()]
            stanzas = [[l for l in g
                        if l.strip() and not l.strip().startswith('#')
                        and not re.match(r'^(import|from) ', l.strip())]
                       for g in groups]
            msgs = []
            ok = len(stanzas) == 2
            msgs.append(f'stanzas {[len(s) for s in stanzas]} (need 2)')
            if ok:
                for i, st in enumerate(stanzas, 1):
                    ok = ok and len(st) == 5
                    msgs.append(f'stanza {i} lines {len(st)} (need 5)')
                    toks = [len(l.split()) for l in st]
                    ok = ok and all(abs(t - tgt) <= 2
                                    for t, tgt in zip(toks, [5, 7, 5, 7, 7]))
                    msgs.append(f'stanza {i} profile {toks} (need [5,7,5,7,7] pm2)')
            if ok:
                print('PASS reference somonka')
            else:
                fails.append(f'somonka reference: {msgs}')
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
print(f'PASS rhythm gate: {len(SKILLS)} documented examples + {len(E3_SKILLS)} E3 references pass their own checkers (somonka via inline stanza check)')
