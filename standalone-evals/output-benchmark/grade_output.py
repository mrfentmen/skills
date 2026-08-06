#!/usr/bin/env python3
"""Output benchmark grader: runs a program, checks output, checks skill form."""
import json, re, subprocess, sys, argparse
from pathlib import Path

BASE = Path(__file__).resolve().parent
ARMDIR = 'references'

MANIFEST = json.loads((BASE / 'e3-manifest.json').read_text())

def logic_lines(path):
    out = []
    for line in Path(path).read_text().splitlines():
        s = line.strip()
        if not s or s.startswith('#') or s.startswith('"""') or s.startswith("'''"):
            continue
        if re.match(r'^(import|from) ', s):
            continue  # imports are ceremony, free per the skill docs
        out.append(s)
    return out

def tok(line):
    return len(line.split())

def run(pid, path):
    item = next(m for m in MANIFEST['items'] if m['id'] == pid)
    try:
        p = subprocess.run([sys.executable, str(path)], input=item['input'],
                           capture_output=True, text=True, timeout=15, cwd=str(path.parent))
        return p.returncode, p.stdout, p.stderr
    except Exception as e:
        return -2, '', str(e)

def out_ok(pid, stdout):
    item = next(m for m in MANIFEST['items'] if m['id'] == pid)
    exp = item['expected'].strip()
    if not exp:
        return True, ''
    exp_tokens = set(re.findall(r'[a-zA-Z0-9]+', exp.lower()))
    out_tokens = set(re.findall(r'[a-zA-Z0-9]+', stdout.lower()))
    missing = exp_tokens - out_tokens
    if missing:
        return False, f'missing {sorted(missing)}'
    exp_nums = set(re.findall(r'\d+', exp))
    out_nums = set(re.findall(r'\d+', stdout))
    extra = out_nums - exp_nums
    if extra:
        return False, f'unexpected numbers {sorted(extra)}'
    return True, ''

def within(actual, target, tol=2):
    return abs(actual - target) <= tol

