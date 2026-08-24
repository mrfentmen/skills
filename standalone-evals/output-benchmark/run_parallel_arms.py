#!/usr/bin/env python3
"""
Parallel agentic-arms launcher.

Spawns several run_feedback_arms.py worker processes CONCURRENTLY so that
multiple providers AND multiple skills are worked at once. Instead of the
sequential provider1-skills-then-provider2-skills behavior, every (provider,
skill-slice) worker runs in parallel and each worker owns a disjoint slice of
the skill list, so wall-clock time collapses to roughly one provider's worth of
sequential work.

Two modes:

  1. Probe mode (--probe): fire one tiny chat call at every configured provider
     at once and print a live status table (OK / rate-limited / error). Use it
     to find which free-tier windows are open before committing a run.

  2. Run mode (default): launch parallel workers and aggregate the per-provider
     agentic logs into a result table when they finish.

Examples:
  # find which providers have live quota right now (parallel pings)
  python3 run_parallel_arms.py --probe

  # work villanelle+etheree across three providers at once, 2 workers/prov
  python3 run_parallel_arms.py \\
      --providers mistral-small,or-north-mini-code,groq-qwen3.6-27b \\
      --skills villanelle,etheree --workers 2 --max-iters 6 --max-minutes 10

  # all skills across every live provider, 1 worker each (default)
  python3 run_parallel_arms.py

Env: keys are read from the repo-root .env.benchmark automatically if present,
so `source .env.benchmark` is not required.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
ENV_FILE = ROOT / '.env.benchmark'
LOG_DIR = BASE / '_parallel_logs'

# Minimal probe prompt; keep max_tokens tiny so a probe costs almost nothing.
PROBE_BODY = (
    '{"model": "%s", "messages": [{"role": "user", "content": "reply ok"}], '
    '"max_tokens": 8}'
)


def load_env() -> None:
    """Load repo-root .env.benchmark into the environment if present (no override)."""
    if not ENV_FILE.is_file():
        return
    for raw in ENV_FILE.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        os.environ.setdefault(k.strip(), v.strip())


def probe_provider(name: str, prov: dict) -> str:
    """One tiny chat call; returns a short status string."""
    keys = [k.strip() for k in os.environ.get(prov['key_env'], '').split(',') if k.strip()]
    if not keys:
        return 'NO-KEY'
    url = prov['url']
    body = PROBE_BODY % prov['model']
    cmd = ['curl', '-sS', '--max-time', '20', url, '-H', 'Content-Type: application/json',
           '-d', body]
    if not prov.get('no_auth'):
        cmd += ['-H', f'Authorization: Bearer {keys[0]}']
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout
    except Exception as e:  # noqa: BLE001
        return f'ERR {type(e).__name__}'
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return 'NON-JSON'
    if data.get('choices'):
        return 'OK'
    err = data.get('error', {})
    msg = str(err.get('message', ''))[:60]
    if 'rate' in msg.lower() or 'limit' in msg.lower():
        return f'RATE-LIMITED ({msg[:40]})'
    return f'ERR ({msg[:40]})'


def probe_all(providers: dict, names: list[str]) -> int:
    """Parallel probe of every requested provider; prints a status table."""
    results: dict[str, str] = {}
    threads = []

    def work(name: str) -> None:
        results[name] = probe_provider(name, providers[name])

    for n in names:
        t = threading.Thread(target=work, args=(n,), daemon=True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print(f'\n=== provider probe ({time.strftime("%H:%M:%S")}) ===')
    for n in names:
        print(f'  {n:24s} {providers[n]["model"]:38s} {results.get(n, "?")}')
    ok = sum(1 for v in results.values() if v == 'OK')
    print(f'--- {ok}/{len(names)} live ---')
    return 0


def shard(items: list[str], n: int) -> list[list[str]]:
    """Split a list into n roughly-equal, non-empty slices (n capped at len)."""
    n = max(1, min(n, len(items)))
    out: list[list[str]] = []
    for i in range(n):
        out.append(items[i::n])
    return out


def run_workers(args) -> int:
    providers = args.providers
    skills = [s.strip() for s in args.skills.split(',') if s.strip()]
    if not skills:
        skills = [i['skill'] for i in json.loads((BASE / 'e3-manifest.json').read_text())['items']]
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    jobs: list[tuple[str, list[str], Path]] = []
    for name in providers:
        for slice_i, slice_skills in enumerate(shard(skills, args.workers)):
            if not slice_skills:
                continue
            jobs.append((name, slice_skills, LOG_DIR / f'{name}-w{slice_i}.log'))

    print(f'=== parallel arms: {len(providers)} providers x {args.workers} workers '
          f'= {len(jobs)} concurrent jobs, {len(skills)} skills each sliced ===')
    started = time.time()
    procs = []
    for job_i, (name, slice_skills, logf) in enumerate(jobs):
        cmd = [sys.executable, str(BASE / 'run_feedback_arms.py'),
               '--providers', name,
               '--skills', ','.join(slice_skills),
               '--max-iters', str(args.max_iters),
               '--out-dir', args.out_dir,
               '--max-minutes', str(args.max_minutes)]
        if args.resume:
            cmd.append('--resume')
        if args.skip_logged:
            cmd.append('--skip-logged')
        if args.line_directive:
            cmd.append('--line-directive')
        if args.sweeps:
            cmd += ['--sweeps', str(args.sweeps)]
        logh = open(logf, 'w')
        p = subprocess.Popen(cmd, stdout=logh, stderr=subprocess.STDOUT)
        procs.append((p, name, slice_skills, logf, logh))
        print(f'  [{name}] w{job_i}: {",".join(slice_skills)} -> {logf.name} (pid {p.pid})')

    # wait
    for p, name, slice_skills, logf, logh in procs:
        p.wait()
        logh.close()
    elapsed = time.time() - started

    # aggregate per-provider agentic logs
    print(f'\n=== results ({elapsed:.0f}s wall) ===')
    total_pass = total = 0
    for name in providers:
        log_path = BASE / args.out_dir / f'{name}-agentic' / 'agentic_log.json'
        if not log_path.is_file():
            print(f'  {name:26s} no log')
            continue
        log = json.loads(log_path.read_text())
        p = sum(1 for v in log.values() if v.get('final_pass'))
        total_pass += p
        total += len(log)
        for skill, v in sorted(log.items()):
            mark = 'PASS' if v.get('final_pass') else 'fail'
            print(f'  {name:26s} {skill:14s} {mark:4s} gens={v.get("generations", 0)}')
        print(f'  {name:26s} -> {p}/{len(log)} passed')
    print(f'\nTOTAL: {total_pass}/{total} passed across {len(providers)} providers '
          f'({elapsed:.0f}s wall, {len(jobs)} concurrent jobs)')
    print('worker logs in _parallel_logs/')
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description='Parallel agentic-arms launcher')
    ap.add_argument('--probe', action='store_true',
                    help='ping every requested provider in parallel and print status, then exit')
    ap.add_argument('--providers', default='')
    ap.add_argument('--skills', default='')
    ap.add_argument('--workers', type=int, default=1,
                    help='skill-shard workers per provider (parallel processes)')
    ap.add_argument('--max-iters', type=int, default=4)
    ap.add_argument('--max-minutes', type=float, default=0)
    ap.add_argument('--out-dir', default='model-outputs')
    ap.add_argument('--resume', action='store_true')
    ap.add_argument('--skip-logged', action='store_true',
                    help='skip any skill already in the log (passed or not) — '
                         'use for chunked resume so each run covers fresh skills')
    ap.add_argument('--line-directive', action='store_true')
    ap.add_argument('--sweeps', type=int, default=0)
    args = ap.parse_args()

    load_env()

    sys.path.insert(0, str(BASE))
    import run_feedback_arms as rfa
    providers = rfa.PROVIDERS
    names = [p.strip() for p in args.providers.split(',') if p.strip()]
    if not names:
        names = list(providers.keys())

    if args.probe:
        return probe_all(providers, names)

    args.providers = names
    return run_workers(args)


if __name__ == '__main__':
    raise SystemExit(main())
