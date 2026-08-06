# Current-Scope Release Report

> **UPDATE (2026-08-06): the public monorepo scope is now 13 skills.** `god`,
> `smoker`, `terry-davis`, `psych`, and `no-bullshit` moved to the public
> `mrfentmen/skills-2` repo (joined by `quantum-computing`); the `skills`
> monorepo is public. All numbers below describe the historical 18-skill scope
> as of commit `629e96f`; the 13-skill current state has a 145-record trigger
> scope (65 explicit + 26 boundary + 36 global `none` + 18 global `trap`).

**Release scope (historical):** 18 coding skills, 180 trigger-evaluation queries  
**Report date:** 2026-08-06  
**Repository commit:** `629e96f` - `Initialize skills monorepo with validated skills and CI`

## Executive summary

The current local scope contains 18 standalone skills and a balanced 180-query trigger set. The deterministic quality and reproducibility gates pass for the current tree. The 180-query trigger set is retained as historical regression data; its query wording and recorded decisions predate the standalone activation rewrite. The committed real-trigger decision artifact reports perfect agreement with its labeled set, while the report must be treated as an upper bound because the same evaluation process authored or reviewed the decisions and query ground truth.

The separate 60-prompt out-of-set routing benchmark is the more discriminating generalization check. Its recorded model result is 36/60 top-1 accuracy (0.600), with the weakest performance on trap prompts. The mechanical keyword router is intentionally a lower bound, not a substitute for an independent blind model.

## Current skill inventory

The 18 local `SKILL.md` directories are:

| Skill | Category |
|---|---|
| `choka` | Japanese form |
| `dodoitsu` | Japanese form |
| `god` | Creator-level coding and architecture persona |
| `gogyohka` | Japanese form |
| `haibun` | Japanese form |
| `haiku` | Japanese form |
| `katauta` | Japanese form |
| `lunes` | Japanese/American form |
| `monoku` | Japanese form |
| `no-bullshit` | Verification-first engineering |
| `psych` | Psychedelic and emergent algorithms |
| `renga` | Japanese linked-verse form |
| `sedoka` | Japanese form |
| `senryu` | Japanese form |
| `sijo` | Korean form |
| `smoker` | Battle-tested engineering persona |
| `tanka` | Japanese form |
| `terry-davis` | TempleOS/HolyC-inspired coding persona |

The inventory is derived from directories directly containing `SKILL.md`, not from historical workspace folders.

## Primary trigger evaluation

**Source:** `evals-infra/legacy/trigger_eval_queries.json`  
**Decision artifact:** external harness file `/Users/del/Desktop/skills 3 /evals-infra/legacy/real_trigger_decisions.json`  
**Report:** external harness file `/Users/del/Desktop/skills 3 /evals-infra/legacy/real_trigger_eval_report.md`  
**Release note:** the relocated harness and its decision/report artifacts are outside the monorepo commit; paths above describe the local validation source.

| Measure | Current result |
|---|---:|
| Skills | 18 |
| Queries | 180 |
| Positive (`should_trigger: true`) | 90 |
| Negative (`should_trigger: false`) | 90 |
| Recorded disagreements | 0 / 180 |
| Precision | 1.000 |
| Recall | 1.000 |
| F1 | 1.000 |

Every skill contributes 10 queries: five positive and five negative. The evaluation sheet deterministically shuffles each skill's queries by skill name, so source ordering does not provide a positional shortcut.

### Primary-evaluation caveat

These results are not an independent blind-model result. The recorded decisions were authored by the model under test, and the query set/ground truth was tuned in the same project. The 1.000/1.000/1.000 result is therefore a reproducibility and consistency result, and an upper bound for expected performance from an actually independent scorer.

## Trigger-overlap hygiene

**Source:** external harness file `/Users/del/Desktop/skills 3 /evals-infra/legacy/trigger_overlap_report.md`

| Check | Result |
|---|---:|
| Strong cross-skill overlaps (two or more foreign terms) | 0 |
| Weak one-term boundary overlaps | 24 |
| False-query self-check violations | 0 |
| False queries accounted for | 90 / 90 |
| False queries routed to a sibling | 75 |
| Clean unrouted negatives | 15 |

The 24 weak overlaps are documented boundary cases, including shared poetic vocabulary (`haibun`/`haiku`, `tanka`/`haiku`, `sedoka`/`katauta`), persona overlap (`smoker`/`no-bullshit`), and art/algorithm boundaries (`psych`/`artistic-creative`). No strong overlap or self-trigger violation is present in the current report.

## Out-of-set routing generalization

**Source:** external harness files `/Users/del/Desktop/skills 3 /evals-infra/legacy/out_of_set_prompts.json` and `out_of_set_eval_report.md`  
**Scope:** 60 fresh prompts: two per current skill plus two `none` prompts. These artifacts are outside the monorepo commit.

### Recorded model result

| Measure | Result |
|---|---:|
| Top-1 routing accuracy | 0.600 (36 / 60) |
| Macro precision/recall/F1 | 0.947 / 0.947 / 0.947 |
| Paraphrase accuracy | 0.586 (17 / 29) |
| Boundary accuracy | 0.650 (13 / 20) |
| Trap accuracy | 0.444 (4 / 9) |
| `none` accuracy | 1.000 (2 / 2) |

