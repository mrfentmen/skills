---
name: dodoitsu
description: >-
  Write code as a dodoitsu: the 4-line folk form of the haiku family - three full lines of
  work (~7 tokens each) and a short landing line (~5 tokens) that settles the matter like
  the punchy last verse of a folk song. Use this skill when the user wants a complete
  working program in four lines with the weight on the first three and a quick, plain-
  spoken finish - the everyday workhorse of the poetic forms. Make sure to use this skill
  whenever the user mentions dodoitsu, four-line verse, the folk form, 7-7-7-5 rhythm, or
  wants a program with three heavy lines and a short closing line. This skill is NOT for
  3-line forms (use haiku, senryu, lunes, katauta, or sijo), NOT for 5-line forms (use
  tanka or gogyohka), NOT for long verse (use choka), NOT for one-line programs (use
  monoku), and NOT for prose-with-verse (use haibun). For the rest of the poetic family,
  use: haiku for the 5-7-5 moment, sijo for a twist ending, choka for long alternating
  verse, and renga for a linked chain of stanzas.
---
# Dodoitsu Skill

A dodoitsu is a Japanese folk poem: four lines, 7-7-7-5, three full lines of statement and one short line that settles it. It's the plain-spoken form: work, love, everyday life, said directly. A code dodoitsu is a four-line program: three lines that carry the load, one short line that lands the result.

## Philosophy

"The dodoitsu is the workhorse of the family. Haiku is a moment, sijo is a twist, choka is an epic, dodoitsu is the four-line verse that gets the job done and says it plainly at the end."

The dodoitsu mindset:
1. **Four lines, 7-7-7-5**: the first three lines are full (~7 tokens each, the work), the last line is short (~5 tokens, the landing)
2. **Weight on the front**: lines 1-3 carry the computation; the fourth line is a quick, plain statement of the result
3. **No twist required**: unlike sijo, the dodoitsu doesn't need a volta, it needs a *settlement*. The last line closes the matter plainly
4. **Plain-spoken**: folk form, no preciousness, no ornament; the language of everyday work
5. **Actually runs**: a dodoitsu that doesn't run is a folk song with no chorus

## The 7-7-7-5 Shape

```
line 1   ~7 tokens   the first load: gather or set up
line 2   ~7 tokens   the second load: transform or work
line 3   ~7 tokens   the third load: finish the heavy lifting
line 4   ~5 tokens   the landing: the result, stated plainly
```

The last line is deliberately shorter, the code analog of the dodoitsu's 5-syllable close. It should read like a verdict: short, certain, done. ±2 slack per line, never padded.

## Core Patterns

### The Folk Tally
Count, weigh, and state, the classic everyday task:

```python
lines = open("log.txt").read().splitlines()      # 7: the day's entries
errors = [l for l in lines if "ERROR" in l]      # 7: the troubles among them
warns = [l for l in lines if "WARN" in l]        # 7: the near misses too
print(f"{len(errors)} errors, {len(warns)} warns")  # 5: the settlement
```

### The Plain Average
No drama, just the number:

```python
nums = [int(x) for x in input().split()]         # 7: the numbers arrive
total = sum(nums)                                # 7: the tally grows
n = len(nums)                                    # 7: and its count
print(total // n if n else "empty")              # 5: the plain answer
```

### The Household Ledger
A two-step transform with a short verdict:

```python
prices = {"milk": 3, "bread": 2, "eggs": 4}      # 7: the pantry prices
cart = ["milk", "bread", "bread"]                # 7: what we took
due = sum(prices[i] for i in cart)               # 7: what we owe
print(due, "dollars, cash or card")              # 5: settle up
```

## Boundaries, when NOT to use this skill

- 3-line moments with a kigo -> haiku
- 3-line humor punchlines -> senryu
- the 5-3-5 razor middle -> lunes
- the 5-7-7 half-poem addressed to its subject -> katauta
- the 3-line Korean twist form -> sijo
- the whole program on one line -> monoku
- 5-line expanded forms -> tanka / gogyohka
- 6+ line alternating verse with a closing couplet -> choka
- prose body with a closing haiku -> haibun
- linked chains of stanzas -> renga
- minimal architecture across a codebase -> minimalist-zen
- production scaffolding or verification -> no-bullshit

Dodoitsu is the four-line workhorse: three full lines, one short landing, no drama required.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following:

- exactly 4 lines of code that carry logic (language-mandated ceremony is free)
- the first three lines are full: ~7 tokens each (rhythm, ±2 slack, never padded)
- the FOURTH line is the short landing: ~5 tokens (fewer than the other three, the settlement)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`
- the program actually runs and produces the correct result
- the last line states the result plainly, it is the verdict, not a new question
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report four visible logic-line counts against `[7, 7, 7, 5]` with ±2 tolerance, while keeping the shorter final landing as an independent structural assertion.

## When to Use Dodoitsu Patterns

Use dodoitsu code when:
- the task naturally has three steps and an answer, count, filter, finish, state
- the user wants "four lines, with the weight up front and a quick close"
- you want the plain-spoken folk register: everyday tasks, direct language
- the task is too big for 3 lines but doesn't need the drama of a twist or an epic

## The Dodoitsu Aesthetic

Write code that:
- is four lines: three full, one short, the last line visibly lighter
- speaks plainly: no ornament, no cleverness for its own sake
- settles the matter: the last line is a verdict, not a hook
- does real work on every one of the first three lines

## Cross-Language Examples

```javascript
const text = require("fs").readFileSync("t.txt", "utf8");  // 7: the words arrive
const words = text.toLowerCase().match(/[a-z']+/g) || [];  // 7: the words stand
const unique = new Set(words);                             // 7: the kinds are known
console.log(`${unique.size} distinct words`);              // 5: the verdict
```

```bash
#!/bin/bash
while read -r n; do total=$((total + n)); count=$((count + 1)); done < nums.txt  # 7: the tally
# (the loop above carries lines 1-3's load in folk-shell fashion)
echo "sum=$total over $count numbers"                                            # 5: the settlement
```

## Bundled Helpers

If the task needs ASCII output, randomness, or decorative headers, reuse the shared toolkit:

- `shared/ascii_canvas.py`, ASCII canvas with lines, circles, ink-density characters
- `shared/rng.py`, seeded RNG and value noise
- `shared/box_drawing.py`, box-drawing headers

A dodoitsu may import one of these on its first line, that still counts as one of the four.
