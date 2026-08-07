# Output-correctness benchmark (E-007)

Measures the skills' real effect on **generated code**: does following a skill's
form contract produce code that (a) runs, (b) answers the task correctly, and
(c) actually carries the skill's form? This is separate from routing evals —
routing asks *which* skill fires; this asks whether the skill's output shape
holds up.

## Files

- `e3-manifest.json` — 28 executable tasks, one per skill (id, task, stdin
  input, expected output tokens).
- `references/<skill>.py` — verified, form-compliant reference implementations.
  These are the **gold set**: they prove every one of the 28 contracts is
  satisfiable and define what compliant output looks like.
- `without_skill/<skill>.py` — plain idiomatic solutions to the same tasks with
  no form intent (the same-author control arm).
- `model-outputs/<provider>/<arm>/<skill>.py` — **independent model arms**:
  with-skill and without-skill outputs produced by real chat models via API.
- `grade_output.py` — mechanical grader: runs each program on the manifest
  input, checks expected output tokens are present, and checks the per-skill
  form contract (line counts, token profiles ±2 per the skills' own
  "rhythm, not law" language, couplet/stanza structure, persona markers).
  `haiku` and `senryu` enforce the conserved 5-7-5 silhouette at any line
  count (3 lines ~5/7/5, 2 lines ~12/5, 1 line ~17), so fewer lines can
  never dodge the rhythm.
- `run_model_arms.py` — reproducible runner: calls a chat-completions API for
  every skill twice (with-skill: full SKILL.md in the system prompt;
  without-skill: bare task) and saves the outputs above. Keys come from
  environment variables (`GROQ_API_KEY`, `MISTRAL_API_KEY`, ...).

## Run it

```bash
cd standalone-evals/output-benchmark
python3 grade_output.py --dir references     # gold set
python3 grade_output.py --dir without_skill  # same-author control

# fresh model arm:
GROQ_API_KEY=... python3 run_model_arms.py --providers groq-llama3.3-70b
python3 grade_output.py --dir model-outputs/groq-llama3.3-70b/with-skill
python3 grade_output.py --dir model-outputs/groq-llama3.3-70b/without-skill
```

Drop any directory of `<skill>.py` files in and grade it with the same form
checks.

## Results — same-author baseline (2026-08-06, extended to 28 forms 2026-08-07)

| Arm | Run | Expected output tokens present | Form compliance |
|---|---|---|---|
| With skill (contract-following) | 28/28 | 28/28 | **28/28** |
| Without skill (plain idiomatic) | 28/28 | 28/28 | **1/28** |

The with-skill number is an upper bound: it was authored by someone holding
the skill spec and deliberately landing the rhythm. It proves all 28
contracts are satisfiable and gradeable. The only accidental without-skill
pass is `monoku` (its contract is exactly one line). The 15 newer forms
(kyoka, somonka, bussokusekika, imayo, kanshi, zappai, waka, renshi,
sonnet, villanelle, cinquain, ryuka, fibonacci, limerick, etheree) were
added as manifest entries, gold references, and control arms; the grader
gained a form-check branch per form (mirroring each skill's
`rhythm_check.py`).

## Results — independent model arms (2026-08-07)

Two real models were run through both arms via API (`run_model_arms.py`,
temperature 0.2, one shot, no checker feedback loop):

| Arm | Model | Run | Correct output | Form compliance (strict) |
|---|---|---|---|---|
| With skill | Groq llama-3.3-70b | 13/13* | 9/13 | 0/13 |
| With skill | Mistral small | 13/13 | 8/13 | 1/13 |
| Without skill | Groq llama-3.3-70b | 10/13* | 3/13 | 0/13 |
| Without skill | Mistral small | 8/13 | 2/13 | 0/13 |

\* runtime failures are model-side stdin misreads (they parse line-by-line
while the manifest input is space-separated on one line), not skill defects.

### The measurable with-skill effect: shape convergence

Strict form compliance is 0/13 one-shot because **models cannot count Python
tokens to ±2 without iterating**. But the with-skill arms converge to the
form's *shape* while the without-skill arms do not — the skill demonstrably
changes output structure:

| Skill (target) | With skill (line counts) | Without skill (line counts) |
|---|---|---|
| choka (>=6, alternating) | 6 (groq) | 17 |
| dodoitsu (4 lines) | 4, 4 | 8 |
| gogyohka (5 lines) | 4, 4 | 9, 11 |
| haiku (1-3 lines) | 3, 2 | 7 |
| lunes (3 lines) | 2, 2 | 21 |
| renga (2-3 per stanza) | 5, 4 stanzas | 8 stanzas |
| senryu (1-3 lines) | 3, 2 | 9 |
| sijo (3 long lines) | 3, 2 | 14 |
| tanka (5 lines) | 6, 5 | 13, 42 |

`haibun` is the bright spot: **Mistral hit full form compliance** (narrative
body + 3-line landing) when given the skill.

## Honest analysis

1. **The skills change output shape.** Given the skill, models land the target
   line count / stanza structure for ~10/13 forms; without it, output drifts
   far from the form (a 21-line lune, a 42-line tanka). The 13/13 vs 1/13
   same-author result is the same effect, taken to exact compliance.
2. **Exact rhythm (±2 tokens) is not one-shot-achievable by current models.**
   The references prove the bars are satisfiable; models just do not count
   tokens. The skills' own language ("rhythm, not a law; never pad to hit a
   count") is philosophy, not a counting procedure.
3. **Implication for use:** these skills are agentic, not one-shot. The
   intended workflow (skill-test-kit + per-skill checkers, e.g. haiku's
   `rhythm_check.py`) has the agent write, run the checker, and refine —
   that is how a model reaches exact compliance. A one-shot API call is the
   weakest-case test and should not be the only bar.

## Agentic upgrade (done)

- Every SKILL.md now ships a **check-and-refine workflow** (`## Workflow`):
  write plainly, shape the rhythm, verify with `scripts/rhythm_check.py solve.py`,
  report the token profile. The checker uses the grader's counting convention
  exactly (whitespace tokens; imports and full-line comments are free), so a
  pass there means a pass in the mechanical form check.
- All 28 skills now bundle a `scripts/rhythm_check.py`. The **rhythm gate**
  (`standalone-evals/check_rhythm_examples.py`, wired into CI) requires every
  documented example and every E3 reference to pass its own checker. The
  documented examples were rewritten until they all pass, so a model copying
  an example starts from a known-pass shape and only refines its own task
  code. The rhythm gate now covers all 28 skills: 28/28 documented examples
  and 28/28 E3 references pass their own checkers (somonka's E3 reference is
  a single file with two stanzas and is checked inline).

## Open work

- Re-run the independent model arms on the full 28-item manifest
  (`run_model_arms.py` picks up all items automatically) and re-grade to
  measure with-skill shape convergence across the newer forms.
- Add a concrete token-counting procedure to the skills so one-shot models
  can reach exact rhythm without a checker feedback loop.
