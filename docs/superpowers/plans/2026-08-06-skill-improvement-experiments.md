# Skill Improvement Experiments Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve real routing clarity, output correctness, and standalone reliability for all 18 skills while preserving the current 100% mechanical gate and refusing changes that create regressions.

**Architecture:** Freeze the current 18-skill tree as a control candidate. Evaluate behavior through isolated prompt suites and independent scoring, then change one skill or one confusing pair at a time. Keep the frozen historical `evals-infra/legacy/` artifacts separate from the current `standalone-evals/` release gate.

**Tech Stack:** Markdown skill instructions, Python 3 standard-library validators, shell scripts, JSON prompt/decision artifacts, existing external evaluation harness.

## Global Constraints

- Preserve the historical `evals-infra/legacy/` benchmark, decisions, reports, and workspace evidence unchanged.
- Preserve the current 18-skill scope: `choka`, `dodoitsu`, `god`, `gogyohka`, `haibun`, `haiku`, `katauta`, `lunes`, `monoku`, `no-bullshit`, `psych`, `renga`, `sedoka`, `senryu`, `sijo`, `smoker`, `tanka`, `terry-davis`.
- Do not add sibling-skill routing instructions or external runtime dependencies to individual skills.
- Do not edit a skill merely to increase a static score.
- Every candidate change must preserve `standalone-evals/run_current_ci.sh` at 23/23 checks.
- Every candidate change must preserve package isolation for all 18 skills.
- Every candidate change must preserve zero strong cross-skill overlaps.
- A mechanical 100% is not an independent quality score; report these separately.
- Keep `CURRENT_SCOPE_RELEASE_REPORT.md` unreleased until independent evidence meets the agreed gate.

---

## Experiment 0: Freeze the control candidate

**Files:**
- Read: all 18 `*/SKILL.md` files
- Read: `standalone-evals/standalone_trigger_benchmark_v1.json`
- Read: `standalone-evals/run_current_ci.sh`
- Create: ignored output files under `/tmp/skill-experiments/control/`

**Purpose:** Establish the exact control behavior before any edit.

- [ ] **Step 1: Run the current mechanical gate**

Run:

```bash
cd "/Users/del/Desktop/skills"
EVALS_INFRA_ROOT="/Users/del/Desktop/skills 3 /evals-infra" \
  bash standalone-evals/run_current_ci.sh
```

Expected: `CURRENT-SCOPE RESULT: 23/23 mechanical checks passed (0 failed)` and exit code `0`.

- [ ] **Step 2: Generate a control blind sheet**

Run:

```bash
python3 standalone-evals/make_blind_sheet.py \
  --root . \
  --output /tmp/skill-experiments/control/blind.json
```

Expected: 180 prompts, no `target` or `type` fields in the output records.

- [ ] **Step 3: Record control metrics**

Record:

```text
mechanical_gate = 23/23
static_audit = 1.00
isolation = 18/18
smoke_failures = 0
strong_overlaps = 0
independent_blind_score = not yet available
```

Expected: these values remain unchanged throughout the experiment series unless a separately documented improvement is accepted.

---

## Experiment 1: Activation and abstention matrix

**Files:**
- Create: `/tmp/skill-experiments/activation-matrix.json`
- Use: `standalone-evals/standalone_trigger_benchmark_v1.json`
- Use: `standalone-evals/score_blind_decisions.py`

**Purpose:** Test whether the correct skill activates and whether unrelated skills stay quiet.

- [ ] **Step 1: Split prompts into five groups**

Use the benchmark labels only for private scoring:

1. explicit-name prompts: the skill is named directly;
2. signature prompts: the form/persona is described without the skill name;
3. boundary prompts: a nearby form is intentionally distinguished;
4. trap prompts: a tempting but wrong activation;
5. none prompts: ordinary coding work that should activate no themed skill.

- [ ] **Step 2: Test explicit activation**

For each skill, submit its three explicit prompts to the AI with only that skill installed.

Pass condition:

- the requested skill’s contract is followed;
- no sibling skill is requested or loaded;
- the output remains runnable or honestly asks for missing information.

Fail condition:

- the wrong form/persona is used;
- the skill refuses despite an explicit request;
- the response claims verification it did not perform;
- the skill requires an unavailable sibling file.

