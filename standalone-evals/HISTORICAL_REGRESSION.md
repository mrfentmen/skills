# Historical regression suite — frozen-artifact record

Last full run: **2026-08-06**. The suite is the pre-relocation eval harness at
`/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh`, kept deliberately
separate from the current-scope gate in this repo (`standalone-evals/run_current_ci.sh`).

## TL;DR

| Invocation | Result |
|---|---|
| `SKILLS_ROOT=<this repo>` (18-skill era, pre-reorg) | **11/11 PASS (exit 0)** |
| `SKILLS_ROOT=<this repo>` (13-skill public scope, post-reorg) | 9 PASS, **2 expected failures** (frozen 18-skill dataset entries for god/smoker/terry-davis/psych/no-bullshit) |
| `bash "<harness>/run_ci_checks.sh"` (no `SKILLS_ROOT`) | 8 PASS, **3 known failures** (frozen artifacts) |

The 3 failures are **not** defects in the current 18 skills. They are a mismatch
between (a) the harness's default root and (b) the legacy trigger dataset, plus
an obsolete canonical-outputs expectation. They are frozen: fixing them would
mean mutating historical artifacts that are intentionally kept as-is.

## Why the default-root invocation fails

`run_ci_checks.sh` and the Python checks resolve their target tree from
`SKILLS_ROOT` if set, otherwise from the harness's own parent directory:

```python
# e.g. skill_contract_check.py / sync_descriptions.py / gen_distinct_variants.py
BASE = Path(os.environ.get("SKILLS_ROOT", str(HARNESS.parent)))
```

The harness was relocated out of the repo to `/Users/del/Desktop/skills 3 /evals-infra`.
Its parent, `/Users/del/Desktop/skills 3 /`, is a **frozen pre-relocation snapshot**
of the original skill tree: it contains the 12 retired aesthetic skills
(`artistic-creative`, `biomimicry`, `cosmic-horror`, `esoteric-programming`,
`glitch-art`, `mathematical-elegance`, `minimalist-zen`, `quantum-computing`,
`renaissance`, `retro-computing`, `steampunk`, `zen-calligraphy`) — and does
**not** contain the 18 current skills.

Meanwhile the harness's legacy dataset
(`evals-infra/legacy/trigger_eval_queries.json`) was updated to describe the **18
current skills** (it is in sync with their frontmatter descriptions). So the
default-root run cross-validates two snapshots that were never meant to be
compared.

## Known frozen failures (default-root invocation)

Run on 2026-08-06, exit 1. Reproduced identically on every recorded run
(2026-08-06).

### 1. skill contract — 54 issues

- 12 × `missing trigger-dataset entry` — the 12 retired skills exist in the old
  tree (default root) but have no entry in the current-era legacy dataset.
- 18 × `trigger-dataset entry has no local SKILL.md` — the 18 current skills
  have dataset entries but no `SKILL.md` in the old tree (default root).
- 12 × `trigger description differs from frontmatter` — same 12 retired skills
  as above: the dataset has no entry for them, so the empty spec never equals
  their frontmatter description.
- 12 × `trigger eval_queries must be a non-empty list` — same 12 retired
  skills: the empty spec has no `eval_queries`.

### 2. description sync — 30 missing

- 18 × `MISSING <skill>: no frontmatter description (would prune)` — dataset
  lists the 18 current skills; the old tree (default root) has no `SKILL.md` for
  them, so the frontmatter lookup returns "missing".
- 12 × `MISSING <skill>: no entry in trigger_eval_queries.json` — the old tree's
  12 retired skills have `SKILL.md` files with no dataset entry.

### 3. distinct variance variants — 49 problems

- 49 × `no canonical for <skill>-workspace/iteration-3/eval-*` — the old tree's
  frozen `iteration-3` eval directories predate the canonical-outputs convention
  (`with_skill/outputs/`), so the distinct-variant check finds no canonical
  reference to diff run-2/run-3 against.

### Checks that pass in both invocations

trigger-overlap, static skill audit, dash sweep, real trigger-eval reproducible,
out-of-set routing eval reproducible, keyword-router real-eval report
reproducible, keyword-router out-of-set report reproducible, generated artifacts
in sync.

## Public-scope reorg (2026-08-06, two rounds)

Round 1: the monorepo dropped `god`, `smoker`, and `terry-davis` to the private
`mrfentmen/skills-2` repo (joined by `quantum-computing`). Round 2: `psych` and
`no-bullshit` also moved there, and `skills-2` became public. The monorepo now
holds the **13 form skills**; skills-2 holds the **6 persona skills** (`god`,
`smoker`, `terry-davis`, `quantum-computing`, `psych`, `no-bullshit`).

The legacy harness dataset (`evals-infra/legacy/trigger_eval_queries.json`)
remains **frozen at 18 skills**, so with `SKILLS_ROOT` set to the 13-skill repo
exactly two checks fail as expected frozen-artifact mismatches:

- **skill contract**: 5 x `trigger-dataset entry has no local SKILL.md`
  (god, smoker, terry-davis, psych, no-bullshit).
- **description sync**: 5 x `MISSING god|smoker|terry-davis|psych|no-bullshit:
no frontmatter description (would prune)`.

These are not defects: the dataset still describes the pre-reorg scope. The
current-scope gate (`standalone-evals/run_current_ci.sh`) passes **18/18** at the
13-skill scope. This run also fixed em dashes introduced into `haiku/SKILL.md`
and `senryu/SKILL.md` by E-009/E-010 (the historical dash sweep bans them); the
sweep is green again.

## Correct usage

Always set `SKILLS_ROOT` so the historical suite validates **this** tree (9/11
at the 13-skill scope, with the 2 expected frozen-dataset failures above)
instead of its default frozen parent:

```bash
SKILLS_ROOT="$(pwd)" bash "/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh"
```

Reproduce the frozen-artifact failures (informational only):

```bash
bash "/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh"
```

## Policy

- **Current-repo health** = `standalone-evals/run_current_ci.sh` (mechanical
  gate, 18/18 at the 13-skill public scope) plus the historical suite run with
  `SKILLS_ROOT` set (9/11; the 2 failures are the frozen 18-skill dataset
  entries for god/smoker/terry-davis/psych/no-bullshit, documented above).
- **Never** read a default-root failure of the historical suite as a defect in
  the current 18 skills; it validates the frozen `skills 3 /` snapshot.
- The 3 failing checks are intentionally **not fixed**: the old tree and the
  legacy dataset are frozen historical regression data and are not rewritten or
  silently replaced.
