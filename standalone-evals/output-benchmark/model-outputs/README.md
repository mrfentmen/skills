# Model outputs (independent evidence)

Real model outputs produced under the skills via the two-prompt test flow
(fresh session, task in `skill-test-kit/<skill>/`, skill applied in the second
message). Each subfolder is one model; each file is that model's solution for
one skill. This is the genuinely independent evidence layer the benchmark
caveats ask for - unlike `references/` (same-author gold set) and
`without_skill/` (same-author control), these were written by external models.

## Contents

| Model | Skill | Verdict |
|---|---|---|
| `big-pickle/haiku.py` | haiku | **PASS** - correct `down:cache`, 3 logic lines, exact profile [3, 7, 5], `rhythm_check.py` exit 0 |

## How to grade a model's full arm

Collect all 13 skill outputs for one model into `model-outputs/<model>/` and
grade with the same mechanical grader used for the arms:

```bash
python3 grade_output.py --dir model-outputs/<model>
```

A single file grades as 1/N while the other skills are missing; the meaningful
number appears once a full 13-skill arm is collected.

## Provenance notes for `big-pickle/haiku.py`

- Model: big pickle (opencode/big-pickle, GLM 4.6 family), opencode free/high.
- Flow: two-prompt (read task + wait; then apply the haiku skill), delivered as
  both `/Users/del/Desktop/big_pickle_haiku.py` and `skill-test-kit/haiku/solve.py`.
- The absolute input path was required by the test prompt (file lives on the
  Desktop); not a portability choice by the model.
- Known minor critiques (not contract failures): no kigo-style variable name,
  non-portable absolute path, minimal output styling (`down:cache`).
- Contrast: longcat2.0-free missed the meter 3/3 on this same task
  ([3, 11, 9], 2-line [11, 9], [3, 11, 11]).
