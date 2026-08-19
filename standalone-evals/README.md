# Standalone evaluation foundation

This directory contains the **current**, versioned activation benchmark for the
28 independently installable skills (the public monorepo scope; persona skills
god/smoker/terry-davis/psych/no-bullshit live in the public skills-2 repo).
It is deliberately separate from the
historical evaluation artifacts in the external `evals-infra/legacy/` tree.

## Dataset

`standalone_trigger_benchmark_v1.json` contains 250 versioned current-scope
routing records (140 explicit/signature + 56 boundary + 36 ordinary + 18 trap;
the ordinary and trap records are global, not per-skill). The validator proves
their structural coverage and anti-leak properties; independent authorship and
blind review are separate Phase 3 evidence and are not claimed by this file:

- 28 skills × 5 explicit-or-signature records = 140
- 28 skills × 2 close boundary records = 56
- 36 ordinary non-skill records
- 18 trap records

The current dataset requires explicit identity or an unmistakable contract for
a skill to be selected. Boundary, ordinary, and trap prompts contain no literal
skill-name tokens. The validator checks the schema, coverage, duplicates,
anti-leak rules, and that every target exists locally.

## Commands

From the skills repository root:

```bash
EVALS_INFRA_ROOT="/Users/del/Desktop/skills 3 /evals-infra" \
HISTORICAL_HARNESS="/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh" \
  bash standalone-evals/run_current_ci.sh
# The historical suite is separate. Always set SKILLS_ROOT so it validates
# THIS tree. For the current 28-skill scope it reports 9/11 checks passed in the isolated compatibility scope (the raw host-tree invocation reports 8/11 because of old workspace artifacts) and
# exits 1 because the frozen historical dataset predates the newer forms and
# relocated persona skills; the exact current mismatches are documented below:
# SKILLS_ROOT="$PWD" bash "/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh"
# When HISTORICAL_HARNESS is set, the current gate also runs a safe compatibility
# assertion for the frozen harness; it passes only when the documented isolated
# 9/11 mismatch is reproduced. Without that variable, compatibility is explicitly
# skipped and the current-scope result is 36/36 rather than a historical result.
# With HISTORICAL_HARNESS configured, the current-scope result is 37/37.
# See standalone-evals/HISTORICAL_REGRESSION.md for the frozen-artifact record.
# Or run the individual checks below:
python3 standalone-evals/validate_standalone_benchmark.py --root .
python3 standalone-evals/check_skill_isolation.py --root .
python3 standalone-evals/run_example_smoke.py --root .
python3 standalone-evals/make_blind_sheet.py --root . --output /tmp/standalone-trigger-v1-blind.json
# After an independent scorer returns decisions keyed by record ID:
python3 standalone-evals/score_blind_decisions.py --decisions /path/to/decisions.json --output /tmp/standalone-trigger-v1-score.json
```

The isolation check packages each skill using a temporary source tree that
contains only that skill, extracts the package into a clean temporary directory,
and rejects sibling/shared/runtime routing dependencies.

The example smoke check inventories every fenced example. Python examples are
syntax-compiled; JavaScript examples are checked with Node module syntax when
Node is available. Unsupported languages, interactive programs, and servers are
explicit skips, not claims of runtime correctness. A syntax pass is evidence of
parseability only, not proof that the example handles every input.

`make_blind_sheet.py` creates a shuffled sheet containing current descriptions
and prompts but no gold labels (28-skill, 250-record scope). An independent
scorer can return one label per record ID; `score_blind_decisions.py` then
joins those decisions to the private benchmark and reports accuracy, per-type
results, and confusion pairs. Explicit-name rows are reported separately from
signature, boundary, trap, and none rows; only the latter semantic slices
should be used as generalization evidence.

**Recorded 2026-08-19:** a fresh scorer (model that saw only the shuffled
sheet; gold never revealed) returned decisions for all 250 records
(`blind_score_decisions_v1.json`) scoring **244/250 = 0.976**
(`blind_score_report_v1.json`): explicit 84/84, signature 56/56, boundary
50/56, ordinary→none 36/36, trap→none 18/18. The six boundary misses are
close form-silhouette calls (haiku↔zappai, cinquain↔gogyohka,
ryuka↔dodoitsu, limerick↔kyoka/gogyohka). A second independent scorer would
bound this number; the tooling below makes that a copy-paste exercise.

## Current-scope held-out workflow

The 145-record release benchmark measures whether the current-scope prompts are
well formed. The held-out set (`current_scope_heldout_v1.json`, 54 records) is a **frozen
historical artifact of the 18-skill era**, kept for comparison and not rebuilt
after the 15-skill reorg (its prompts reference skills that now live in
skills-2). It measures routing on fresh prompts the descriptions were not tuned
on: two intent prompts per skill (18 paraphrase + 18 boundary), 9
sibling/persona traps, and 9 ordinary prompts that should select `none`. It is
a separate experiment artifact, never a replacement for the release benchmark
or the frozen historical set.

