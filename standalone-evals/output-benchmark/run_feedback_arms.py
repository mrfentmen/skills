#!/usr/bin/env python3
"""
Checker-feedback agentic arms (the agentic ceiling).

For every skill in e3-manifest.json, this runs the documented agentic
workflow mechanically: write -> grade with the mechanical grader -> feed the
failure reasons back to the model -> refine -> repeat.

  * iteration 0 is the existing one-shot with-skill output (same model, same
    day, same prompts) or a fresh call when none exists
  * the judge is grade_output.py itself (run + expected output tokens + form),
    so "passes the loop" means "passes the benchmark"
  * the feedback message contains the grader's exact failure reasons
    (missing/extra output tokens, runtime stderr, form contract violations)

Outputs land in model-outputs/<provider>-agentic/with-skill/<skill>.py and a
run log at model-outputs/<provider>-agentic/agentic_log.json with iterations
and final status per skill, so a quota-limited run is still interpretable.

Usage:
  GROQ_API_KEY=... MISTRAL_API_KEY=... python3 run_feedback_arms.py
  python3 run_feedback_arms.py --providers mistral-small --skills haiku,tanka
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
MANIFEST = json.loads((BASE / 'e3-manifest.json').read_text(encoding='utf-8'))
GRADER = BASE / 'grade_output.py'

PROVIDERS: dict[str, dict] = {
    "groq-llama3.3-70b": {
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "key_env": "GROQ_API_KEY",
        "model": "llama-3.3-70b-versatile",
    },
    "groq-gpt-oss-120b": {
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "key_env": "GROQ_API_KEY",
        "model": "openai/gpt-oss-120b",
    },
    "groq-qwen3.6-27b": {
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "key_env": "GROQ_API_KEY",
        "model": "qwen/qwen3.6-27b",
    },
    "zai-glm-4.7-flash": {
        "url": "https://api.z.ai/api/paas/v4/chat/completions",
        "key_env": "ZAI_API_KEY",
        "model": "glm-4.7-flash",
    },
    "mistral-small": {
        "url": "https://api.mistral.ai/v1/chat/completions",
        "key_env": "MISTRAL_API_KEY",
        "model": "mistral-small-latest",
    },
    "mistral-large": {
        "url": "https://api.mistral.ai/v1/chat/completions",
        "key_env": "MISTRAL_API_KEY",
        "model": "mistral-large-latest",
    },
    "mistral-codestral": {
        "url": "https://api.mistral.ai/v1/chat/completions",
        "key_env": "MISTRAL_API_KEY",
        "model": "codestral-latest",
    },
}

WITH_SKILL_SYSTEM = (
    "You are a coding agent. The following skill specification is ACTIVATED "
    "and must be followed exactly:\n\n{skill_text}\n\n"
    "Follow the skill's form contract, minimum requirements, and boundaries."
)
REFINE_INSTRUCTION = (
    "\n\nYour previous attempt failed the benchmark's checks. The checks are:\n"
    "{feedback}\n\n"
    "Fix the code so it runs, prints exactly the expected result (no extra "
    "numbers), and satisfies every form requirement listed. Output only the "
    "final, complete Python program in a single code block, no explanations."
)


def call_chat(provider: dict, system: str, user: str, max_tokens: int = 1800,
              key: str = '', retries: int = 6, base_wait: int = 20) -> str | None:
    payload = json.dumps({
        "model": provider["model"],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    })
    # round-robin across comma-joined keys so a per-key rate limit does not stall a run
    if 'keys' in provider and provider['keys']:
        auth = provider['keys'][provider.get('_ki', 0) % len(provider['keys'])]
        provider['_ki'] = provider.get('_ki', 0) + 1
    else:
        auth = key or provider['key']
    for attempt in range(retries):
        try:
            proc = subprocess.run(
                ["curl", "-sS", "--max-time", "240", provider["url"],
                 "-H", f"Authorization: Bearer {auth}",
                 "-H", "Content-Type: application/json",
                 "-d", payload],
                capture_output=True, text=True, timeout=260)
        except subprocess.TimeoutExpired:
            print(f"      [{attempt}] timeout", flush=True)
            time.sleep(base_wait)
            continue
        if proc.returncode != 0:
            print(f"      [{attempt}] curl exit {proc.returncode}", flush=True)
            time.sleep(base_wait)
            continue
        try:
            data = json.loads(proc.stdout)
        except json.JSONDecodeError:
            print(f"      [{attempt}] non-JSON reply", flush=True)
            time.sleep(base_wait)
            continue
        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"].strip()
        err = data.get("error", {})
        msg = str(err.get("message", proc.stdout))[:140]
        if ("rate" in msg.lower() or "limit" in msg.lower() or "overload" in msg.lower()
                or "temporar" in msg.lower() or "1305" in str(err.get("code", ""))
                or "429" in str(err.get("code", "")) or "5" == str(err.get("code", ""))[:1]):
            # flat sleep: Groq's per-minute TPM window resets in ~60s, so a flat
            # wait lands the next attempt just after the window refills; Z.ai's
            # 1305 overload errors also clear in tens of seconds
            wait = base_wait
            print(f"      [{attempt}] rate-limited ({msg[:60]}); sleeping {wait}s", flush=True)
            time.sleep(min(wait, 240))
            continue
        print(f"      provider error: {msg}", flush=True)
        return None
    return None


def extract_code(text: str) -> str:
    blocks = re.findall(r"```(?:python|py)?\s*\n(.*?)```", text, re.DOTALL)
    if blocks:
        text = blocks[-1]
    # reasoning models (qwen3.6) emit <think>...</think> blocks that are not valid
    # Python; drop them and any prose before the first statement
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return text.strip()


def generate(provider: dict, system: str, user: str, key: str = '',
             retries: int = 6, base_wait: int = 20) -> str | None:
    """Call the model and return the extracted code, or None on failure."""
    raw = call_chat(provider, system, user, key=key, retries=retries, base_wait=base_wait)
    if raw is None:
        return None
    code = extract_code(raw)
    return code if code.strip() else None


def grade_skill(skill: str, workdir: Path) -> tuple[bool, str]:
    """Grade one skill's file in workdir via the real grader. Returns (passed, detail)."""
    proc = subprocess.run([sys.executable, str(GRADER), '--dir', str(workdir)],
                          capture_output=True, text=True, timeout=300)
    for line in proc.stdout.splitlines():
        if line.startswith(f'{skill} '):
            ok = ' run=True out=True form=True' in line
            detail = line.split('|', 1)[1].strip() if '|' in line else ''
            # trim repeated form messages
            return ok, re.sub(r"(\[.*?\])( \1)+", r"\1", detail)[:900]
    return False, 'grader produced no row for this skill'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--providers', default='groq-llama3.3-70b,mistral-small')
    parser.add_argument('--skills', default='')
    parser.add_argument('--max-iters', type=int, default=4,
                        help='total generations per skill including the starting one')
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--skip-logged', action='store_true',
                        help='skip any skill already present in the log (passed or not); '
                             'for wall-clock chunked runs so completed attempts are not re-done')
    parser.add_argument('--sweeps', type=int, default=0,
                        help='re-attempt quota-limited skills this many extra passes (helps rolling TPD windows)')
    parser.add_argument('--out-dir', default='model-outputs',
                        help='output base under output-benchmark/ (default model-outputs; '
                             'use a fresh name to preserve prior agentic evidence)')
    parser.add_argument('--max-minutes', type=float, default=0,
                        help='optional wall-clock budget; 0 = unlimited')
    args = parser.parse_args()
    t_start = time.time()

    def budget_left() -> bool:
        return args.max_minutes <= 0 or (time.time() - t_start) < args.max_minutes * 60

    providers = [p.strip() for p in args.providers.split(',') if p.strip()]
    wanted = {s.strip() for s in args.skills.split(',') if s.strip()}
    items = [i for i in MANIFEST['items'] if not wanted or i['skill'] in wanted]

    for name in providers:
        prov = PROVIDERS.get(name)
        if not prov:
            print(f'unknown provider {name!r}; skipping')
            continue
        keys = os_keys(prov['key_env'])
        if not keys:
            print(f'provider {name}: no env {prov["key_env"]}; skipping')
            continue
        prov = dict(prov, key=keys[0], keys=keys, _ki=0)
        out_dir = BASE / args.out_dir / f'{name}-agentic' / 'with-skill'
        work_dir = BASE / f'.agentic-work-{name}'
        work_dir.mkdir(parents=True, exist_ok=True)
        out_dir.mkdir(parents=True, exist_ok=True)
        log_path = BASE / args.out_dir / f'{name}-agentic' / 'agentic_log.json'
        log = json.loads(log_path.read_text()) if log_path.is_file() else {}
        print(f'\n=== agentic {name} ({prov["model"]}) — {len(items)} skills, max {args.max_iters} gens ===')

        quota_limited: list[str] = []
        for idx, item in enumerate(items, 1):
            skill = item['skill']
            entry = log.get(skill)
            if args.skip_logged and entry:
                print(f'  {skill:12s} already in log (skip-logged)', flush=True)
                continue
            if args.resume and entry and entry.get('final_pass'):
                print(f'  {skill:12s} already passed in log', flush=True)
                continue
            final_file = out_dir / f'{skill}.py'
            skill_dir = work_dir / skill
            skill_dir.mkdir(parents=True, exist_ok=True)
            start_base = BASE / (args.out_dir if args.out_dir != 'model-outputs' else 'model-outputs')
            start_file = start_base / name / 'with-skill' / f'{skill}.py'
            cur = None
            if start_file.is_file() and start_file.read_text(encoding='utf-8').strip() != '# MODEL CALL FAILED':
                cur = start_file.read_text(encoding='utf-8')
                gens = 1
            elif final_file.is_file() and args.resume:
                cur = final_file.read_text(encoding='utf-8')
                gens = 1
            else:
                gens = 0
            skill_file = ROOT / skill / 'SKILL.md'
            system = WITH_SKILL_SYSTEM.format(skill_text=skill_file.read_text(encoding='utf-8'))
            task = USER_TASK.format(task=item['task'])

            passed = False
            attempts = []
            while gens <= args.max_iters and budget_left():
                if cur is None:
                    print(f'  [{idx}/{len(items)}] {skill:12s} gen {gens + 1}/{args.max_iters} ...', flush=True)
                    cur = generate(prov, system, task)
                    gens += 1
                    if cur is None:
                        break
                (skill_dir / f'{skill}.py').write_text(cur)
                ok, detail = grade_skill(skill, skill_dir)
                attempts.append({'gen': gens, 'passed': ok, 'detail': detail[:300]})
                print(f'  [{idx}/{len(items)}] {skill:12s} gen {gens}: {"PASS" if ok else "fail"}', flush=True)
                if ok or gens >= args.max_iters:
                    passed = ok
                    break
                feedback = detail or 'the code did not pass'
                print(f'    refining: {feedback[:140]}', flush=True)
                cur = generate(prov, system, task + REFINE_INSTRUCTION.format(feedback=feedback))
                gens += 1
                if cur is None:
                    break
            if cur is not None:
                final_file.write_text(cur)
                print(f'  {skill:12s} final: {"PASS" if passed else "FAIL (budget spent)"} after {min(gens, args.max_iters)} gens', flush=True)
            else:
                final_file.write_text('# MODEL CALL FAILED\n')
                print(f'  {skill:12s} final: QUOTA-LIMITED', flush=True)
            if cur is None:
                quota_limited.append(skill)
            log[skill] = {'final_pass': passed, 'generations': min(gens, args.max_iters),
                          'attempts': attempts, 'ts': time.strftime('%Y-%m-%d %H:%M:%S')}
            log_path.write_text(json.dumps(log, indent=1))
            time.sleep(3)
            if not budget_left():
                print('--- wall-clock budget exhausted; run --resume to continue ---', flush=True)
                break

        # sweeps: keep re-attempting quota-limited skills while the window frees tokens
        for sweep in range(args.sweeps):
            if not quota_limited or not budget_left():
                break
            print(f'\n--- sweep {sweep + 1}/{args.sweeps}: {len(quota_limited)} quota-limited skills ---', flush=True)
            still = []
            for skill in quota_limited:
                if not budget_left():
                    still.append(skill)
                    continue
                item = next(i for i in items if i['skill'] == skill)
                skill_file = ROOT / skill / 'SKILL.md'
                system = WITH_SKILL_SYSTEM.format(skill_text=skill_file.read_text(encoding='utf-8'))
                task = USER_TASK.format(task=item['task'])
                final_file = out_dir / f'{skill}.py'
                skill_dir = work_dir / skill
                skill_dir.mkdir(parents=True, exist_ok=True)
                gens = 0
                cur = None
                passed = False
                attempts = []
                print(f'  sweep {sweep + 1}: {skill:12s} fresh attempt ...', flush=True)
                while gens < args.max_iters and budget_left():
                    if cur is None:
                        cur = generate(prov, system, task, retries=6, base_wait=45)
                        gens += 1
                        if cur is None:
                            break
                    (skill_dir / f'{skill}.py').write_text(cur)
                    ok, detail = grade_skill(skill, skill_dir)
                    attempts.append({'gen': gens, 'passed': ok, 'detail': detail[:300]})
                    print(f'    sweep gen {gens}: {"PASS" if ok else "fail"}', flush=True)
                    if ok or gens >= args.max_iters:
                        passed = ok
                        break
                    cur = generate(prov, system, task + REFINE_INSTRUCTION.format(feedback=detail),
                                   retries=6, base_wait=45)
                    gens += 1
                    if cur is None:
                        break
                if cur is not None:
                    final_file.write_text(cur)
                    print(f'  sweep {sweep + 1}: {skill:12s} {"PASS" if passed else "budget spent"}', flush=True)
                    if passed:
                        log[skill]['final_pass'] = True
                        log[skill]['ts'] = time.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    still.append(skill)
                log[skill]['attempts'] = attempts
                log_path.write_text(json.dumps(log, indent=1))
            quota_limited = still

        passes = sum(1 for v in log.values() if v.get('final_pass'))
        print(f'\nagentic {name}: {passes}/{len(items)} passed (from {log_path})')
    return 0


def os_keys(env: str) -> list[str]:
    import os
    v = os.environ.get(env, '')
    return [k.strip() for k in v.split(',') if k.strip()]


USER_TASK = (
    "{task}\n\n"
    "Write a complete, self-contained Python program that solves this exactly as "
    "asked. Read input from stdin as described. Output only the Python code in a "
    "single code block, no explanations."
)


if __name__ == '__main__':
    raise SystemExit(main())
