# Historical regression suite: frozen-artifact record

Last verified current-scope run: **2026-08-07**. The suite is the pre-relocation
harness at `/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh`, kept
separate from the current-scope gate in this repo
(`standalone-evals/run_current_ci.sh`).

## TL;DR

| Invocation | Result | Meaning |
|---|---:|---|
| 18-skill era, before the public-scope reorg | **11/11 PASS** | Historical baseline recorded on 2026-08-06 |
| 13-skill post-reorg scope, before the 15-form expansion | **9/11 checks passed** | Five moved persona entries were expected mismatches |
| Current 28-form scope in isolated compatibility scope | **9/11 checks passed** | The frozen legacy dataset lacks the 15 newer forms and moved personas; one description drift is also reported |
| Current 28-form scope in the raw host tree | **8/11 checks passed** | Adds the old workspace variance-layout mismatch to the frozen metadata mismatches |
| Current 28-form scope without `SKILLS_ROOT` | **8/11 checks passed** | The relocated harness compares its frozen parent tree with the current-era dataset |

The current historical command exits **1** for this repository scope. The
isolated compatibility assertion intentionally recognizes the stable 9/11
metadata mismatch; the raw host-tree command can be 8/11 when old workspace
artifacts are visible.
That red result is not silently relabeled green. It is a compatibility result
against frozen artifacts, not the release gate for the current 28-form tree.

## Actual current run

Command:

```bash
SKILLS_ROOT="$(pwd)" bash "/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh"
```

Verified result on 2026-08-07:

- trigger-overlap: pass
- static skill audit: pass, all current skills score 1.00
- description sync: **fail**
- skill contract: **fail**
- dash sweep: pass
- reproducible real/out-of-set evaluations: pass
- generated artifacts: pass
- distinct variance variants: pass in the isolated compatibility scope; raw host-tree runs may fail on obsolete workspace layouts

The failing historical checks report:

- five moved persona skills absent from the current tree: `god`, `no-bullshit`,
  `psych`, `smoker`, and `terry-davis`
- fifteen newer forms absent from the frozen legacy trigger dataset:
  `bussokusekika`, `cinquain`, `etheree`, `fibonacci`, `imayo`, `kanshi`,
  `kyoka`, `limerick`, `renshi`, `ryuka`, `somonka`, `sonnet`, `villanelle`,
  `waka`, and `zappai`
- a `gogyohka` description drift between the current frontmatter and the
  frozen legacy JSON
The raw host-tree invocation additionally reports that the frozen distinct-variance
check expects canonical files in the old workspace layout. The isolated
compatibility check intentionally excludes those unrelated host-only workspace
artifacts.

These failures are expected from comparing different historical scopes. They
must not be fixed by mutating or replacing the frozen legacy dataset.

## Why the default-root invocation fails

The runner resolves its target tree from `SKILLS_ROOT` when set; otherwise it
uses the parent directory of the relocated harness:

```python
BASE = Path(os.environ.get("SKILLS_ROOT", str(HARNESS.parent)))
```

The harness was relocated to `/Users/del/Desktop/skills 3 /evals-infra`.
Its parent is a frozen pre-relocation snapshot, not the current 28-form tree.
The default-root invocation therefore compares two unrelated snapshots and
reports additional missing skills and historical workspace variants.

Reproduce it with:

```bash
bash "/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh"
```

## Policy

- **Current release health** is `standalone-evals/run_current_ci.sh` plus
  `standalone-evals/check_rhythm_examples.py`. With `HISTORICAL_HARNESS` configured,
  the current gate passes **37/37** mechanical checks; without it, the historical
  compatibility check is explicitly skipped and the current gate is **36/36**.
  The regression gate's 1/28 control result is a frozen same-author baseline, not
  a claim that every plain program should fail its form check.
  Separately, all 28 documented examples plus all 28 E3 references pass.
- The external historical suite remains an informational compatibility check.
- The 11/11 and 9/11 results above are preserved as historical snapshots; they
  are not claims about the current 28-form scope.
- Do not mutate frozen legacy trigger data merely to make a cross-scope command
  exit zero. If a zero-exit historical gate is required, create a separately
  versioned 28-skill historical dataset and harness rather than rewriting this
  artifact.
