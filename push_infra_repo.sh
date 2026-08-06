#!/bin/bash
# Create/update mrfentmen/skills-infra: the shared helpers + eval harness
# behind the 29 skill repos, in their own repo.
#
# Contents staged:
#   shared/                        - helper modules (ASCII canvas, box drawing, RNG)
#   evals-infra/                   - the full eval harness (+ legacy history)
#   package_skills.py              - .skill packager (layout-aware)
#   ci/audit-and-package.yml       - the per-skill-repo CI template
#   README.md.gitignore          - generated here
#
# Excluded: __pycache__, *.pyc.DS_Store, dist/, workspaces/, generated
# reports (SKILL_AUDIT.json, ALL_SKILLS_*.html/md).
#
# Usage:  GITHUB_TOKEN=<pat> bash push_infra_repo.sh
# The token is read from the environment only, never written to any file.
# Re-running updates the repo (create-API "already exists" is handled, then
# pull --rebase + push syncs new/changed files).
set -eu
TOKEN="${GITHUB_TOKEN:?set GITHUB_TOKEN first}"
export GIT_TERMINAL_PROMPT=0   # never hang on a credential prompt; fail fast
USER="mrfentmen"
REPO="skills-infra"
SRC="${SKILLS_ROOT:-/Users/del/Desktop/skills}"
HARNESS="${EVALS_INFRA_ROOT:-/Users/del/Desktop/skills 3 /evals-infra}"
export EVALS_INFRA_ROOT="$HARNESS"
[ -d "$SRC" ] || { echo "missing skills root: $SRC" >&2; exit 1; }
[ -d "$HARNESS" ] || { echo "missing evals harness: $HARNESS" >&2; exit 1; }
W="/tmp/$REPO-repo"

echo "=== creating/updating $USER/$REPO ==="
created=$(curl -s -X POST -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/user/repos" \
  -d "{\"name\":\"$REPO\",\"private\":true,\"description\":\"Shared helpers + eval harness behind mrfentmen's skills\"}") \
  || { echo "FAIL: GitHub API unreachable (curl exit $?)"; exit 1; }
echo "$created" | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
except Exception:
    print('BADJSON from create API'); sys.exit(2)
if 'full_name' in d: print('created: ' + d['full_name'])
elif 'errors' in d: print('exists/err: ' + str(d['errors'][0].get('message', '?')))
else:
    print('API error: ' + str(d.get('message', '?')))
    sys.exit(2)" || { echo 'FAIL: aborting (check the token)'; exit 1; }
# keep the description current on EXISTING repos too (the create call above
# fails for them, so PATCH separately; idempotent on every deploy)
curl -s -X PATCH -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/$USER/$REPO" \
  -d "{\"description\":\"Shared helpers + eval harness behind mrfentmen's skills\"}" >/dev/null

rm -rf "$W"; mkdir -p "$W"

# stage contents (rsync excludes caches; everything else in evals-infra goes,
# including legacy history)
rsync -a --exclude='__pycache__' --exclude='*.pyc' --exclude='.DS_Store' \
  "$SRC/shared/" "$W/shared/"
rsync -a --exclude='__pycache__' --exclude='*.pyc' --exclude='.DS_Store' \
  "$HARNESS/" "$W/evals-infra/"
cp "$SRC/package_skills.py" "$W/"
mkdir -p "$W/ci"
cp "$SRC/ci/audit-and-package.yml" "$W/ci/audit-and-package.yml"
cp "$SRC/ci/generate_repo_readme.py" "$W/ci/"

cat > "$W/README.md" <<'EOF'
# skills-infra

The shared helpers and evaluation harness behind the themed
skills (`mrfentmen/<skill>`). Kept separate so the skill repos stay lean.

## Layout

- `shared/`, helper modules the skills reference: `ascii_canvas.py`
  (ASCII canvas, lines/circles/ink-density), `box_drawing.py` (box headers),
  `rng.py` (seeded RNG + distributions)
- `evals-infra/`, the eval harness (see `evals-infra/HOW_TO_RUN_EVALS.md`):
  scaffold → grade → check-runnability → aggregate → viewer, plus the static
  skill audit, trigger-overlap check, and the real (model-scored) trigger eval
- `package_skills.py`, layout-aware `.skill` packager: monorepo mode
  (`skills/`) and single-skill mode (per-skill repo root)
- `ci/audit-and-package.yml`, the GitHub Actions template deployed to every
  per-skill repo: static audit (quality gate) → repackage → auto-commit back

## How the skill repos use this

`push_all_skills.sh` (in the skills monorepo) copies `shared/` into each skill
repo and snapshots `package_skills.py` + `static_skill_audit.py` into
`.github/scripts/` so the Audit & Package workflow is self-contained.
EOF

printf '__pycache__/\n*.pyc\n.DS_Store\n' > "$W/.gitignore"

cd "$W" || { echo "FAIL: cd"; exit 1; }
git init -q && git symbolic-ref HEAD refs/heads/main || { echo "FAIL: git init"; exit 1; }
# fetch the remote head so idempotency can compare against IT (local HEAD is
# unborn on a fresh staging dir; first push has no remote yet -> ignored)
git -c credential.helper= fetch -q \
  "https://x-access-token:$TOKEN@github.com/$USER/$REPO.git" main 2>/dev/null || true
git -c user.name="$USER" -c user.email="$USER@users.noreply.github.com" add -A >/dev/null 2>&1
if git rev-parse --verify -q FETCH_HEAD >/dev/null 2>&1 \
    && git diff --cached --quiet FETCH_HEAD -- .; then
  echo "nothing changed, repo already current"; rm -rf "$W"; exit 0
fi
git -c user.name="$USER" -c user.email="$USER@users.noreply.github.com" \
  commit -q -m "Add skills-infra: shared helpers + eval harness"

# CI may have advanced the remote; rebase before pushing. `-X theirs` keeps
# the LOCAL version of any file changed on both sides (this repo's staging
# dir is the source of truth; CI-only artifacts it doesn't stage survive).
# `|| true` is INTENTIONAL: first push has no remote branch yet.
git -c credential.helper= pull --rebase -X theirs -q \
  "https://x-access-token:$TOKEN@github.com/$USER/$REPO.git" main 2>/dev/null || true
if git -c credential.helper= push -q \
  "https://x-access-token:$TOKEN@github.com/$USER/$REPO.git" main; then
  echo "pushed: ok"
else
  echo "pushed: FAIL"
  exit 1
fi
rm -rf "$W"
echo "=== done: $USER/$REPO updated ==="