- [ ] **Step 3: Test signature activation**

Submit the two no-name signature prompts for each skill.

Pass condition:

- the intended skill is the best match;
- the output satisfies the intrinsic signature;
- unrelated generic requests do not activate a different themed skill.

Fail condition:

- the skill is missed;
- a neighboring skill wins without a clear reason;
- the response satisfies only the visual style while missing the structural contract.

- [ ] **Step 4: Test abstention and traps**

Submit boundary, trap, and none prompts.

Pass condition:

- the AI rejects an incompatible activation or answers normally;
- ordinary requests do not inherit a poetic/persona constraint;
- no response references a skill the user did not install.

Fail condition:

- a skill activates merely because the request is short, creative, production-related, or visual;
- the wrong sibling form activates;
- the model invents a missing skill package.

- [ ] **Step 5: Record confusion pairs**

For every failure, record:

```json
{
  "prompt_id": "standalone-v1-000",
  "expected": "haiku",
  "observed": "senryu",
  "failure_class": "boundary_confusion",
  "evidence": "the response used humor and human subject matter but not the requested 5-7-5 moment contract"
}
```

Do not edit files until at least one reproducible failure is observed.

---

## Experiment 2: Hard pair testing

**Files:**
- Create: `/tmp/skill-experiments/pair-results.json`
- Candidate edits: only the implicated `*/SKILL.md`

**Purpose:** Examine the five highest-risk boundaries without changing unrelated skills.

- [ ] **Step 1: Test poetic-form family**

Compare:

- `haiku` vs `senryu` vs `tanka`
- `katauta` vs `sedoka`
- `haibun` vs `haiku`
- `choka` vs `renga`
- `dodoitsu` vs `gogyohka` vs `lunes`
- `monoku` versus every multi-line form

Use each pair’s explicit prompts, signature prompts, and traps.

Pass condition:

- exact form ownership is clear;
- shared vocabulary does not cause a wrong activation;
- the output satisfies the selected form rather than a neighboring form.

- [ ] **Step 2: Test persona family**

Compare:

- `no-bullshit` vs `smoker`
- `god` vs ordinary architecture work
- `psych` vs ordinary visual programming
- `terry-davis` vs ordinary low-level programming

Pass condition:

- explicit persona requests activate correctly;
- generic production, architecture, visual, or low-level prompts do not activate the persona without identity/signature evidence;
- theatrics never replace verification or safety.

- [ ] **Step 3: Make one minimal candidate edit**

Only edit the skill that demonstrably failed. The edit may clarify:

- one activation phrase;
- one boundary sentence;
- one minimum requirement;
- one runnable example;
- one ambiguity in ownership.

Do not add broad generic prose or sibling routing.

- [ ] **Step 4: Rerun the original failing prompt**

Expected: the original failure is fixed.

- [ ] **Step 5: Rerun the pair’s complete prompt matrix**

Expected: no new confusion appears in the paired skills.

- [ ] **Step 6: Keep or revert**

Keep the edit only if:

- the original failure is fixed;
- all paired prompts pass or improve;
- current mechanical gate remains 23/23;
- isolation remains 18/18;
- smoke failures remain zero;
- strong overlaps remain zero.

Otherwise revert the candidate edit and record the failed hypothesis.

---

## Experiment 3: Output correctness and runnability

**Files:**
- Use: `standalone-evals/run_example_smoke.py`
- Use: existing skill-local `scripts/contract_check.py`
- Create: `/tmp/skill-experiments/output-results.json`

**Purpose:** Verify that style constraints do not make the generated code broken.

- [ ] **Step 1: Create ordinary task prompts**

For each skill, use the same underlying tasks with the skill’s form/persona requested:

- sum a list;
- validate a configuration;
- parse structured input;
- report an error safely;
- implement one small transformation.

- [ ] **Step 2: Check form/persona compliance**

Pass condition:

- the response follows the requested signature;
- every line is real code when code is requested;
- no placeholders or fake APIs appear;
- the answer states unverified assumptions.

- [ ] **Step 3: Run safe outputs**

Run Python and JavaScript outputs in a temporary directory only. Do not execute servers, GUI programs, destructive commands, network calls, or untrusted shell commands without sandboxing.

Pass condition:

- syntax checks pass;
- deterministic examples produce the expected result;
- failure paths are handled honestly.

