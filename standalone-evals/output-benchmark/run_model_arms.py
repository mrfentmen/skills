#!/usr/bin/env python3
"""
Run the E3 output benchmark with real models (genuinely independent arms).

For every skill in e3-manifest.json this script calls a chat-completions API
twice:

  * with-skill    - system prompt = the skill's full SKILL.md (activated)
  * without-skill - system prompt = plain coding agent (control)

The model output is saved as model-outputs/<provider>/<arm>/<skill>.py so it
can be graded with grade_output.py.  Keys are read from environment variables
(GROQ_API_KEY, MISTRAL_API_KEY, ...) and never stored in this file.

Usage:
  GROQ_API_KEY=... MISTRAL_API_KEY=... \
    python3 run_model_arms.py --providers groq-llama3.3-70b,mistral-small
  python3 run_model_arms.py --providers groq-llama3.3-70b --skills haiku,tanka
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
MANIFEST = json.loads((BASE / "e3-manifest.json").read_text(encoding="utf-8"))

PROVIDERS: dict[str, dict] = {
    "groq-llama3.3-70b": {
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "key_env": "GROQ_API_KEY",
        "model": "llama-3.3-70b-versatile",
    },
    "mistral-small": {
        "url": "https://api.mistral.ai/v1/chat/completions",
        "key_env": "MISTRAL_API_KEY",
        "model": "mistral-small-latest",
    },
    "cerebras-llama3.3-70b": {
        "url": "https://api.cerebras.ai/v1/chat/completions",
        "key_env": "CEREBRAS_API_KEY",
        "model": "llama-3.3-70b",
    },
    "xai-grok-4.5": {
        "url": "https://api.x.ai/v1/chat/completions",
        "key_env": "XAI_API_KEY",
        "model": "grok-4.5",
    },
}

WITH_SKILL_SYSTEM = (
    "You are a coding agent. The following skill specification is ACTIVATED "
    "and must be followed exactly:\n\n{skill_text}\n\n"
    "Follow the skill's form contract, minimum requirements, and boundaries."
)
WITHOUT_SKILL_SYSTEM = "You are a coding agent that writes working Python programs."
USER_TASK = (
    "{task}\n\n"
    "Write a complete, self-contained Python program that solves this exactly as "
    "asked. Read input from stdin as described. Output only the Python code in a "
    "single code block, no explanations."
)


def call_chat(provider: dict, system: str, user: str, max_tokens: int = 1800,
              retries: int = 4) -> str | None:
    payload = json.dumps({
        "model": provider["model"],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    })
    for attempt in range(retries):
        cmd = [
            "curl", "-sS", "--max-time", "180", provider["url"],
            "-H", f"Authorization: Bearer {provider['key']}",
            "-H", "Content-Type: application/json",
            "-d", payload,
        ]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=200)
        except subprocess.TimeoutExpired:
            print("    timeout; retrying")
            time.sleep(8)
            continue
        if proc.returncode != 0:
            print(f"    curl exit {proc.returncode}; retrying")
            time.sleep(8)
            continue
        try:
            data = json.loads(proc.stdout)
        except json.JSONDecodeError:
            print(f"    non-JSON reply; retrying ({proc.stdout[:80]!r})")
            time.sleep(8)
            continue
        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"].strip()
        err = data.get("error", {})
        msg = str(err.get("message", proc.stdout))[:160]
        code = str(err.get("code", ""))
        if "429" in code or "rate" in msg.lower() or "limit" in msg.lower():
            wait = 12 * (attempt + 1)
            print(f"    rate-limited; sleeping {wait}s")
            time.sleep(wait)
            continue
        print(f"    provider error: {msg}")
        return None
    return None


def extract_code(text: str) -> str:
    blocks = re.findall(r"```(?:python|py)?\s*\n(.*?)```", text, re.DOTALL)
    if blocks:
        return blocks[-1].strip()
    return text.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--providers", default="groq-llama3.3-70b,mistral-small")
    parser.add_argument("--skills", default="")
    parser.add_argument("--sleep", type=float, default=2.5)
    parser.add_argument("--resume", action="store_true",
                        help="skip arms whose output already exists")
    args = parser.parse_args()

    providers = [p.strip() for p in args.providers.split(",") if p.strip()]
    wanted = {s.strip() for s in args.skills.split(",") if s.strip()}
    items = [i for i in MANIFEST["items"] if not wanted or i["skill"] in wanted]
    if not items:
        print("no manifest items selected")
        return 1

    for name in providers:
        prov = PROVIDERS.get(name)
        if not prov:
            print(f"unknown provider {name!r}; skipping")
            continue
        key = os.environ.get(prov["key_env"], "")
        if not key:
            print(f"provider {name}: missing env {prov['key_env']}; skipping")
            continue
        prov = dict(prov, key=key)
        print(f"\n=== provider {name} ({prov['model']}) — {len(items)} skills x 2 arms ===")
        failures = 0
        for item in items:
            skill = item["skill"]
            skill_file = ROOT / skill / "SKILL.md"
            for arm, system in (
                ("with-skill",
                 WITH_SKILL_SYSTEM.format(skill_text=skill_file.read_text(encoding="utf-8"))
                 if skill_file.is_file() else "You are a coding agent."),
                ("without-skill", WITHOUT_SKILL_SYSTEM),
            ):
                out_dir = BASE / "model-outputs" / name / arm
                out_dir.mkdir(parents=True, exist_ok=True)
                out_file = out_dir / f"{skill}.py"
                if args.resume and out_file.is_file() \
                        and out_file.read_text(encoding="utf-8").strip() != "# MODEL CALL FAILED":
                    print(f"  {skill:12s} {arm:14s} cached", flush=True)
                    continue
                print(f"  {skill:12s} {arm:14s} ...", flush=True)
                content = call_chat(prov, system, USER_TASK.format(task=item["task"]))
                if content is None:
                    failures += 1
                    out_file.write_text("# MODEL CALL FAILED\n")
                    continue
                out_file.write_text(extract_code(content) + "\n")
                time.sleep(args.sleep)
        print(f"provider {name}: {len(items) * 2 - failures}/{len(items) * 2} calls succeeded")

    print("\nNow grade the arms from the output-benchmark directory:")
    for name in providers:
        print(f"  python3 grade_output.py --dir model-outputs/{name}/with-skill")
        print(f"  python3 grade_output.py --dir model-outputs/{name}/without-skill")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
