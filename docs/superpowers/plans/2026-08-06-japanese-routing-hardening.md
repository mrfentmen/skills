# Japanese Skills Routing Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a fresh blind routing benchmark for all 13 Japanese-form skills and independently authored conventional baselines for their existing iteration-3 tasks, without changing historical benchmark truth.

**Architecture:** Keep the historical `out_of_set_prompts.json` and its decisions immutable. Add a separate Japanese-only dataset plus a parameterized evaluator that reuses the existing blind-sheet/scoring protocol and writes separate sheet, decisions, and report artifacts. Author one conventional baseline per existing Japanese iteration-3 eval, store those sources in the ignored workspace tree, and track only a provenance manifest and deterministic validation metadata in `evals-infra/legacy/independent_baselines/`.

**Tech Stack:** Python 3 standard library, JSON, existing `real_trigger_eval.py`/`run_out_of_set_eval.py` helpers, existing `grade_evals.py`, `check_runnability.py`, `gen_distinct_variants.py`, and shell CI wrapper.

## Global Constraints

- Do not rewrite the historical 60-prompt out-of-set dataset, decisions, or reports.
- Blind prompts must omit direct form names and trigger phrases wherever the intent can be expressed naturally.
- Each new prompt has exactly one target label or `none`; no ambiguous multi-target ground truth.
- Independent baselines must be prompt-only, conventional, readable, and never copied from `SKILL.md`, a with-skill output, or a generated variance variant.
- Do not claim LLM-vs-LLM routing results without a second model/scorer; mechanical routing is only a lower-bound comparison.
- Preserve existing skill descriptions, form contracts, and historical scores.
- Keep generated workspaces, caches, packages, and reports out of the tracked source scope.

---

### Task 1: Add the Japanese blind-routing dataset and validator

**Files:**
- Create: `evals-infra/legacy/japanese_out_of_set_prompts_v2.json`
- Create: `evals-infra/legacy/validate_japanese_out_of_set.py`
- Test: validator command itself plus duplicate/anti-leak assertions

**Interfaces:**
- Dataset top-level shape: `{"meta": {...}, "prompts": [{"id", "prompt", "target", "type", "note"}]}`.
- Target labels: the 13 Japanese skill names plus `none`.
- Validator CLI: `python3 evals-infra/legacy/validate_japanese_out_of_set.py [--root ROOT]`; exit 0 only when schema, uniqueness, target counts, duplicate checks, and anti-leak checks pass.

- [ ] Write 41 records: three prompts each for `haiku`, `tanka`, `senryu`, `haibun`, `sedoka`, `katauta`, `gogyohka`, `lunes`, `monoku`, `sijo`, `choka`, `dodoitsu`, and `renga`, plus two `none` prompts.
- [ ] Use a balanced type mix across each skill: one paraphrase, one sibling boundary, and one trap. Keep author notes in the dataset but exclude notes from the blind scorer sheet.
- [ ] Ensure prompts are fresh against both `legacy/out_of_set_prompts.json` and `legacy/trigger_eval_queries.json` using normalized whitespace and case-insensitive exact comparison.
- [ ] Ensure no prompt contains its target skill’s literal name or a direct form signature phrase such as `5-7-5`, `5-7-7`, `one line`, `closing couplet`, `stanza`, `twist`, or `free-form`; when a prompt inherently needs a shape, express it semantically instead.
- [ ] Validate target counts, type counts, duplicate IDs, duplicate normalized prompts, and target-label membership.
- [ ] Validate that every target skill has exactly three prompts and `none` has exactly two.

### Task 2: Parameterize the blind routing evaluator

**Files:**
- Modify: `evals-infra/run_out_of_set_eval.py`
- Modify: `evals-infra/legacy/out_of_set_eval_prompt.md` only if the shared instructions need a dataset-neutral wording
- Create: `evals-infra/legacy/japanese_out_of_set_eval_prompt.md` if separate instructions are safer
- Create: `evals-infra/legacy/run_japanese_out_of_set_eval.py`
- Test: deterministic sheet generation, mechanical scorer, and report output

**Interfaces:**
- New CLI: `python3 evals-infra/legacy/run_japanese_out_of_set_eval.py [--scorer CMD|--decisions FILE|--no-wait|--timeout N]`.
- It must write only Japanese-specific artifacts: `japanese_out_of_set_eval_sheet.md`, `japanese_out_of_set_decisions.json`, and `japanese_out_of_set_eval_report.md`.
- It must reuse the existing blind-sheet shuffle and grading behavior, with the new dataset path supplied explicitly rather than changing the historical evaluator defaults.

