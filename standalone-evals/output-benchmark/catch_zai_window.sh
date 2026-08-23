#!/bin/bash
# Poll Z.ai free-tier until a real-generation-sized probe succeeds, then run
# the agentic arm on the open forms immediately (the window is short-lived:
# probes themselves consume quota, so this waits silently and only calls the
# API once it is ready, then lets the runner's own retry logic ride the window).
#
# Usage (from standalone-evals/output-benchmark/):
#   bash catch_zai_window.sh [skills] [max-minutes]
set -a
source ../../.env.benchmark
SKILLS="${1:-etheree,villanelle}"
MAXMIN="${2:-7}"
KEY=$(echo "$ZAI_API_KEY" | tr ',' '\n' | head -1)
for i in $(seq 1 120); do
  code=$(curl -s -o /tmp/zai_window_probe.json -w "%{http_code}" -m 20 \
    https://api.z.ai/api/paas/v4/chat/completions \
    -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
    -d '{"model":"glm-4.7-flash","messages":[{"role":"user","content":"write the word ok"}],"max_tokens":60}')
  if [ "$code" = "200" ]; then
    echo "$(date +%H:%M:%S) window open — firing arm on $SKILLS"
    python3 run_feedback_arms.py --providers zai-glm-4.7-flash \
      --skills "$SKILLS" --max-iters 5 --sweeps 3 --max-minutes "$MAXMIN" \
      --out-dir model-outputs-zai-glm47
    exit 0
  fi
  sleep 20
done
echo "no window in $(($i * 20))s"