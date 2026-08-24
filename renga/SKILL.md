---
name: renga
description: >-
  Write runnable code in a renga form: at least three linked stanzas that alternate 5-7-5 and 7-7 units, with each stage handing a visible pivot to the next. Activate only for an explicit renga, linked verse, stanza pipeline, or chained-stanza request.
---
# Renga Skill

A renga is a linked poem: many stanzas written by many poets, each continuing where the last left off. The stanzas alternate, a 5-7-5 (three lines) then a 7-7 couplet (two lines), and each is joined to its neighbor by a pivot: the kakekotoba, a word that ends one stanza and begins the next. A code renga is a program built from linked stanzas, each handing its result to the next through a pivot variable.

## Philosophy

"The renga is the social form of the family. No stanza is complete alone; each exists to be continued. A code renga is a pipeline where every stage is a verse, and the pivot variable is the kakekotoba that carries the poem forward."

The renga mindset:
1. **Stanzas, not lines**: the unit is the stanza, 3 lines (5-7-5) or 2 lines (7-7), and the poem is 3+ stanzas chained
2. **Alternating shape**: 5-7-5 stanza, then 7-7 couplet, then 5-7-5, then 7-7... the classic renga alternation
3. **The pivot**: each stanza ends by binding a variable (the kakekotoba) that the next stanza opens by reading, the hand-off IS the link
4. **Linked, not independent**: unlike sedoka's mirrored stanzas, renga stanzas are sequential, stanza n+1 cannot exist without stanza n's result
5. **Actually runs**: a renga that doesn't run end-to-end is a party where nobody shows up

## The Alternating Structure

```
stanza 1 (hokku, 3 lines):  ~5 / ~7 / ~5     the opening - sets the scene, binds the first pivot
stanza 2 (couplet, 2 lines): ~7 / ~7         develops - opens on the pivot, binds the next
stanza 3 (3 lines):          ~5 / ~7 / ~5     turns - opens on the pivot, binds the next
stanza 4 (couplet, 2 lines): ~7 / ~7         closes - opens on the pivot, lands the result
```

Each stanza is one stage of the computation. The pivot is the variable that flows through the chain, the poem's thread.

## Core Patterns

### The Chain Pipeline
Three stages, two hand-offs, one result:

```python
data = [int(x) for x in input().split()]
total = sum(data)
count = len(data)

avg = total // count
print("avg", avg)

print("sum", total)
print("count", count)
print("total", total)
```

### The Transforming Renga
Each stanza reshapes the pivot:

```python
text = open("notes.txt").read().lower()
tokens = text.split()
seen = set(tokens)

freq = sorted(((tokens.count(w), w) for w in seen), reverse=True)
top = freq[:5]

print("leaders:", " ".join(w for _, w in top))
print("of", "the", "notes", "today")
print("the", "loudest", "voices", "win")
```

### The Long Renga
Four stanzas when the task needs four stages:

```python
nums = [int(x) for x in input().split()]
total = sum(nums)
n = len(nums)

mean = total / n
above = sum(1 for x in nums if x > mean)

print(f"mean {mean:.1f}, {above} above it")
print("the", "few", "high", "ones", "pull")
print("the", "whole", "average", "up")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the renga form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.


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

- at least 3 stanzas: alternating 3-line (5-7-5) and 2-line (7-7) stanzas, in that classic alternation
- the FIRST stanza is a 3-line 5-7-5 (the hokku opening)
- every stanza after the first OPENS by reading the previous stanza's pivot variable, the link must be visible in code
- line rhythm within stanzas: ~5 tokens on short lines, ~7 on long (±2 slack, never padded)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`
- the program actually runs end-to-end and produces the correct result
- the LAST stanza lands the result (the closing couplet tells the tale)
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report stanza-visible logic-line counts against `[5, 7, 5, 7, 7, 5, 7, 5]` with ±2 tolerance, while grading stanza count, blank-line boundaries, and pivot reuse independently.

## Boundaries

This skill is not for a single linear program or unrelated blocks without linked handoffs and pivots. Without an explicit renga request or the linked-stanza contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names renga or requests linked alternating stanzas with visible handoff pivots. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Renga Aesthetic

Write code that:
- is built from stanzas, each visibly opening on the previous one's pivot
- alternates 5-7-5 and 7-7 like the classical chain
- reads like a relay: every stanza exists to be continued
- lands at the end, the final couplet states what the whole chain achieved

## Cross-Language Examples

```javascript
const fs = require("fs");                              // 5: the door opens
const text = fs.readFileSync("data.txt", "utf8");      // 7: the words arrive
const nums = text.trim().split(/\s+/).map(Number);     // 5: the numbers stand
const mean = nums.reduce((a, b) => a + b, 0) / nums.length;  // 7: the center holds
const devs = nums.map(n => Math.abs(n - mean));        // 7: the distances grow
console.log(`mean ${mean.toFixed(2)}, spread ${devs.reduce((a, b) => a + b, 0).toFixed(2)}`);  // 7: the couplet
```

```bash
#!/bin/bash
# 5: the door opens
words=$(tr '[:upper:]' '[:lower:]' < notes.txt | tr -cs '[:alpha:]' '\n' | grep -v '^$')
# 7: the words arrive
echo "$words" | sort | uniq -c | sort -rn | head -1
# 5: the loudest
top=$(echo "$words" | sort | uniq -c | sort -rn | head -1)
# 7: the crowd
echo "the loudest word"
# 7: the couplet
echo "winner: $top"
```

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