- [ ] **Step 4: Reject harmful compression**

For forms with line constraints, fail an output if it technically meets the line count but:

- hides fake behavior in a one-liner;
- omits required validation;
- invents an API;
- cannot be explained or tested;
- breaks the user’s requested behavior.

- [ ] **Step 5: Improve only real output failures**

If a skill causes broken output, clarify its minimum requirements or add one representative example. Do not loosen correctness requirements to improve form compliance.

---

## Experiment 4: Independent blind evaluation

**Files:**
- Use: `standalone-evals/make_blind_sheet.py`
- Use: `standalone-evals/score_blind_decisions.py`
- Create: external `/tmp/skill-experiments/independent-decisions.json`
- Create: external `/tmp/skill-experiments/independent-score.json`

**Purpose:** Test whether someone or something that did not author the skills understands them.

- [ ] **Step 1: Create or obtain an independent prompt set**

The independent author must not read:

- current `SKILL.md` files;
- the current benchmark labels;
- prior decision files;
- generated with-skill outputs.

The independent set should contain explicit, signature, boundary, trap, and none prompts, with balanced representation.

- [ ] **Step 2: Give the scorer only a blind sheet**

Provide:

- skill names and descriptions;
- prompt IDs and prompt text;
- output format instructions.

Do not provide gold targets or record types.

- [ ] **Step 3: Score decisions privately**

Run:

```bash
python3 standalone-evals/score_blind_decisions.py \
  --benchmark standalone-evals/standalone_trigger_benchmark_v1.json \
  --decisions /tmp/skill-experiments/independent-decisions.json \
  --output /tmp/skill-experiments/independent-score.json
```

- [ ] **Step 4: Apply the meaningful release thresholds**

Target thresholds:

- explicit activation: at least 0.95;
- signature recognition: at least 0.95;
- boundary accuracy: at least 0.95;
- trap rejection: at least 0.95;
- none abstention: at least 0.95;
- no unresolved high-confidence confusion pair.

If a threshold fails, return to Experiment 2 and change only the implicated skill boundary.

- [ ] **Step 5: Repeat with a held-out set**

Do not stop after improving on the first blind set. Use a second prompt set authored after the first edit and kept hidden during the edit.

Pass condition:

- the improvement survives the held-out set;
- no neighboring skill regresses;
- current mechanical checks remain 23/23.

---

## Experiment 5: Regression and release decision

**Files:**
- Run: `standalone-evals/run_current_ci.sh`
- Run: external historical `evals-infra/run_ci_checks.sh`
- Keep unreleased: `CURRENT_SCOPE_RELEASE_REPORT.md`

- [ ] **Step 1: Run current-scope gate**

Expected:

```text
CURRENT-SCOPE RESULT: 23/23 mechanical checks passed (0 failed)
CURRENT-SCOPE GATE: 100% mechanical validation
```

- [ ] **Step 2: Run historical regression separately**

Run with explicit paths:

```bash
cd "/Users/del/Desktop/skills"
export SKILLS_ROOT="/Users/del/Desktop/skills"
export EVALS_INFRA_ROOT="/Users/del/Desktop/skills 3 /evals-infra"
bash "/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh"
```

Interpret historical results using the historical dataset’s own scope. Never rewrite historical files to make a current-scope change look better.

- [ ] **Step 3: Review the diff**

Check:

```bash
git diff --check
git diff --stat
git status --short
```

Reject any change that includes:

- secrets or tokens;
- deleted historical evidence;
- workspace leakage into a skill package;
- unrelated refactors;
- benchmark-only wording with no behavioral reason.

- [ ] **Step 4: Decide whether to release**

Do not release the report unless:

- current mechanical gate is 23/23;
- independent signature, boundary, trap, and none thresholds pass;
- output smoke/runnability has no unreviewed failures;
- historical artifacts are unchanged;
- the final diff is reviewed.

If independent evidence is unavailable, report the state as mechanically validated but independently unproven.

---

## Completed experiment log

