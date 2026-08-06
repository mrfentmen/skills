---
name: choka
description: >-
  Write code as a choka: the long form of the haiku family - a program of 6 or more lines
  alternating short and long (5-7-5-7-5-7...) and ending with a heavy 7-7 closing couplet
  that lands the result. Use this skill when the user wants a LONGER poem-shaped program
  that still follows strict verse rhythm, a task too big for 3-5 lines but too small for
  prose, or a step-by-step algorithm metered like the ancient long poems. Make sure to use
  this skill whenever the user mentions choka, long verse, alternating line rhythm, or
  wants a multi-step program shaped as a poem with a strong closing couplet. This skill is
  NOT for 3-line forms (use haiku, senryu, lunes, katauta, or sijo), NOT for 5-line forms
  (use tanka or gogyohka), NOT for 4-line folk forms (use dodoitsu), NOT for prose-with-
  verse (use haibun), NOT for linked chains of stanzas (use renga), and NOT for one-line
  programs (use monoku).
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

### The Pipeline Choka
A multi-step transformation, metered:

```python
import json
raw = open("scores.json").read()               # 5: the raw ledger
data = json.loads(raw)                          # 7: parsed into memory
scores = [d["score"] for d in data]            # 5: the numbers alone
high = sorted(scores, reverse=True)[:3]        # 7: the elite three
low = sorted(scores)[:3]                        # 7: the forgotten three
print("top:", high, "| bottom:", low)          # 7: the couplet - the story
```

### The Game-Loop Choka
A simulation with a beginning, a middle, and a landing:

```python
import random
pos, steps, total = 0, 0, 0                    # 5: the walk begins
while -3 < pos < 3 and steps < 50:             # 7: the boundary holds
    pos += random.choice((-1, 1))              # 5: one step, random
    steps += 1                                 # 5: one step counted
    total += pos                               # 5: the path remembers
print(f"escaped at {steps} steps") if pos == 3 else print(f"still walking after {steps}")  # 7+7: the couplet
```

### The Long Computation Choka
When the task genuinely needs many steps, meter them all:

```python
import math, sys
n = int(sys.argv[1])                            # 5: the number arrives
sieve = [True] * (n + 1)                        # 7: assume all are prime
for p in range(2, int(math.isqrt(n)) + 1):     # 5: strike from two
    if sieve[p]:                                # 5: p survived the sieve
        for m in range(p * p, n + 1, p):        # 7: its multiples fall
            sieve[m] = False                    # 5: marked composite
primes = [i for i in range(2, n + 1) if sieve[i]]  # 7: the survivors line up
print(f"{len(primes)} primes under {n}")        # 7: the couplet - the census
```

## Boundaries, when NOT to use this skill

- 3-line moments, kigo, short and dense -> haiku
- 3-line humor punchlines -> senryu
- the 5-3-5 punch form -> lunes
- the 5-7-7 half-poem -> katauta
- 3-line Korean twist form -> sijo
- the whole program on one line -> monoku
- 5-line expanded forms -> tanka / gogyohka
- the 4-line folk form with a short landing -> dodoitsu
- prose body with a closing haiku -> haibun
- linked chains of independent stanzas -> renga
- long programs that are NOT metered (just long) -> no-bullshit or minimalist-zen

Choka is the long form of the family: more than six lines, alternating rhythm, and a closing couplet that lands the result.

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

## When to Use Choka Patterns

Use choka code when:
- the task has 4+ natural steps: read, parse, transform, summarize, report
- the user wants "a longer poem-shaped program" or "the long form of haiku"
- a 3-5 line solution would be cramped but a full module would be ceremony
- you want the verse discipline applied to a real multi-step computation

## The Choka Aesthetic

Write code that:
- is long but never lazy, every line earns its place
- breathes in the family rhythm: short, long, short, long
- builds toward a closing couplet that makes the whole journey land
- names the steps so the poem reads top to bottom as a story

## Cross-Language Examples

```javascript
const fs = require("fs");                       // 5: the file awaits
const text = fs.readFileSync("data.txt", "utf8");  // 7: the words arrive
const lines = text.split("\n").filter(Boolean); // 5: the rows stand
const nums = lines.map(Number);                 // 5: the numbers form
const mean = nums.reduce((a, b) => a + b, 0) / nums.length;  // 7: the center holds
console.log(`mean ${mean.toFixed(2)} over ${nums.length} rows`);  // 7+7: the couplet
```

```bash
#!/bin/bash
total=0; count=0                                # 5: the tally begins
while read -r n; do                             # 5: each number arrives
  total=$((total + n)); count=$((count + 1))    # 7: the sum and its count
done < nums.txt                                 # 5: the stream ends
echo "sum=$total over $count numbers"           # 7+7: the couplet
```

## Bundled Helpers

If the task needs ASCII output, randomness, or decorative headers, reuse the shared toolkit, a choka may import a helper on a short line and still count it as one of its steps:

- `shared/ascii_canvas.py`, ASCII canvas with lines, circles, ink-density characters
- `shared/rng.py`, seeded RNG and value noise
- `shared/box_drawing.py`, box-drawing headers
