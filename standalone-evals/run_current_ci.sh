#!/usr/bin/env bash
# Current-scope gate for the 22 standalone form skills (public monorepo scope;
# persona skills god/smoker/terry-davis/psych/no-bullshit moved to skills-2).
# Historical evals-infra/legacy checks are intentionally separate.
set -u

ROOT="${SKILLS_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
ROOT="$(cd "$ROOT" && pwd)"
HARNESS="${EVALS_INFRA_ROOT:-}"
PYTHON="${PYTHON:-python3}"
passed=0
total=0
failed=0

check() {
  total=$((total + 1))
  name="$1"
  shift
  printf '\n==> %s\n' "$name"
  if "$@"; then
    passed=$((passed + 1))
    printf 'PASS: %s\n' "$name"
  else
    failed=$((failed + 1))
    printf 'FAIL: %s\n' "$name"
  fi
}

check "standalone benchmark contract" \
  "$PYTHON" "$ROOT/standalone-evals/validate_standalone_benchmark.py" --root "$ROOT"

check "standalone Python compilation" \
  "$PYTHON" -m py_compile "$ROOT"/standalone-evals/*.py "$ROOT"/*/scripts/contract_check.py

for skill in choka dodoitsu gogyohka haibun haiku katauta lunes monoku \
  renga sedoka senryu sijo tanka kyoka somonka bussokusekika imayo \
  kanshi zappai waka renshi sonnet
do
  check "skill-local contract: $skill" bash -c "cd \"$ROOT/$skill\" && ./scripts/contract_check.py"
done

check "example syntax smoke" \
  "$PYTHON" "$ROOT/standalone-evals/run_example_smoke.py" --root "$ROOT"

check "one-skill package isolation" \
  "$PYTHON" "$ROOT/standalone-evals/check_skill_isolation.py" --root "$ROOT"

if [ -n "$HARNESS" ] && [ -f "$HARNESS/static_skill_audit.py" ]; then
  check "static skill audit" \
    "$PYTHON" "$HARNESS/static_skill_audit.py" --root "$ROOT" --min-score 0.75
else
  total=$((total + 1))
  failed=$((failed + 1))
  printf '\nFAIL: static skill audit (set EVALS_INFRA_ROOT to the harness directory)\n'
fi

printf '\nCURRENT-SCOPE RESULT: %d/%d mechanical checks passed (%d failed)\n' "$passed" "$total" "$failed"
printf 'NOTE: historical regression suite is not included; run the external harness separately.\n'
if [ "$failed" -eq 0 ]; then
  printf 'CURRENT-SCOPE GATE: 100%% mechanical validation\n'
  printf 'NOTE: blind routing quality and generated-code correctness are separate evaluations.\n'
  exit 0
fi
printf 'CURRENT-SCOPE GATE: NOT 100%% mechanical validation\n'
exit 1
