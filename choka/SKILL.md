---
name: choka
description: >-
  Write runnable code in a choka form: a multi-line program with alternating short and long logic lines and a final 7-7 closing couplet that resolves the computation. Activate only for an explicit choka, long metered verse, or alternating-line program request.
---
# Choka Skill

A choka is the long poem of the Japanese tradition: alternating 5-7-5-7-5-7 lines flowing on and on, ending with a 7-7 couplet that closes the song. A code choka is a longer program, six, ten, twenty lines, that keeps the family's verse discipline: short line, long line, short line, and a heavy closing couplet that lands the result.

## Philosophy

"The choka is the haiku that grew up and got a job. It still breathes in 5s and 7s, but it has the room to do real work, and it must end with a couplet that makes the whole journey land."

The choka mindset:
1. **Long form**: 6+ lines of logic, for tasks that need steps, phases, or a pipeline too big for the short forms
2. **Alternating rhythm**: short lines ~5 tokens, long lines ~7 tokens, alternating (5-7-5-7-5-7...), the code analog of the ancient meter
3. **The closing couplet (7-7)**: the final two lines are the landing, the result, the summary, the moment the whole poem was walking toward. Without a strong closing couplet there is no choka, just a long poem.
4. **Each line does real work**: no filler lines to pad the count, every line is a step the task needed
5. **Actually runs**: a choka that doesn't run is an epic of broken promises

## Structure

```
line 1   ~5 tokens   the first step (short)
line 2   ~7 tokens   the second step (long)
line 3   ~5 tokens   the third step
line 4   ~7 tokens   ...
...
line n-1 ~7 tokens   the second-to-last step (long)
line n   ~7 tokens   THE CLOSING COUPLET: the result lands here
```

The last two lines are the couplet: both ~7 tokens, together they state the outcome. The poem may open short and close long, the alternating meter is a rhythm, not a law: ±2 slack, and a step may be two short lines where the rhythm needs a breath.

## Core Patterns

### The Summation Choka
A long-breathing count that opens short and closes on the couplet:

```python
all_nums = input().split()
nums = [int(x) for x in all_nums]
total = sum(nums)
count = len(nums); print("count", count)
print("count", count, "of", "them", "in", "all")
print("sum", total, "is", "their", "total")
```

### The Game-Loop Choka
A simulation with a beginning, a middle, and a landing:

```python
import random
pos, steps, total = 0, 0, 0
while -3 < pos < 3 and steps < 50:
    pos += random.choice((-1, 1))  # one random step
    steps += 1
    total += pos
print("escaped", "at", steps, "steps", "now")
print("or", "still", "walking", "after", steps)
```

### The Long Computation Choka
When the task genuinely needs many steps, meter them all:

```python
import math, sys
n = int(sys.argv[1])
sieve = [True] * (n + 1)
for p in range(2, int(math.isqrt(n)) + 1):
    if sieve[p]:
        for m in range(p * p, n + 1, p):
            sieve[m] = False
primes = [i for i in range(2, n + 1) if sieve[i]]
print("primes", len(primes), "under", n, "now")
print("and", "the", "sieve", "holds", "true")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the choka form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

## Template-first construction

Do not invent a choka from a blank page. Start by copying the first passing Python example in this skill, then adapt its slots to the user's task:

**Output contract:** print exactly the numbers the example prints (here the count and the sum) and nothing else — do not add a mean, average, or range; the output check compares the exact number set on every input.

1. Preserve the long-breathing line count (at least six logic lines) and the closing couplet: the last two logic lines must both be ~7 tokens (±2).
2. The common trap is writing the closing lines too short — `print("count", count)` is only 3 tokens. A ~7-token couplet line needs real content: `print("count", count, "of", "them", "in", "all")` (7). The couplet states the outcome with weight.
3. Alternate the meter: no run of three consecutive lines all under 5 or all over 7 tokens. Intersperse a short line and a longer line.
4. Replace the example's data handling with the real task work; never leave poetic filler, dead assignments, or fake output.
5. After every edit, run the program for the requested input, then run `scripts/rhythm_check.py solve.py`. Fix only the flagged line by reshaping its real expression — a 1-3 token line gets real content, never a filler statement.

This copy-then-adapt method is intentional: it preserves a known-valid alternating shape and the ~7-7 closing couplet while leaving the computation task-specific.


## Counting Tokens (the exact procedure)

The rhythm is the number of whitespace-separated groups per logic line: exactly what `len(line.split())` returns, exactly what `scripts/rhythm_check.py` counts. Count mechanically, not by feel:

1. **Split on spaces.** Each space-separated group is one token. `x = 1` is 3 tokens (`x`, `=`, `1`); `x=1` is 1 token.
2. **Brackets and parens glue when there is no space.** `sum(nums)` is 1 token; `sum(nums) / len(nums)` is 3; `[int(x) for x in data]` is 5 (`[int(x)`, `for`, `x`, `in`, `data]`).
3. **A space inside a call or a string splits.** `print("a", b)` is 2 tokens (`print("a",`, `b)`); `"two words"` is 2 tokens.
4. **Inline comments count; full-line comments and imports are free.** `total = sum(data)  # the total sum` is 7 tokens.
5. **Names are always one token.** `total = x` and `t = x` are both 3 tokens. Renaming never changes the count; the budget is changed by expression shape, not word length.

