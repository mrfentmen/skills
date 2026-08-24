#!/bin/bash
# Poll OpenRouter free-tier models until a real-generation-sized probe succeeds,
# then fire the agentic arm on etheree immediately. Mirrors catch_zai_window.sh:
# waits silently (probes consume the short window), then lets the runner's own
# retry logic ride the window. north-mini-code is preferred because it is the
# model that closed villanelle by copying the fixed documented example verbatim.
#
# Usage (from standalone-evals/output-benchmark/):
#   bash catch_or_window.sh [skills] [max-minutes]
set -a
source ../../.env.benchmark
SKILLS="${1:-etheree}"
MAXMIN="${2:-7}"
KEY=$(echo "$OPENROUTER_API_KEY" | tr ',' '\n' | head -1)
for i in $(seq 1 120); do
  code=$(curl -s -o /tmp/or_window_probe.json -w "%{http_code}" -m 20 \
    https://openrouter.ai/api/v1/chat/completions \
    -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
    -d '{"model":"cohere/north-mini-code:free","messages":[{"role":"user","content":"write the word ok"}],"max_tokens":60}')
  if [ "$code" = "200" ]; then
    echo "$(date +%H:%M:%S) window open — firing north-mini-code arm on $SKILLS"
    python3 run_feedback_arms.py --providers or-north-mini-code \
      --skills "$SKILLS" --max-iters 5 --sweeps 3 --max-minutes "$MAXMIN" \
      --out-dir model-outputs-or-north-mini-code
    exit 0
  fi
  sleep 20
done
echo "no OpenRouter window in $(($i * 20))s"
