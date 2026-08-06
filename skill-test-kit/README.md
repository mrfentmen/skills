# Skill Test Kit

Mock work for hands-on testing: **18 realistic coding tasks**, one per skill.
You load a skill into an AI agent, point it at a task folder, and check the AI's
`solve.py` against the answer key.

## The core idea

Each folder is a real-ish work item: `task.md` (the assignment), `input/` (data
the script must read), and `expected.md` (the answer key **for you** — don't
show it to the AI). The task text deliberately does **not** name the skill: the
skill is the thing being tested, so it comes from *your* instruction, not the
task file.

## How to test one skill (≈2 minutes)

1. **Load the skill into your agent.**
   - Claude Code: `cp -R /Users/del/Desktop/skills/<skill> ~/.claude/skills/`
   - Any other coding agent (or this chat): paste the contents of
     `/Users/del/Desktop/skills/<skill>/SKILL.md` into the conversation.

2. **Give the agent the task.** Say something like:

   > Use the haiku skill to complete the task in `skill-test-kit/haiku/task.md`.
   > Write `solve.py` in that folder.

   (Because the skills activate on explicit requests, naming the skill is what
   makes it fire — that's by design, not a cheat.)

3. **Run the AI's output:**
   ```bash
   cd skill-test-kit/haiku
   python3 solve.py
   ```

4. **Grade it against `expected.md`** — two parts:
   - **Correctness**: the deterministic values (e.g. "total 8, 200s 5, 404s 2")
   - **Form checklist**: the skill's shape (e.g. "≤3 lines, 5-7-5 ±2,
     setup/turn/landing") — tick the boxes.

## The honest A/B test

For each skill, run the **same task twice**: once with your instruction naming
the skill, once with the bare task only ("complete the task in
`skill-test-kit/haiku/task.md`"). Compare:

| | Correctness | Form |
|---|---|---|
| With skill | should pass | **should pass** |
| Without skill | should pass | usually fails |

The form column is the point. Plain code never produces a 7-7-7-5 dodoitsu, a
5-3-5 lune hinge, or a closing choka couplet by accident. (The forms that *can*
happen by accident — haiku, monoku, senryu — are noted in their `expected.md`.)

## The 18 tasks at a glance

| Skill | Task | Input |
|---|---|---|
| choka | log request census (long pipeline) | `access.log` |
| dodoitsu | config validator, four working lines | `app.conf` |
| god | bounded queue with invariants + verification | — |
| gogyohka | word census, five free-rhythm lines | `words.txt` |
| haibun | trip journal with poetic landing | `trip.csv` |
| haiku | service health check, three lines | `health.json` |
| katauta | directly-addressed message, 5-7-7 | `names.txt` |
| lunes | F→C conversion, 5-3-5 | `temps.txt` |
| monoku | ID filter, one physical line | `ids.txt` |
| no-bullshit | fix a naive email validator + honest report | `src/validator.py` |
| psych | 12x12 cellular automaton, 6 generations | — |
| renga | chained text pipeline in linked stanzas | `text.txt` |
| sedoka | forward/reverse sum in mirrored stanzas | `numbers.txt` |
| senryu | meeting estimate with a punchline | `minutes.txt` |
| sijo | score report with a third-line twist | `scores.csv` |
| smoker | fix a wrong overtime branch + honest report | `src/payroll.py` |
| tanka | read-time stats, result then reflection | `reads.txt` |
| terry-davis | count high-bit bytes, direct style | `bytes.bin` |

## Notes

- All inputs are deterministic and small; every `expected.md` value is
  verified against the actual data files.
- `no-bullshit` and `smoker` ship intentionally buggy `src/` files — the task
  is to fix them, so don't "fix" the data.
- You can test the same task with several different agents/models — the more
  varied the model, the stronger the evidence.
- The automated version of this idea (with a mechanical grader) lives in
  `standalone-evals/output-benchmark/`.