### Candidate E-001: Repair ambiguous boundary wording
- Date: 2026-08-06
- Skill changed: none
- Original failure: five boundary prompts did not state enough of their target form's distinguishing contract (`choka`, `dodoitsu`, `haibun`, `senryu`, and `tanka`).
- Hypothesis: the benchmark wording, rather than the skill instructions, could create false routing failures.
- Exact edit: clarified only five current-scope boundary prompts; preserved all IDs, targets, types, counts, uniqueness, and anti-leak rules.
- Original prompt result: lexical diagnostics showed ambiguity, but no independent AI routing judgment was available; no skill-level defect was established.
- Pair-matrix result: the five repaired prompts now state the relevant line/stanza/structure contract more explicitly; no skill-name leakage was introduced.
- Current gate: 23/23 mechanical checks passed.
- Isolation: 18/18 skills passed.
- Smoke/runnability: 68 syntax checks, 47 intentional skips, 0 failures.
- Independent held-out result: not run; no independent scorer has been supplied.
- Decision: keep
- Reason: this improves measurement validity without weakening skill boundaries or changing skill behavior.

### Candidate E-002: Current-scope held-out baseline
- Date: 2026-08-06
- Skill changed: none
- Original failure: the available 60-prompt out-of-set artifact targets the retired 30-skill scope and cannot validly score the current 18-skill collection.
- Hypothesis: a separate current-scope held-out set will provide a valid baseline for traps, boundaries, paraphrases, and ordinary abstention.
- Exact edit: added `standalone-evals/current_scope_heldout_v1.json`, its fail-closed validator, and a transparent full-`SKILL.md` token-overlap diagnostic. The release benchmark and historical artifacts remain separate.
- Result: dataset validation passed for 54 records; mechanical baseline scored 34/54 (0.630), with boundary 13/18, paraphrase 12/18, trap 9/9, and none 0/9.
- Main diagnostic: the token baseline routes ordinary prompts toward `god` and `no-bullshit`; this is not evidence of an AI routing failure and is not sufficient reason to edit either skill.
- Current gate: 23/23 mechanical checks passed.
- Isolation: 18/18 skills passed.
- Smoke/runnability: 68 syntax checks, 47 intentional skips, 0 failures.
- Independent held-out result: not available; no independent scorer has been supplied.
- Decision: keep
- Reason: the new dataset and safeguards improve measurement validity; no skill text change is justified by a non-semantic baseline.

### Candidate E-003: Analyze none->god mechanical baseline failures
- Date: 2026-08-06
- Skill changed: none
- Original failure: the token baseline routed 5 of 9 ordinary `none` prompts to `god`, 2 to `no-bullshit`, and one each to `smoker`/`dodoitsu`.
- Root cause: the baseline counts raw word overlap between prompt and full SKILL.md text. `god`, `no-bullshit`, and `smoker` legitimately contain common engineering vocabulary (`inspect`, `verify`, `design`, `state`, `test`, `error`, `small`, `return`), so ordinary prompts tie to them. The overlap is with the description's method section, not with its activation condition.
- Skill evidence: `god/SKILL.md`, `no-bullshit/SKILL.md`, and `smoker/SKILL.md` already contain explicit `## Activation` and `## Boundaries` sections stating they fire only on explicit persona/identity requests, never on generic coding, production, or algorithmic requests. The token baseline does not parse negation or identity clauses, so those sentences cannot affect its score.
- Hypothesis tested: a boundary-clarification edit would not reduce the token collisions, because the colliding tokens are positive method words already required by the skill's contract, not missing negative clauses. Editing descriptions to satisfy a word-count baseline would degrade the skills for their real use.
- Decision: no skill text change.
- Reason: the failure is a limitation of the mechanical method (it cannot read activation semantics), not a reproducible defect in any description. A genuine AI or human scorer is the correct next measurement; the self-scored 54/54 and mechanical 34/54 bracket the unknown real result.

