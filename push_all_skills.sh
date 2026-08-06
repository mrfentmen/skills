#!/bin/bash
# Create one PUBLIC GitHub repo per skill and push that skill's contents.
# Also distributes the CI assets into every repo: the Audit & Package GitHub
# Action workflow (.github/workflows/) plus the scripts it runs
# (.github/scripts/), so every push to any skill repo re-runs the static
# audit and repackages the .skill.
# Usage:  GITHUB_TOKEN=<pat> bash push_all_skills.sh
# The token is read from the environment only, never written to any file.
# The skill list is derived from the filesystem (every dir under SRC that
# contains a SKILL.md), so moving skill folders in or out of the monorepo
# automatically changes what gets pushed - no hardcoded list to keep in
# sync. Re-running on EXISTING repos is the deploy path for CI: the
# create-API returns "name already exists" (handled, not fatal) and the
# push then syncs the new .github/ files into each repo.
set -u
TOKEN="${GITHUB_TOKEN:?set GITHUB_TOKEN first}"
export GIT_TERMINAL_PROMPT=0   # never hang on a credential prompt; fail fast instead
USER="mrfentmen"
SRC="${SKILLS_ROOT:-/Users/del/Desktop/skills}"
HARNESS="${EVALS_INFRA_ROOT:-/Users/del/Desktop/skills 3 /evals-infra}"
export EVALS_INFRA_ROOT="$HARNESS"
[ -d "$SRC" ] || { echo "missing skills root: $SRC" >&2; exit 1; }
[ -d "$HARNESS" ] || { echo "missing evals harness: $HARNESS" >&2; exit 1; }
# Filesystem-derived skill list: any directory directly under SRC that has
# a SKILL.md. Skips workspaces, dist/, shared/, ci/, evals-infra, etc.
SKILLS=$(cd "$SRC" && for d in */; do
  [ -f "${d%/}/SKILL.md" ] && printf '%s ' "${d%/}"
done)

ok=0; fail=0; failed_list=()
for skill in $SKILLS; do
  echo "=== $skill ==="
  created=$(curl -s -X POST -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github+json" \
    "https://api.github.com/user/repos" \
    -d "{\"name\":\"$skill\",\"private\":false,\"description\":\"AI coding skill: $skill\"}")
  # keep the description current on EXISTING repos too (the create call above
  # fails for them, so PATCH separately; idempotent on every deploy)
  curl -s -X PATCH -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github+json" \
    "https://api.github.com/repos/$USER/$skill" \
    -d "{\"description\":\"AI coding skill: $skill\"}" >/dev/null
  repo_ok=$(echo "$created" | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
except Exception:
    print('BADJSON'); sys.exit()
if 'full_name' in d: print('created')
elif 'errors' in d: print('ERR: ' + str(d['errors'][0].get('message', '?')))
else: print('MSG: ' + str(d.get('message', '?')))")
  echo "  repo: $repo_ok"

  W="/tmp/skill-repo-$skill"
  rm -rf "$W"; mkdir -p "$W"
  cp -R "$SRC/$skill"/. "$W/" 2>/dev/null
  [ -f "$SRC/dist/$skill.skill" ] && cp "$SRC/dist/$skill.skill" "$W/"
  cp -R "$SRC/shared" "$W/shared" 2>/dev/null

  # CI assets: the Audit & Package workflow + the scripts it runs. Single
  # source of truth lives in the monorepo; each repo gets a snapshot copy.
  mkdir -p "$W/.github/workflows" "$W/.github/scripts"
  cp "$SRC/ci/audit-and-package.yml" "$W/.github/workflows/audit-and-package.yml"
  cp "$HARNESS/static_skill_audit.py" "$W/.github/scripts/"
  cp "$SRC/package_skills.py" "$W/.github/scripts/"

  # repo README: generated per-skill (description + usage prompt + style
  # sample from SKILL.md) by ci/generate_repo_readme.py
  python3 "$SRC/ci/generate_repo_readme.py" "$SRC/$skill" "$W/README.md" \
    || { echo "  FAIL: README generation"; fail=$((fail+1)); failed_list+=("$skill"); continue; }

  printf '__pycache__/\n*.pyc\n.DS_Store\n' > "$W/.gitignore"

  cd "$W" || { echo "  FAIL: cd"; fail=$((fail+1)); failed_list+=("$skill"); continue; }
  git init -q && git symbolic-ref HEAD refs/heads/main || { echo "  FAIL: git init"; fail=$((fail+1)); failed_list+=("$skill"); continue; }
  git -c user.name="$USER" -c user.email="$USER@users.noreply.github.com" add -A >/dev/null 2>&1
  if ! git -c user.name="$USER" -c user.email="$USER@users.noreply.github.com" commit -q -m "Add $skill skill"; then
    echo "  FAIL: commit (nothing to commit?)"; fail=$((fail+1)); failed_list+=("$skill"); continue
  fi
  # CI may have auto-committed refreshed artifacts since the last sync, and
  # the repo README is regenerated per push, so rebase local work on top of
  # the remote before pushing. `-X theirs` keeps the LOCAL version of any
  # file changed on BOTH sides (the monorepo is the source of truth, a
  # manual remote edit to a file that also changed locally gets overwritten;
  # CI-only artifacts like SKILL_AUDIT.json/dist are untouched by the local
  # commit, so they never conflict and always survive).
  # The `|| true` is INTENTIONAL: the first push has no remote branch yet
  # (pull fails, ignored) and any real conflict now resolves via -X theirs.
  git -c credential.helper= pull --rebase -X theirs -q \
    "https://x-access-token:$TOKEN@github.com/$USER/$skill.git" main 2>/dev/null || true
  PUSH_OUT=$(git -c credential.helper= push -q "https://x-access-token:$TOKEN@github.com/$USER/$skill.git" main 2>&1)
  if [ $? -eq 0 ]; then
    echo "  pushed: ok"; ok=$((ok+1))
  else
    echo "  pushed: FAIL ($PUSH_OUT)"; fail=$((fail+1)); failed_list+=("$skill")
  fi
  rm -rf "$W"
done
echo
echo "=== DONE: $ok pushed, $fail failed ==="
[ $fail -gt 0 ] && printf 'failed: %s\n' "${failed_list[@]}"
