#!/usr/bin/env bash
# Self-contained historical-style gate for the current 28-skill release scope.
# The external legacy runner remains a frozen comparison artifact and is not
# invoked here because it targets a different 18-skill repository snapshot.
set -u

ROOT="${SKILLS_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
if ! ROOT="$(cd "$ROOT" 2>/dev/null && pwd)"; then
  printf 'CURRENT-HISTORICAL GATE: RED\nFAIL: invalid skill root: %s\n' "$ROOT"
  exit 1
fi
PYTHON="${PYTHON:-python3}"
if ! command -v "$PYTHON" >/dev/null 2>&1; then
  printf 'CURRENT-HISTORICAL GATE: RED\nFAIL: Python interpreter not found: %s\n' "$PYTHON"
  exit 1
fi
if ! command -v pgrep >/dev/null 2>&1; then
  printf 'CURRENT-HISTORICAL GATE: RED\nFAIL: pgrep is required for safe child-process cleanup\n'
  exit 1
fi
TIMEOUT_SECONDS="${CURRENT_HISTORICAL_TIMEOUT_SECONDS:-300}"
case "$TIMEOUT_SECONDS" in
  ''|*[!0-9]*)
    printf 'CURRENT-HISTORICAL GATE: RED\nFAIL: timeout must be a non-negative integer: %s\n' "$TIMEOUT_SECONDS"
    exit 1
    ;;
esac

timeout_child=""

child_descendants() {
  parent="$1"
  if command -v pgrep >/dev/null 2>&1; then
    pgrep -P "$parent" 2>/dev/null || true
  fi
}

kill_tree() {
  parent="$1"
  for descendant in $(child_descendants "$parent"); do
    kill_tree "$descendant"
  done
  kill -TERM "$parent" 2>/dev/null || true
}

cleanup_timeout_child() {
  if [ -n "$timeout_child" ] && kill -0 "$timeout_child" 2>/dev/null; then
    kill_tree "$timeout_child"
  fi
}

handle_interrupt() {
  signal="$1"
  cleanup_timeout_child
  timeout_child=""
  case "$signal" in
    INT) exit 130 ;;
    TERM) exit 143 ;;
    HUP) exit 129 ;;
  esac
}
trap 'handle_interrupt INT' INT
trap 'handle_interrupt TERM' TERM
trap 'handle_interrupt HUP' HUP

run_with_timeout() {
  limit="$1"
  shift
  "$@" &
  timeout_child=$!
  started="$(date +%s)"
  while kill -0 "$timeout_child" 2>/dev/null; do
    now="$(date +%s)"
    if [ "$limit" -gt 0 ] && [ $((now - started)) -ge "$limit" ]; then
      kill_tree "$timeout_child"
      sleep 1
      kill_tree "$timeout_child"
      wait "$timeout_child" 2>/dev/null || true
      printf 'timed out after %ss: %s\n' "$limit" "$*" >&2
      timeout_child=""
      return 124
    fi
    sleep 1
  done
  wait "$timeout_child"
  status=$?
  timeout_child=""
  return "$status"
}

passed=0
total=0
failed=0

check() {
  total=$((total + 1))
  name="$1"
  shift
  printf '\n==> %s\n' "$name"
  if run_with_timeout "$TIMEOUT_SECONDS" "$@"; then
    passed=$((passed + 1))
    printf 'PASS: %s\n' "$name"
  else
    failed=$((failed + 1))
    printf 'FAIL: %s\n' "$name"
  fi
}

check "current trigger and held-out contracts" \
  "$PYTHON" "$ROOT/standalone-evals/check_current_scope_regressions.py" --root "$ROOT"

check "current example rhythm gate" \
  "$PYTHON" "$ROOT/standalone-evals/check_rhythm_examples.py"

check "current example syntax smoke" \
  "$PYTHON" "$ROOT/standalone-evals/run_example_smoke.py" --root "$ROOT"

check "current one-skill package isolation" \
  "$PYTHON" "$ROOT/standalone-evals/check_skill_isolation.py" --root "$ROOT"

check "current static skill audit" \
  "$PYTHON" "$ROOT/standalone-evals/static_skill_audit.py" --root "$ROOT" --min-score 0.75

check "current Python compilation" \
  "$PYTHON" -m py_compile "$ROOT"/standalone-evals/*.py "$ROOT"/*/scripts/*.py

check "current source whitespace" git -C "$ROOT" diff --check

printf '\nCURRENT-HISTORICAL RESULT: %d/%d gates passed (%d failed)\n' "$passed" "$total" "$failed"
printf 'SCOPE: versioned 28-skill current tree; frozen external legacy artifacts are reported separately.\n'
if [ "$failed" -eq 0 ]; then
  printf 'CURRENT-HISTORICAL GATE: GREEN\n'
  exit 0
fi
printf 'CURRENT-HISTORICAL GATE: RED\n'
exit 1