- [ ] Extract or wrap the existing sheet/scoring/grade functions without changing historical output paths or semantics.
- [ ] Build the blind sheet from descriptions plus shuffled prompts, never including `target`, `type`, or `note`.
- [ ] Accept the existing compact or object decision formats and reject missing labels, extra labels, invalid values, and wrong prompt counts.
- [ ] Add deterministic report sections for total accuracy, paraphrase/boundary/trap/none accuracy, per-label precision/recall/F1, and top confusion pairs.
- [ ] Run with the existing keyword router as a lower-bound scorer and store its result separately from any human/model-authored decision file.
- [ ] Add a small regression check proving the historical evaluator’s output paths remain unchanged.

### Task 3: Author independent Japanese baselines

**Files:**
- Create: `evals-infra/legacy/independent_baselines/manifest.json`
- Create: `evals-infra/legacy/independent_baselines/README.md`
- Create: `evals-infra/legacy/independent_baselines/authoring_check.py`
- Create/update ignored sources under: `*-workspace/iteration-3/eval-*/without_skill/independent-baseline/solution.py`
- Test: manifest/source provenance check, grader, and runnability

**Interfaces:**
- Manifest shape: `{"version": 1, "authoring_rule": ..., "entries": [{"skill", "eval_id", "eval_name", "prompt_sha256", "source", "language", "derived_from": []}]}`.
- Authoring checker CLI: `python3 evals-infra/legacy/independent_baselines/authoring_check.py --root ROOT`; it verifies every Japanese iteration-3 eval has exactly one manifest entry, source exists, prompt hash matches metadata, `derived_from` is empty, and no source path is under `with_skill`, `run-2`, or `run-3`.

- [ ] Author a conventional baseline independently for every existing Japanese iteration-3 eval, using only `eval_metadata.json.prompt` and the task requirements; do not read the skill files or with-skill outputs during authoring.
- [ ] Use readable Python implementations for Python prompts and preserve the existing JavaScript/Cross-language conventions where the eval requires them; do not force a target poetic shape onto baselines.
- [ ] Copy or link each baseline into the corresponding `without_skill/outputs/independent-baseline/` directory only after authoring, without replacing the existing historical baseline output.
- [ ] Add manifest entries with SHA-256 hashes of the exact prompt and source path, plus explicit `derived_from: []`.
- [ ] Make the authoring checker reject duplicate source hashes across unrelated evals when the files are byte-identical, preventing a shared template from masquerading as independent authorship.
- [ ] Grade the independent-baseline files using the existing metadata and record a separate baseline summary report, without overwriting historical `grading.json`.

### Task 4: Add deterministic validation/report plumbing

**Files:**
- Modify: `evals-infra/run_ci_checks.sh` only if the new validator can run without requiring model decisions
- Create: `evals-infra/legacy/japanese_baseline_report.py` if a separate summary is needed
- Modify: `evals-infra/HOW_TO_RUN_EVALS.md` with commands and provenance caveats
- Test: validator, baseline checker, mechanical router, and report reproducibility

**Interfaces:**
- `japanese_baseline_report.py --root ROOT` writes `japanese_independent_baseline_report.md` under the legacy evaluation directory.
- All deterministic commands exit nonzero on malformed data, stale reports, missing baseline sources, non-runnable outputs, or provenance violations.

- [ ] Add documentation for the new dataset, blind evaluator, baseline authoring rule, and exact commands.
- [ ] Keep model-dependent scoring optional: CI validates dataset shape, duplicates, anti-leak properties, manifest/source integrity, and mechanical-router reproducibility without waiting for an LLM.
- [ ] Add artifact-sync handling only for tracked deterministic reports; do not commit generated workspace outputs or local scorer secrets.

### Task 5: Run full validation and review

**Files:**
- Review all files changed above
- No source changes unless a validation failure identifies a concrete defect

- [ ] Run `python3 evals-infra/legacy/validate_japanese_out_of_set.py --root /Users/del/Desktop/skills`.
- [ ] Run `python3 evals-infra/legacy/independent_baselines/authoring_check.py --root /Users/del/Desktop/skills`.
- [ ] Run the Japanese evaluator with `python3 evals-infra/legacy/run_japanese_out_of_set_eval.py --scorer "python3 evals-infra/keyword_router.py"` and verify deterministic rerun output.
- [ ] Run `grade_evals.py`, `check_runnability.py --root`, `gen_distinct_variants.py --check`, and the full `run_ci_checks.sh` with explicit `SKILLS_ROOT`/`EVALS_INFRA_ROOT`.
- [ ] Review staged diff for secrets, workspace leakage, accidental historical-artifact rewrites, duplicate baselines, and undocumented score claims.
- [ ] Have a code reviewer inspect the final changes and fix any concrete blockers.
