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
        if re.match(r'^(import|from) ', s) and ';' not in s:
            continue  # pure imports are ceremony; inline import+logic is countable
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
        couplet = [tok(l) for l in lines[-2:]] if len(lines) >= 2 else []
        need(bool(couplet) and all(within(t, 7) for t in couplet),
             f'closing couplet not ~7-7: {couplet}')
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
        need(not any(';' in line for line in lines),
             'each breath must be one visible statement; split semicolon-packed lines')
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
    elif pid == 'kyoka':
        toks = [tok(l) for l in lines]
        need(len(lines) == 5, f'need exactly 5 logic lines, got {len(lines)}')
        need(all(within(t, tgt) for t, tgt in zip(toks, [5, 7, 5, 7, 7])),
             f'token profile {toks} != [5,7,5,7,7] pm2')
    elif pid == 'somonka':
        raw = Path(path).read_text()
        groups = [g.splitlines() for g in raw.split('\n\n') if g.strip()]
        stanzas = []
        for g in groups:
            lg = [l for l in g
                  if l.strip() and not l.strip().startswith('#')
                  and not re.match(r'^(import|from) ', l.strip())]
            if lg:
                stanzas.append(lg)
        need(len(stanzas) == 2, f'need two blank-line-separated stanzas, got {len(stanzas)}')
        if len(stanzas) == 2:
            for i, st in enumerate(stanzas, 1):
                toks = [tok(l) for l in st]
                need(len(st) == 5, f'stanza {i} has {len(st)} lines, need 5')
                need(all(within(t, tgt) for t, tgt in zip(toks, [5, 7, 5, 7, 7])),
                     f'stanza {i} profile {toks} != [5,7,5,7,7] pm2')
    elif pid == 'bussokusekika':
        toks = [tok(l) for l in lines]
        need(len(lines) == 6, f'need exactly 6 logic lines, got {len(lines)}')
        need(all(within(t, tgt) for t, tgt in zip(toks, [5, 7, 5, 7, 7, 7])),
             f'token profile {toks} != [5,7,5,7,7,7] pm2')
    elif pid == 'imayo':
        toks = [tok(l) for l in lines]
        need(len(lines) == 4, f'need exactly 4 logic lines, got {len(lines)}')
        need(all(within(t, 12, 4) for t in toks),
             f'lines not ~12 pm4 (7-5 long-short): {toks}')
    elif pid == 'kanshi':
        toks = [tok(l) for l in lines]
        need(len(lines) == 4, f'need exactly 4 logic lines, got {len(lines)}')
        need(all(within(t, tgt) for t, tgt in zip(toks, [7, 7, 7, 7])),
             f'token profile {toks} != [7,7,7,7] pm2')
    elif pid == 'zappai':
        toks = [tok(l) for l in lines]
        need(0 < len(toks) <= 3, f'need 1-3 logic lines, got {len(toks)}')
        if 1 <= len(toks) <= 3:
            want = {3: [5, 7, 5], 2: [12, 5], 1: [17]}[len(toks)]
            need(all(within(t, tgt) for t, tgt in zip(toks, want)),
                 f'token profile {toks} not within pm2 of silhouette {want} (5-7-5 conserved)')
    elif pid == 'waka':
        toks = [tok(l) for l in lines]
        need(len(lines) == 5, f'need exactly 5 logic lines, got {len(lines)}')
        need(all(within(t, tgt) for t, tgt in zip(toks, [5, 7, 5, 7, 7])),
             f'token profile {toks} != [5,7,5,7,7] pm2')
    elif pid == 'renshi':
        raw = Path(path).read_text()
        groups = [g.splitlines() for g in raw.split('\n\n') if g.strip()]
        sizes = []
        for g in groups:
            lg = [l for l in g if l.strip() and not l.strip().startswith('#')]
            if lg:
                sizes.append(len(lg))
        need(3 <= len(sizes) <= 6, f'need 3-6 stages, got {len(sizes)}')
        need(all(s in (2, 3) for s in sizes), f'stage sizes not 2-3 lines: {sizes}')
    elif pid == 'sonnet':
        toks = [tok(l) for l in lines]
        need(len(lines) == 14, f'need exactly 14 logic lines, got {len(lines)}')
        need(all(within(t, 10) for t in toks),
             f'lines not ~10 tokens pm2 (iambic pentameter analog): {toks}')
    elif pid == 'villanelle':
        toks = [tok(l) for l in lines]
        need(len(lines) == 19, f'need exactly 19 logic lines, got {len(lines)}')
        need(all(within(t, 10, 3) for t in toks),
             f'lines not ~10 tokens pm3: {toks}')
        a_pos = [1, 6, 12, 18]
        b_pos = [3, 9, 15, 19]
        if len(toks) >= 19:
            a_toks = [toks[i - 1] for i in a_pos]
            b_toks = [toks[i - 1] for i in b_pos]
            need(max(a_toks) - min(a_toks) <= 3,
                 f'refrain A not repeated at {a_pos}: {a_toks}')
            need(max(b_toks) - min(b_toks) <= 3,
                 f'refrain B not repeated at {b_pos}: {b_toks}')
            need(abs(sum(a_toks) / 4 - sum(b_toks) / 4) >= 2,
                 f'refrains A and B not distinct ({a_toks} vs {b_toks})')
            # The refrains must be the same expression each return, not just
            # similar-sized lines: require heavy token overlap with the first
            # occurrence at each position (comments stripped).
            def norm(l):
                return l.split('#', 1)[0].split()
            a_lines = [norm(lines[i - 1]) for i in a_pos]
            b_lines = [norm(lines[i - 1]) for i in b_pos]
            a0, b0 = set(a_lines[0]), set(b_lines[0])
            need(all(len(a0 & set(ln)) / max(1, len(a0)) >= 0.6
                     for ln in a_lines[1:]),
                 f'refrain A text drifts across {a_pos}: {a_lines}')
            need(all(len(b0 & set(ln)) / max(1, len(b0)) >= 0.6
                     for ln in b_lines[1:]),
                 f'refrain B text drifts across {b_pos}: {b_lines}')
    elif pid == 'cinquain':
        toks = [tok(l) for l in lines]
        need(len(lines) == 5, f'need exactly 5 logic lines, got {len(lines)}')
        need(all(within(t, tgt, 1) for t, tgt in zip(toks, [2, 4, 6, 8, 2])),
             f'token profile {toks} != [2,4,6,8,2] pm1')
    elif pid == 'ryuka':
        toks = [tok(l) for l in lines]
        need(len(lines) == 4, f'need exactly 4 logic lines, got {len(lines)}')
        need(all(within(t, tgt) for t, tgt in zip(toks, [8, 8, 8, 6])),
             f'token profile {toks} != [8,8,8,6] pm2')
    elif pid == 'fibonacci':
        toks = [tok(l) for l in lines]
        fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        need(6 <= len(toks) <= 8, f'need 6-8 logic lines, got {len(toks)}')
        need(all(any(abs(t - f) <= 1 for f in fibs) for t in toks),
             f'token counts not fibonacci (+/-1): {toks}')
        for i in range(2, len(toks)):
            need(abs(toks[i] - (toks[i - 1] + toks[i - 2])) <= 3,
                 f'line {i + 1}: {toks[i]} is not the sum of {toks[i - 2]} and {toks[i - 1]} (+/-3)')
        need(len(toks) > 0 and toks[-1] >= 5, 'final line too small to carry the result')
    elif pid == 'limerick':
        toks = [tok(l) for l in lines]
        need(len(lines) == 5, f'need exactly 5 logic lines, got {len(lines)}')
        need(all(within(t, tgt) for t, tgt in zip(toks, [8, 8, 5, 5, 8])),
             f'token profile {toks} != [8,8,5,5,8] pm2')
    elif pid == 'etheree':
        toks = [tok(l) for l in lines]
        need(len(lines) == 10, f'need exactly 10 logic lines, got {len(lines)}')
        need(all(within(t, i + 1, 1) for i, t in enumerate(toks)),
             f'ladder not 1-10 pm1: {toks}')
    return fails