The report also records 24 invalid answers that named skills outside the active 18-skill set. They count as wrong for top-1 routing, which is appropriate for a closed 18-label release scope.

### Interpretation

The out-of-set result is the current generalization warning: semantic paraphrases and sibling traps are materially harder than the tuned in-set queries. Trap prompts are the weakest class and should be the first target for future routing hardening. The same-author upper-bound caveat applies to these recorded decisions and ground truth.

The mechanical keyword-router report is intentionally much lower: 0.117 top-1 accuracy (7/60). That is an expected lower bound for prompts designed to defeat literal-term matching; it is not evidence that the descriptions themselves fail.

## Skill-output benchmark snapshot

**Source:** generated local snapshots `/Users/del/Desktop/skills/ALL_SKILLS_BENCHMARK.md`, `/Users/del/Desktop/skills/FORM_RHYTHM_REPORT.json`, and `/Users/del/Desktop/skills/SKILL_AUDIT.json`, plus associated iteration-3 workspace artifacts. These snapshots were generated on 2026-08-06 (benchmark/rhythm: 00:56 local time; audit: 01:18 local time), are ignored local artifacts, and are not part of the source release payload.

The latest local benchmark snapshot records a with-skill score of **1.00 for all 18 skills**. Recorded conventional baseline scores and deltas are:

| Skill | Baseline | With skill | Delta | Runnable |
|---|---:|---:|---:|---:|
| choka | 0.68 | 1.00 | +0.32 | 3/3 |
| dodoitsu | 0.57 | 1.00 | +0.43 | 3/3 |
| god | 0.29 | 1.00 | +0.71 | 2/2 |
| gogyohka | 0.67 | 1.00 | +0.33 | 3/3 |
| haibun | 0.67 | 1.00 | +0.33 | 3/3 |
| haiku | 0.69 | 1.00 | +0.31 | 7/7 |
| katauta | 0.56 | 1.00 | +0.44 | 3/3 |
| lunes | 0.67 | 1.00 | +0.33 | 3/3 |
| monoku | 0.75 | 1.00 | +0.25 | 3/3 |
| no-bullshit | 0.47 | 1.00 | +0.53 | 3/3 |
| psych | 0.75 | 1.00 | +0.25 | 2/2 |
| renga | 0.62 | 1.00 | +0.38 | 3/3 |
| sedoka | 0.67 | 1.00 | +0.33 | 3/3 |
| senryu | 0.67 | 1.00 | +0.33 | 3/3 |
| sijo | 0.67 | 1.00 | +0.33 | 3/3 |
| smoker | 0.47 | 1.00 | +0.53 | 3/3 |
| tanka | 0.61 | 1.00 | +0.39 | 3/3 |
| terry-davis | 0.62 | 1.00 | +0.38 | 2/2 |

### Benchmark caveats

- These are mechanical assertion scores, not a human quality judgment.
- Baselines are conventional solutions evaluated against skill-specific structural or vocabulary assertions; the delta measures the current harness contract, not general coding ability.
- Runnability is separately reported and does not automatically imply semantic correctness for every possible input.
- Generated workspaces and benchmark reports are excluded from the committed source scope by repository ignore rules.

## Release gates

The current deterministic checks passed:

- **Skill contract:** 18 skills, required sections present, trigger coverage aligned.
- **Static skill audit:** all skills at or above the 0.75 quality floor; current audit snapshot reports 1.00 across the skill entries.
- **Description synchronization:** 0 drifted, 0 missing.
- **Trigger overlap:** 0 strong overlaps, 0 self-check violations.
- **Real-trigger reproducibility:** full 18-skill set reproduces 1.000 precision/recall/F1 from committed decisions.

The local Git working tree was clean before this report was created at commit `629e96f`; creating this report itself is the current intended source change.

## Release conclusion

**Status: conditionally source-scope ready, with routing generalization caveats.**

The source tree satisfies structural quality and reproducibility gates, and the historical 180-query trigger artifact remains internally consistent. This is conditional source-scope readiness, not proof of independent routing performance: the primary decisions are same-author, the query wording predates the standalone rewrite, and the main unresolved quality signal is semantic routing on fresh out-of-set prompts, especially traps and prompts that cause invalid labels outside the current 18-skill set. A future release should add independently scored blind routing data and retain the current 60-prompt benchmark as a historical comparison rather than replacing it.

## Reproduction commands

From the project root, with the relocated harness path configured:

```bash
ROOT=/Users/del/Desktop/skills
HARNESS='/Users/del/Desktop/skills 3 /evals-infra'
export SKILLS_ROOT="$ROOT" EVALS_INFRA_ROOT="$HARNESS"

python3 "$HARNESS/skill_contract_check.py" --root "$ROOT"
python3 "$HARNESS/static_skill_audit.py" --root "$ROOT" --min-score 0.75
python3 "$HARNESS/sync_descriptions.py" --root "$ROOT" --check
python3 "$HARNESS/trigger_overlap_check.py" --root "$ROOT"
python3 "$HARNESS/run_real_trigger_eval.py" --no-wait --quiet
```

The out-of-set report is present as a deterministic artifact under the external harness legacy directory; it is not included in monorepo commit `629e96f`. A new scorer can be supplied through the external harness's `run_out_of_set_eval.py --scorer ...` without changing the historical ground truth.
