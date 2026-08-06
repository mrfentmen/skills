# Japanese Skills Routing Hardening

## Goal

Improve confidence in the 13 Japanese-form coding skills by testing semantic routing on fresh blind prompts and comparing skill outputs against independently authored conventional baselines.

## Scope

The pass covers:

- haiku, tanka, senryu, haibun, sedoka, katauta, gogyohka, lunes, monoku, sijo, choka, dodoitsu, and renga.
- Three fresh blind routing prompts per skill (39 prompts total), plus two ordinary coding `none` prompts.
- A separate dataset and evaluator so the historical 60-prompt out-of-set benchmark remains immutable and reproducible.
- Independent baseline outputs for the existing Japanese-form benchmark prompts, authored from prompts alone without loading the corresponding `SKILL.md`.

## Blind routing dataset

Add `evals-infra/legacy/japanese_out_of_set_prompts_v2.json` with:

- Stable prompt IDs distinct from the historical dataset.
- Exactly one target label per prompt, or `none`.
- Prompt types drawn from `paraphrase`, `boundary`, and `trap`, with explicit notes kept out of the blind scorer sheet.
- Form names, trigger phrases, and direct line-budget leakage omitted where the intent can be expressed naturally without them.
- Duplicate checks against both the historical out-of-set prompts and the in-set trigger queries.

The new evaluator will reuse the existing blind-sheet/scoring protocol and emit a separate report containing overall accuracy, per-type accuracy, per-label metrics, and confusion pairs. Existing decisions and reports will not be overwritten.

## Independent baselines

Add a provenance manifest under `evals-infra/legacy/independent_baselines/` that records:

- The source prompt and output path for each baseline.
- The authoring rule: prompt-only, no skill file, no with-skill output, and no generated variance variant as a source.
- A stable authoring timestamp and baseline version.

Materialize baseline source files into the existing Japanese iteration-3 workspace layout for grading. Baselines will be conventional, readable programs that solve the task without deliberately imitating the target form. They will be independently authored per eval rather than generated from skill outputs or from one shared template.

## Validation

Run these gates after implementation:

1. JSON schema, target-label, duplicate, and prompt anti-leak checks.
2. New blind routing evaluator with deterministic scoring/report generation.
3. Existing trigger-overlap, description-sync, and static audit checks.
4. Grading and runnability for all Japanese baselines and existing outputs.
5. Distinct variance verification and the complete CI wrapper.

A failure in any gate blocks completion; no score or routing claim will be reported unless the corresponding artifact is regenerated and validated.

## Non-goals

- Do not rewrite the historical 60-prompt ground truth.
- Do not change skill descriptions or form contracts as part of this pass.
- Do not use generated run-2/run-3 variants as independent baselines.
- Do not claim an LLM-vs-LLM result without a second model/scorer; the mechanical router remains a lower-bound comparison only.