parser = argparse.ArgumentParser()
parser.add_argument('--dir', default='references')
ARMDIR = parser.parse_args().dir
stdout_by = {}
results = []
for item in MANIFEST['items']:
    pid = item['id']
    path = BASE / ARMDIR / f'{pid}.py'
    head = path.read_text(encoding='utf-8', errors='replace').splitlines()[:1] if path.is_file() else ['']
    if head and head[0].strip() == '# MODEL CALL FAILED':
        # an arm that never produced code: report it honestly as a failure
        results.append((pid, False, False, False, '', ['MODEL CALL FAILED']))
        continue
    rc, so, se = run(pid, path)
    stdout_by[pid] = so
    oo, omsg = out_ok(pid, so)
    form = check_form(pid, path) if rc == 0 else [f'RUNTIME FAIL ({rc})']
    if se.strip():
        # The actionable part of a traceback is the tail (failing line + error
        # type/message), not the leading file path; the agentic loop feeds this
        # straight back to the model, so truncating to the head made runtime
        # errors invisible. Cap at the last ~700 chars instead.
        se = se.strip()
        if len(se) > 700:
            se = '...' + se[-700:]
        form.append('stderr: ' + se)
    results.append((pid, rc == 0, oo, not form, omsg, form))

ok_all = 0
for pid, runs, out, form, omsg, fl in results:
    passed = runs and out and form
    ok_all += 1 if passed else 0
    print(f'{pid:12s} run={runs} out={out} form={form} | {omsg} {fl if fl else ""}')
print(f'\nPASS {ok_all}/{len(results)} (run + correct output + form)')