### 1. Validate the held-out set

```bash
python3 standalone-evals/validate_current_heldout.py
```

Checks the 54-record schema, type counts (18/18/9/9), duplicate prompts,
skill-name leakage (including aliases such as `terry davis` / `no bullshit`),
and exact-prompt overlap with the release benchmark. Fails closed if
the release benchmark is missing.

### 2. Generate the blind scoring sheet

```bash
python3 standalone-evals/make_current_heldout_sheet.py \
  --output /tmp/current-heldout-blind-sheet.md
```

Writes the frozen 18-skill descriptions plus the 54 prompts in a deterministic shuffle
with **no gold labels** and no record types. Give only this sheet to a scorer
(a human or a model that has never seen the targets). Decisions are submitted
as a JSON object mapping every `heldout-v1-XXX` id to a skill name or `none`.

### 3. Run the mechanical baseline (floor)

```bash
python3 standalone-evals/run_current_heldout_baseline.py \
  --output /tmp/current-heldout-baseline.json
```

A deliberately simple full-`SKILL.md` token-overlap router. It is **not an AI
score**: it cannot read activation clauses, so it over-fires on ordinary
prompts for persona skills and misses numeric shape signatures. Its accuracy is
the mechanical floor, never evidence of a description defect.

### 4. Score submitted decisions

After a scorer returns a decisions file (JSON mapping ids to skill names or
`none`), join it to the private targets and report per-type accuracy:

```bash
DECISIONS="/tmp/skill-experiments/my-decisions.json"  # edit: your decisions file
DECISIONS="$DECISIONS" python3 - <<'PY'
import json
import os
from collections import defaultdict
from pathlib import Path

mine = json.loads(Path(os.environ["DECISIONS"]).read_text())
data = json.loads(Path("standalone-evals/current_scope_heldout_v1.json").read_text())
records = data["records"]
by_type = defaultdict(list)
for r in records:
    by_type[r["type"]].append(r)
for t in ("paraphrase", "boundary", "trap", "none"):
    sub = by_type[t]
    ok = sum(mine[r["id"]] == r["target"] for r in sub)
    print(f"{t}: {ok}/{len(sub)}")
print("all:", sum(mine[r["id"]] == r["target"] for r in records), "/", len(records))
PY
```

### Interpreting the three numbers

- **Mechanical baseline** (`run_current_heldout_baseline.py`) is the floor.
- **Same-author self-score** is an upper bound: the scorer wrote the prompts and
  labels, so a perfect score measures consistency, not independence.
- **A fresh scorer that only saw the blind sheet** is the meaningful number.
  Record it with its scorer identity and how it was blinded. Until such a score
  exists, held-out routing is mechanically validated but independently unproven.

## Release boundary

This is an evaluation foundation, **not a release report**. The current-scope command reports 100% for its mechanical checks, including
`check_current_scope_regressions.py`, which validates the current 250-query
trigger set, the frozen 54-record held-out comparison set, 28 executable gold
references, and the expected frozen 1/28 same-author control baseline. When `HISTORICAL_HARNESS` is
configured, it also runs an exact compatibility assertion for the frozen
historical harness; when it is not configured, that check is explicitly
skipped. Neither result proves
perfect AI behavior or independent generalization. The self-contained current historical-style suite is available as
`bash standalone-evals/run_current_historical_ci.sh`; it validates the current
28-skill tree without reading frozen external artifacts. The old 180-query set and its
recorded results remain frozen historical regression data; they are not rewritten
or silently replaced by this current standalone dataset. Run the external
`evals-infra/run_ci_checks.sh` separately (with `SKILLS_ROOT` set) when you
intentionally want historical regression checks too. As recorded on 2026-08-06,
the **current 28-skill scope satisfies 9/11 isolated historical checks (exit 1)** when
`SKILLS_ROOT` points at the isolated compatibility tree. The raw host-tree
invocation is 8/11 because it also sees old workspace variance artifacts. The
frozen dataset also predates the
15 newer forms and records one gogyohka description drift; the exact mismatches
are recorded in `standalone-evals/HISTORICAL_REGRESSION.md`. At the earlier
18-skill scope the suite was 11/11. With the 2026-08-06 expansion the repo now contains 28 form
skills. The 15 newer forms are not part of the frozen historical harness, and
five persona skills moved to skills-2; therefore the historical command is an
informational compatibility check, not a current release gate. The known
frozen-artifact failures are recorded in
`standalone-evals/HISTORICAL_REGRESSION.md`.