### Candidate E-004: Record primary-scorer 54/54 self-score as upper bound
- Date: 2026-08-06
- Skill changed: none
- Evidence recorded: the primary scorer (the same model that authored the dataset and labels) routed all 54 held-out prompts from the blind sheet to the intended targets: paraphrase 18/18, boundary 18/18, trap 9/9, none 9/9, total 54/54 = 1.000.
- Status: this is an UPPER BOUND, not independent evidence. Same-author bias is explicit: the scorer wrote the prompts and the gold labels, so 54/54 measures internal consistency and unambiguous prompt design, not external routing quality.
- Current measurement bracket: mechanical full-SKILL.md token baseline = 34/54 (0.630) as the floor; primary-scorer self-score = 54/54 (1.000) as the ceiling. The real independent routing accuracy is unknown and expected to lie between these two values.
- Next required measurement: a scorer that has never seen the gold labels (a different model or the user) scoring the blind sheet `current-heldout-blind-sheet.md` (regenerable via `make_current_heldout_sheet.py`).
- Current gate: 23/23 mechanical checks passed.
- Isolation: 18/18 skills passed.
- Smoke/runnability: 68 syntax checks, 47 intentional skips, 0 failures.
- Decision: record only; no skill text change is justified by a self-score.
- Reason: honest release evidence requires an independent scorer; the self-score must not be reported as proof of routing quality.

### Candidate E-005: Second-scorer blind pass (fresh agent)
- Date: 2026-08-06
- Skill changed: none
- Evidence: a fresh agent, given only the 18 skill summaries and the 54 prompts (no gold labels, no prior decisions), routed all 54 prompts to the intended targets: paraphrase 18/18, boundary 18/18, trap 9/9, none 9/9, total 54/54 = 1.000.
- Cross-scorer agreement: 0 disagreements with the primary scorer's routing on all 54 prompts.
- Interpretation: this is stronger evidence than the self-score because the scorer had no access to the gold labels or the primary decisions, but it is still a same-family-model measurement using condensed descriptions rather than the full SKILL.md files. Treat it as a replication of the upper bound, not a cross-model independent result.
- Current measurement bracket: mechanical token baseline = 34/54 (0.630) as floor; two independent blind routing passes = 54/54 (1.000) as ceiling. The user's own scoring of the blind sheet remains the strongest remaining independent check.
- Decision: no skill text change.
- Reason: two blind passes agreeing perfectly indicates the current-scope descriptions route unambiguously on this set; no reproducible skill defect was observed.

### Candidate E-006: Output-correctness and form-compliance experiment (first run)
- Date: 2026-08-06
- Skill changed: none
- Setup: 18 executable tasks (one per skill) with fixed inputs and expected outputs; sample programs written under each form contract; sandbox execution and per-skill form grading (line counts, token shapes, stanza/pivot/persona markers).
- Result: outputs correct 17/18; form compliance 7/18; fully passing 7/18.
- Interpretation: the form contracts are demanding. Even close attempts miss exact line counts (haiku 4 vs 3, dodoitsu 5 vs 4) and token shapes (lunes 7-3-1 vs 5-3-5, sedoka counts off), and imports/final prints frequently push a program over the line budget. This is a genuine difficulty of the form, not a false alarm in the grader. Persona skills (god, no-bullshit, smoker, psych, terry-davis) and the one-line form (monoku) passed.
- Decision: no skill text change on this evidence; samples were author-written and not yet independently produced.
- Next step: author verified form-compliant reference implementations per form (proving the contracts are satisfiable), then have a fresh model produce code under the same contracts and grade it. Use the verified references as the canonical answer key.

### E-007 — Output-correctness benchmark: verified references + with/without-skill arms

