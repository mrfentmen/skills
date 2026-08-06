# Output-correctness benchmark (E-007)

Measures the skills' real effect on **generated code**: does following a skill's
form contract produce code that (a) runs, (b) answers the task correctly, and
(c) actually carries the skill's form? This is separate from routing evals —
routing asks *which* skill fires; this asks whether the skill's output shape
holds up.

## Files

- `e3-manifest.json` — 13 executable tasks, one per skill (id, task, stdin
  input, expected output tokens).
- `references/<skill>.py` — verified, form-compliant reference implementations.
  These are the **gold set**: they prove every one of the 13 contracts is
  satisfiable and define what compliant output looks like.
- `without_skill/<skill>.py` — plain idiomatic solutions to the same tasks with
  no form intent (the control arm).
- `grade_output.py` — mechanical grader: runs each program on the manifest
  input, checks expected output tokens are present, and checks the per-skill
  form contract (line counts, token profiles ±2 per the skills' own
  "rhythm, not law" language, couplet/stanza structure, persona markers).
  `haiku` and `senryu` enforce the conserved 5-7-5 silhouette at any line
  count (3 lines ~5/7/5, 2 lines ~12/5, 1 line ~17), so fewer lines can
  never dodge the rhythm.

## Run it

```bash
cd standalone-evals/output-benchmark
python3 grade_output.py --dir references     # gold set
python3 grade_output.py --dir without_skill  # control arm
python3 grade_output.py --dir /path/to/fresh_model_outputs  # any new arm
```

Drop any directory of `<skill>.py` files in and grade it with the same form
checks.

## Results (2026-08-06, same-author)

| Arm | Run | Expected output tokens present | Form compliance |
|---|---|---|---|
| With skill (contract-following) | 13/13 | 13/13 | **13/13** |
| Without skill (plain idiomatic) | 13/13 | 13/13 | **1/13** |

"Expected output tokens present" means every expected token is in the output
and no unexpected **numbers** appear (extra words are allowed; extra numbers
fail).

The only without-skill pass is `monoku` — its contract is exactly one line, so
natural short code lands inside it. `haiku` and `senryu` look permissive
("three lines or fewer") but their rhythm silhouette is enforced at any line
count (3 lines ~5/7/5, 2 lines ~12/5, 1 line ~17), so plain 2-line code
(which reads ~7/1 or ~3/7, not ~12/5) no longer passes by accident. The other
**12 forms require deliberate compliance**: plain code never produces a 7-7-5
dodoitsu settlement, a 5-3-5 lune hinge, a 3-stanza renga alternation, a
closing 7-7 choka couplet, or the inspect/plan/verify discipline of
no-bullshit and smoker.

## Honest limits

- **Current status: the genuinely independent run is still pending.** Both
  arms below were authored by the same writer — no external model CLI or API
  key was available on this machine. The with-skill number is a **same-author
  upper bound**, not an independent model result; the without-skill number is
  the same-author control. The mechanical grader is objective, but the writer
  is not independent. Running the real benchmark only needs an API key (see
  below).
- Token profiles are checked with ±2 tolerance and imports count as free
  ceremony, exactly as the SKILL.md contracts specify ("rhythm, not a law;
  never pad to hit a count").
- The references are one valid implementation each, not the only one. The
  point is satisfiability and gradeability, not canonical output.

## Getting a genuinely independent number

To run the real with-skill vs without-skill benchmark with a fresh model:
give the model (1) the full `SKILL.md` for the skill plus the manifest task
(with-skill arm), or (2) the bare task only (without-skill arm), collect the
programs into two directories, and grade both with `grade_output.py --dir …`.
The delta between the arms is the skill's measurable effect on output shape.