Adjust honestly:

- **Under the target:** grow a real step, never a filler statement. `sum(data)` (1 token) becomes `sum(data) / len(data)` (3), then a print that must happen anyway can carry more real words. A comprehension is worth 5-7 tokens of real work.
- **Over the target:** shrink real steps. Drop words from prints that only narrate, prefer `f(a,b)` over `f(a, b)`, replace a spread-out expression with a tighter one. Remove nothing the task needs.
- **Never pad:** no dead assignments, no `* 1`, no placeholder statements, no splitting one line into two to reach a count. A line carrying real work at the wrong count is fixed by reshaping it, not by faking it.

After adjusting, run `scripts/rhythm_check.py solve.py`; it prints the profile line by line. Within tolerance is a pass; off by more means reshape that line only.

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following:

- at least 6 lines of code that carry logic (ceremony like `fn main()` is free)
- lines alternate short/long: ~5 tokens on short lines, ~7 on long lines (rhythm, ±2 slack, never padded)
- the FINAL TWO lines are the closing couplet: both ~7 tokens, together they state the result
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`
- the program actually runs and produces the correct result
- every line is a real step the task needed, no filler lines
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the visible logic-line profile against alternating `[5, 7, 5, 7, 5, 7, 7, 7]` with ±2 tolerance and retain the independent closing-couplet check; do not pad to improve a diagnostic.

## Boundaries

This skill is not for generic code that happens to use several lines, generic brevity, or an ordinary multi-step script. Without an explicit choka request or its alternating-line-and-closing-couplet contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names choka or requests alternating long verse with a closing couplet. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Choka Aesthetic

Write code that:
- is long but never lazy, every line earns its place
- breathes in the family rhythm: short, long, short, long
- builds toward a closing couplet that makes the whole journey land
- names the steps so the poem reads top to bottom as a story

## Cross-Language Examples

```javascript
// 5: the file awaits
const raw = fs.readFileSync("data.txt", "utf8");
// 7: the words arrive
const lines = raw.split("\n").filter(Boolean);
// 5: the rows stand
const nums = lines.map(Number);
// 5: the numbers form
const total = nums.reduce((a, b) => a + b, 0);
// 7: the center holds
const mean = total / nums.length;
// 7: the couplet
console.log(`mean ${mean.toFixed(2)} over ${nums.length} rows`);
```

```bash
#!/bin/bash
# 5: the tally begins
total=0; count=0
# 5: each number arrives
while read -r n; do
# 7: the sum and its count
total=$((total + n)); count=$((count + 1))
# 5: the stream ends
done < nums.txt
# 5: the tally holds
echo "the tally: $count lines"
# 7: the couplet
printf "sum=%s over %s numbers" "$total" "$count"
```

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
