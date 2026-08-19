#!/usr/bin/env python3
"""Second independent blind routing scorer.

Scores every prompt in a blind sheet (id + prompt, gold omitted) with an LLM
router. The router sees ONLY the sheet's skill descriptions and prompts —
never the private benchmark. Decisions are written as the standard
{id: label} object for score_blind_decisions.py.

Usage:
  MISTRAL_API_KEY=... python3 run_second_blind_scorer.py \
      --sheet standalone-evals/blind_sheet_v2.json \
      --output /tmp/standalone-trigger-v1-decisions-model.json \
      [--workers 6] [--resume]
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
URL = "https://api.mistral.ai/v1/chat/completions"
MODEL = "mistral-small-latest"

ROUTER_SYSTEM = (
    "You are a skill router. Below is a list of available skills, each with a "
    "short description. For a given user prompt, choose the single skill that "
    "should activate, or choose \"none\" when no skill fits (ordinary coding, "
    "generic requests, or requests that only resemble a skill's surface "
    "without its core contract). Respond with exactly one word: the skill name "
    "or \"none\". No explanations.\n\n"
    "Available skills:\n{skill_list}"
)


def os_keys(env: str) -> list[str]:
    v = os.environ.get(env, "")
    return [k.strip() for k in v.split(",") if k.strip()]


def call_router(keys: list[str], system: str, prompt: str,
                retries: int = 5, base_wait: int = 8) -> str | None:
    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.0,
        "max_tokens": 16,
    })
    for attempt in range(retries):
        key = keys[(attempt + random.randrange(len(keys))) % len(keys)]
        proc = subprocess.run(
            ["curl", "-sS", "--max-time", "60", URL,
             "-H", f"Authorization: Bearer {key}",
             "-H", "Content-Type: application/json",
             "-d", payload],
            capture_output=True, text=True, timeout=70)
        if proc.returncode != 0:
            time.sleep(base_wait)
            continue
        try:
            data = json.loads(proc.stdout)
        except json.JSONDecodeError:
            time.sleep(base_wait)
            continue
        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"].strip()
        time.sleep(base_wait)
    return None


def normalize(raw: str) -> str:
    raw = raw.strip().lower().strip('"').strip("'").strip(".")
    raw = re.sub(r"[^a-z-]", "", raw)
    return raw


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sheet", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    keys = os_keys("MISTRAL_API_KEY")
    if not keys:
        print("FAIL: MISTRAL_API_KEY not set")
        return 1

    sheet = json.loads(args.sheet.read_text(encoding="utf-8"))
    skills = sheet["skills"]
    records = sheet["records"]
    print(f"sheet: {len(records)} prompts, {len(skills)} skills")

    valid_names = {s["name"] for s in skills} | {"none"}
    skill_list = "\n".join(f"- {s['name']}: {s['description']}" for s in skills)
    system = ROUTER_SYSTEM.format(skill_list=skill_list)

    decisions: dict[str, str] = {}
    if args.resume and args.output.is_file():
        decisions = json.loads(args.output.read_text(encoding="utf-8"))
        print(f"resuming: {len(decisions)} decisions already recorded")

    remaining = [r for r in records if r["id"] not in decisions]
    print(f"to score: {len(remaining)}")

    def score_one(record: dict) -> tuple[str, str]:
        raw = call_router(keys, system, record["prompt"])
        label = normalize(raw) if raw else "none"
        if label not in valid_names:
            label = "none"
        return record["id"], label

    t0 = time.time()
    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(score_one, r): r["id"] for r in remaining}
        for fut in as_completed(futures):
            record_id, label = fut.result()
            decisions[record_id] = label
            done += 1
            if done % 25 == 0:
                args.output.write_text(json.dumps(decisions, indent=1) + "\n", encoding="utf-8")
                elapsed = time.time() - t0
                print(f"  {done}/{len(remaining)} ({elapsed:.0f}s)", flush=True)

    args.output.write_text(json.dumps(decisions, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {len(decisions)} decisions to {args.output} ({time.time() - t0:.0f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