def check_form(pid, path):
    lines = logic_lines(path)
    src = Path(path).read_text().lower()
    out = stdout_by[pid].lower()
    fails = []
    def need(cond, msg):
        if not cond:
            fails.append(msg)
    if pid == 'choka':
        need(len(lines) >= 6, f'need >=6 logic lines, got {len(lines)}')
        need(len(lines) >= 2 and within(tok(lines[-1]), 7) and within(tok(lines[-2]), 7),
             f'closing couplet not ~7-7: {[tok(l) for l in lines[-2:]]}')
        toks = [tok(l) for l in lines]
        need(any(t < 5 for t in toks) and any(t > 5 for t in toks),
             f'no short/long alternation in {toks}')
        runs = 1
        for a, b in zip(toks, toks[1:]):
            same = (a < 5 and b < 5) or (a > 7 and b > 7)
            runs = runs + 1 if same else 1
            need(runs < 3, f'too many consecutive like-sized lines: {toks}')
    elif pid == 'dodoitsu':
        need(len(lines) == 4, f'need exactly 4 logic lines, got {len(lines)}')
        need(all(within(t, tgt) for t, tgt in zip([tok(l) for l in lines], [7, 7, 7, 5])),
             f'token profile {[tok(l) for l in lines]} != [7,7,7,5] pm2')
    elif pid == 'god':
        for m in ('creator', 'invariant', 'boundary', 'verif'):
            need(m in src, f'missing god marker: {m}')
    elif pid == 'gogyohka':
        need(len(lines) == 5, f'need exactly 5 logic lines, got {len(lines)}')
    elif pid == 'haibun':
        comments = sum(1 for l in Path(path).read_text().splitlines() if l.strip().startswith('#'))
        need(comments >= 2, f'need narrative comments, got {comments}')
        need(len(lines) >= 5, f'need body + 3-line landing, got {len(lines)} logic lines')
    elif pid == 'haiku':
        toks = [tok(l) for l in lines]
        need(0 < len(toks) <= 3, f'need 1-3 logic lines, got {len(toks)}')
        if 1 <= len(toks) <= 3:
            want = {3: [5, 7, 5], 2: [12, 5], 1: [17]}[len(toks)]
            need(all(within(t, tgt) for t, tgt in zip(toks, want)),
                 f'token profile {toks} not within pm2 of silhouette {want} (5-7-5 conserved)')
    elif pid == 'katauta':
        need(len(lines) == 3, f'need exactly 3 logic lines, got {len(lines)}')
        need(all(within(t, tgt) for t, tgt in zip([tok(l) for l in lines], [5, 7, 7])),
             f'token profile {[tok(l) for l in lines]} != [5,7,7] pm2')
    elif pid == 'lunes':
        need(len(lines) == 3, f'need exactly 3 logic lines, got {len(lines)}')
        toks = [tok(l) for l in lines]
        need(all(within(t, tgt) for t, tgt in zip(toks, [5, 3, 5])),
             f'token profile {toks} != [5,3,5] pm2')
        if len(toks) == 3:
            need(toks[1] < toks[0] and toks[1] <= toks[2], 'middle line not visibly shortest')
    elif pid == 'monoku':
        need(len(lines) == 1, f'need exactly 1 logic line, got {len(lines)}')
    elif pid == 'no-bullshit':
        for m in ('inspect', 'assum', 'plan', 'verif', 'unverif'):
            need(m in out, f'missing report marker in output: {m}')
    elif pid == 'psych':
        need('feedback' in src or 'emerge' in src or 'mutat' in src, 'missing emergent/feedback marker')
        need('grid' in src, 'missing grid concept')
        need('#' in out or '*' in out or '+' in out, 'no visual grid output')
    elif pid == 'renga':
        # stanzas = blank-line separated groups of logic lines
        raw = Path(path).read_text()
        groups = [g.splitlines() for g in raw.split('\n\n') if g.strip()]
        sizes = []
        for g in groups:
            lg = [l for l in g if l.strip() and not l.strip().startswith('#')]
            if lg:
                sizes.append(len(lg))
        need(len(sizes) >= 3, f'need >=3 stanzas, got {sizes}')
        if len(sizes) >= 3:
            need(all(s in (2, 3) for s in sizes), f'stanza sizes not 2/3: {sizes}')
            need(sizes[0] == 3 and sizes[1] == 2 and sizes[2] == 3, f'alternation wrong: {sizes}')
    elif pid == 'sedoka':
        raw = Path(path).read_text()
        groups = [g.splitlines() for g in raw.split('\n\n') if g.strip()]
        sizes = []
        for g in groups:
            lg = [l for l in g if l.strip() and not l.strip().startswith('#')]
            if lg:
                sizes.append(len(lg))
        need(sizes == [3, 3], f'need two 3-line stanzas, got {sizes}')
        for t, tgt in zip([tok(l) for l in lines], [5, 7, 7, 5, 7, 7]):
            need(within(t, tgt), f'token {t} not within pm2 of {tgt}')
        need('reverse' in src or 'back' in src or 'mirror' in src, 'second stanza not a mirror')
    elif pid == 'senryu':
        toks = [tok(l) for l in lines]
        need(0 < len(toks) <= 3, f'need 1-3 logic lines, got {len(toks)}')
        if 1 <= len(toks) <= 3:
            want = {3: [5, 7, 5], 2: [12, 5], 1: [17]}[len(toks)]
            need(all(within(t, tgt) for t, tgt in zip(toks, want)),
                 f'token profile {toks} not within pm2 of silhouette {want} (5-7-5 conserved)')
    elif pid == 'sijo':
        need(len(lines) == 3, f'need exactly 3 logic lines, got {len(lines)}')
        toks = [tok(l) for l in lines]
        need(all(t >= 12 for t in toks), f'lines not long enough: {toks}')
        need('yet' in out or 'but' in out, 'third line missing twist marker')
    elif pid == 'smoker':
        for m in ('inspect', 'fix', 'unverif'):
            need(m in out, f'missing smoker marker in output: {m}')
    elif pid == 'tanka':
        need(len(lines) == 5, f'need exactly 5 logic lines, got {len(lines)}')
        need(all(within(t, tgt) for t, tgt in zip([tok(l) for l in lines], [5, 7, 5, 7, 7])),
             f'token profile {[tok(l) for l in lines]} != [5,7,5,7,7] pm2')
    elif pid == 'terry-davis':
        need(any(m in src for m in ('holy', 'templeos', 'holyc', 'divine')), 'missing TempleOS/HolyC marker')
        need('direct' in src or 'control' in src, 'missing direct-control marker')
    return fails

parser = argparse.ArgumentParser()
parser.add_argument('--dir', default='references')
ARMDIR = parser.parse_args().dir
stdout_by = {}
results = []
for item in MANIFEST['items']:
    pid = item['id']
    path = BASE / ARMDIR / f'{pid}.py'
    rc, so, se = run(pid, path)
    stdout_by[pid] = so
    oo, omsg = out_ok(pid, so)
    form = check_form(pid, path) if rc == 0 else [f'RUNTIME FAIL ({rc})']
    if se.strip():
        form.append('stderr: ' + se.strip()[:80])
    results.append((pid, rc == 0, oo, not form, omsg, form))

ok_all = 0
for pid, runs, out, form, omsg, fl in results:
    passed = runs and out and form
    ok_all += 1 if passed else 0
    print(f'{pid:12s} run={runs} out={out} form={form} | {omsg} {fl if fl else ""}')
print(f'\nPASS {ok_all}/{len(results)} (run + correct output + form)')