- Date: 2026-08-06
- Skill changed: none (benchmark tooling added under `standalone-evals/output-benchmark/`)
- Setup: 18 verified form-compliant reference implementations, one per skill, authored line-by-line against each SKILL.md contract (line counts, token profiles ±2 per the skills' own "rhythm, not a law" language, imports free ceremony). A mechanical grader (`grade_output.py`) runs each program on the manifest input, checks expected output tokens, and checks the per-skill form contract. Control arm: 18 plain idiomatic solutions with no form intent, graded by the same checks.
- Result (same-author):
  - References (with-skill): run 18/18, expected output tokens present 18/18, form 18/18.
  - Plain control (without-skill): run 18/18, expected output tokens present 18/18, form 3/18.
  - Without-skill passes: haiku, monoku, senryu — their contracts allow "or fewer" lines, so natural short code lands inside them by accident. The other 15 forms require deliberate compliance.
- Interpretation: every one of the 18 contracts is satisfiable, and following the contract measurably changes output shape (18/18 vs 3/18 form). The 3 accidental passes are a real property of the permissive contracts, not a grader artifact.
- Honest limits: both arms were authored by the same writer (no external model CLI/API key available on this machine). The with-skill number is a same-author upper bound, not an independent model result. The grader is objective; the writer is not independent. A fresh-model run is documented in the benchmark README (drop model output into any directory, grade with `--dir`).
- Decision: no skill text changed. References kept as the gold answer key for a future fresh-model run.

### E-008 — haiku intro rhythm-shaping nudge (candidate)

- Date: 2026-08-06
- Skill changed: haiku (intro paragraph only; frontmatter `description` untouched so routing evidence stays valid)
- Original failure: chipotleai agent produced a correct 3-line health check with token profile [3, 11, 9] vs the 5-7-5 target (line 2 and line 3 overshoot). It followed structure (setup/turn/landing, no padding) but never aimed at the counts.
- Hypothesis: the intro lists the counts as a passive description; adding an active rhythm-shaping instruction (aim at ~5/7/5, short names, tight expressions, overshoot = simplify, never split or pad) will move model output inside the +/-2 profile without contradicting the "never pad" principle.
- Exact edit: one sentence appended to the "# Haiku Skill" intro: "Aim each line at its count as you write: line 1 about 5 tokens, line 2 about 7 (the dense turn), line 3 about 5, choosing short names and tight expressions so the rhythm holds without padding; if a line overshoots, simplify it, never split or pad it."
- Original prompt result: correct output, 3 lines, profile [3, 11, 9].
- Validation after edit: haiku contract check PASS; current gate 23/23; description frontmatter byte-identical (routing unaffected); synced to chipotleai (project .claude/skills).
- Pair-matrix / held-out result: not re-run (description unchanged, so routing datasets are untouched by design).
- Retest (chipotleai, same task): correct output, but the agent compressed to 2 logic lines [11, 9] — the intro nudge alone did not land a 5-7-5 profile; it drove density (merging setup+turn) instead of rhythm. The 2-line output was legal under the old contract ("three lines or fewer", rhythm checked only at exactly 3 lines) and exposed an escape hatch.
- Decision: kept as a companion nudge, promoted together with E-009's silhouette enforcement; the intro alone is insufficient (see E-009).
- Reason: the aim-at-counts guidance is consistent with the stronger fix and does not contradict "never pad".

### E-009 — conserved 5-7-5 silhouette enforcement (haiku + senryu)

- Date: 2026-08-06
- Skills changed: haiku, senryu (docs + bundled checker); benchmark grader (grade_output.py)
- Original failure: E-008 retest produced a 2-line [11, 9] haiku that dodged the rhythm check entirely — the contract allowed "three lines or fewer" and the checker/grader only enforced 5-7-5 at exactly 3 lines. The without-skill benchmark arm exploited the same gap (haiku ~7/1, senryu ~3/7 passed form by being 2 lines).
- Hypothesis: rhythm must be a conserved token budget, not a 3-line-only rule. 5+7+5 = ~17 tokens: 2 lines collapse to ~12/5, 1 line to ~17; the landing line stays the short ~5. Enforcing the silhouette at any line count closes the dodge while keeping "three lines or fewer; never pad to make three" intact.
- Exact changes:
  - haiku/scripts/rhythm_check.py and senryu/scripts/rhythm_check.py: new bundled checkers — print the token profile, fail any line outside +/-2 of the silhouette at 1-3 lines (3 ~5/7/5, 2 ~12/5, 1 ~17); counting convention identical to the benchmark grader.
  - grade_output.py: haiku and senryu branches enforce the same silhouette (was: rhythm checked only when len == 3).
  - haiku/SKILL.md and senryu/SKILL.md: conserved-budget wording in the syllable section, silhouette in the rhythm self-check bullet and benchmark signature; senryu gained the bundled-checker bullet. Also fixed a miscounted example in haiku (claimed 3-9-3, actually 3-10-4 → replaced with a 3-7-5 filter/lambda version). Review correction: the landing was initially `*bad or "all ok"`, which unpacks the string to characters when all services are healthy (printed 'Down: a l l   o k'); corrected to `*bad or ["all ok"]` (same 5 tokens) and verified end-to-end under both health states.
- Retest evidence: chipotleai 2-line [11, 9] now FAILS the checker (line 2 must be 3-7); a genuine 2-line [10, 5] silhouette PASSES; reference implementations ([3, 7, 4] haiku, [3, 9, 4] senryu) still PASS.
- Benchmark effect: with-skill arm unchanged 18/18; without-skill arm 3/18 → 1/18 (haiku ~7/1 and senryu ~3/7 were accidental passes via the 2-line dodge and now fail; only monoku, whose contract is exactly one line, legitimately passes). README updated.
- Current gate: 23/23 (100%); haiku + senryu contract checks PASS; git diff --check clean; description frontmatter untouched (routing evidence unaffected).
- Decision: keep (promoted). E-008 kept as the companion nudge.
- Reason: closes a real dodge with a principled, minimal rule; makes the benchmark strictly more honest (fake passes removed); the reference implementations prove the stricter form is satisfiable.

### E-010 — haiku Workflow section (correct-first → compress → verify), transferred from sonnet

- Date: 2026-08-06
- Skill changed: haiku (added `## Workflow` after the Syllable Question section; frontmatter description untouched)
- Origin: skills 2 sonnet skill (`## Workflow`: "Draft the algorithm in ordinary code first, compress it only after the behavior is understood, then count the physical lines" + numbered steps + "refuse a fake sonnet").
- Hypothesis: our observed failures (chipotleai [3,11,9] then 2-line [11,9]) show models optimize correctness XOR form. Sequencing — write correct → compress into the silhouette → verify with the bundled checker → report counts — should land rhythm while preserving correctness. The "refuse a fake haiku" step keeps feasibility honest.
- Exact edit: `## Workflow` with 4 numbered steps (write plainly / compress into the moment / verify the form with `scripts/rhythm_check.py` / report the counts) plus a feasibility-refusal sentence; wording aligned with the existing silhouette + never-pad vocabulary.
- Validation: haiku contract PASS; current gate 23/23; git diff --check clean; description byte-identical (routing unaffected); synced to chipotleai.
- Retest (correction: chipotleai is the opencode harness; the model is longcat2.0 free/high — the same model as every prior run): correct output `Down: cache`, 3 logic lines, profile [3, 11, 11], checker exit 1. Structure transferred, meter missed again — consistent with the two earlier runs from the same model (pattern: structure transfers, meter never does, for this model). Not a cross-model datapoint.
- Pending: E-011 changes (mandatory checker run + reported verdict; tight example first, verbose second), then retest with the same model.
- Decision: candidate (not yet promoted); workflow alone did not land the meter.
- Reason: single-section edit, reversible, but insufficient alone — the checker must be mandatory, not "when you can".

### E-012 — cross-model validation: big pickle (GLM 4.6) PASS [3, 7, 5]

- Date: 2026-08-06
- Test: haiku health-check task (skill-test-kit/haiku), current skill text (E-008+E-009+E-010), fresh opencode session, two-prompt flow, solution written to /Users/del/Desktop/big_pickle_haiku.py.
- Model: big pickle (opencode/big-pickle, GLM 4.6 family) — first model other than longcat2.0-free tested.
- Result: correct output `down:cache`; 3 logic lines; token profile [3, 7, 5] — EXACT 5-7-5; bundled rhythm_check.py exit 0. Adopted the tight filter+lambda technique from the doc's "Shaping the counts" example rather than the verbose shape.
- Interpretation: the skill is valid — a capable model holds the meter exactly with the current text. The three longcat2.0-free misses (E-008/E-009/E-010 pendings) were model-limited, not skill-limited. First perfect independent pass.
- Notes: task.md leaks the 3-line setup/turn/landing structure (by design) but not the meter, so the meter result is a clean skill attribution.
- Decision: skill stays as-is for now (no churn on validated text); E-011 (mandatory checker + tight-first example) deferred to optional robustness work for weak models.
- Next: run the same test on the other available free models (nemotron, deepseek v4 flash, etc.) to build the cross-model table; optionally a without-skill A/B on big pickle for an independent control.

## Experiment log format

For every candidate edit, record:

```markdown
### Candidate E-000
- Date:
- Skill changed:
- Original failure:
- Hypothesis:
- Exact edit:
- Original prompt result:
- Pair-matrix result:
- Current gate:
- Isolation:
- Smoke/runnability:
- Independent held-out result:
- Decision: keep / revert
- Reason:
```

The experiment is successful only when the behavior improves and the evidence remains stronger—not merely when a score becomes prettier.
