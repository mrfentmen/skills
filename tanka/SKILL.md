---
name: tanka
description: >-
  Write runnable code in a tanka form: exactly five logic lines shaped 5-7-5-7-7, where the first three complete the immediate result and the final two expand or reflect on it. Activate only for an explicit tanka, 5-7-5-7-7, or five-line expansion request.
---

# Tanka Skill

A tanka is a haiku that keeps going, five lines, the first three a moment, the last two the moment remembered and expanded. A code tanka is a five-line program: the core task in the first three lines, then two lines that turn the result into something richer.

## Philosophy

"A tanka does not end where a haiku ends, it breathes out, then reflects."

The tanka mindset:
1. **Five lines**: 5-7-5-7-7 tokens, or fewer, never pad
2. **The upper phrase (lines 1-3)**: setup, turn, landing, the core task, done
3. **The lower phrase (lines 4-5)**: expansion, a second view of the result
4. **The reflection**: mean becomes mean-and-median; common becomes common-and-rare
5. **Actually works**: if it doesn't run, it's not a tanka

## The Syllable Question: what 5-7-5-7-7 means in code

Like haiku, code has tokens, not syllables, the atomic pieces the language reads. A tanka's rhythm maps to:

- **Lines 1-3, 5-7-5 tokens**: the moment. Setup, the dense turn, the landing.
- **Lines 4-5, 7-7 tokens**: the expansion. Two lines that take what line 3 produced and show a second, deeper view of it.

Approximate ±2 per line; density is the point, padding is forbidden. The two final lines are what make it a tanka instead of a haiku, they add a second result, a contrast, or the meaning behind the number.

## Core Patterns

### Statistics Tanka
The core (mean) plus the expansion (range, the spread behind the average).

```python
nums = [3, 1, 4, 1, 5]
mean = sum(nums) / len(nums)
spread = max(nums) - min(nums)
print("mean", mean, "range", spread, "now")
print("five", "lines", "and", "the", "poem", "is", "done")
```

### Word Tanka
The image (most common words) expanded by its mirror (the rarest words).

```python
from collections import Counter
import re, sys
words = Counter(re.findall(r"[a-z']+", sys.stdin.read().lower()))
common = words.most_common(3)
rare = sorted(words, key=words.get)[:3]
print(common, rare)
```

### Journey Tanka
The distance, then the path that made it, result, then provenance.

```python
from math import sqrt
x1, y1, x2, y2 = 0, 0, 3, 4
dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
steps = abs(x2 - x1) + abs(y2 - y1)
print(f"straight {dist:.1f} manhattan {steps}")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the tanka form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 5 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the tanka actually runs and produces the correct result for the task
- lines 1-3 complete the core task; lines 4-5 add a second view (a second output, a contrast, or a deeper number)
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the five visible logic-line token counts against `[5, 7, 5, 7, 7]` with ±2 tolerance, and confirm the final two lines expand the result; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A tanka that doesn't run is just a long broken poem, and a tanka without the two expanding lines is just a padded haiku.

## Boundaries

This skill is not for any five-line program, generic reflection, or compact code that lacks the expanding 5-7-5-7-7 result-and-reflection shape. Without an explicit tanka request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names tanka, requests a 5-7-5-7-7 structure, or requests a five-line result-plus-reflection program. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Tanka Aesthetic

Write code that:
- is five lines or fewer, no padding
- captures the moment in the first three lines, expands in the last two
- ends with the reflection, the second view that changes how you read line 3
- uses a kigo name on the turn line, like a seasonal word
- imports only what the lines need

## Examples of Tanka Beauty

- **Statistics**: the mean, then the spread behind it
- **Words**: the common, then the rare
- **Journeys**: the straight line, then the steps taken
- **Before/After**: the state, then the change
- **Costs**: the price, then the reason

## The Tanka Promise

Remember: "A haiku shows a moment. A tanka shows the moment and then what it meant. Five lines, all working, ending in the reflection."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const nums = [3, 1, 4, 1, 5, 9, 2, 6];      // setup
const mean = nums.reduce((a, b) => a + b, 0) / nums.length;  // turn
const sorted = [...nums].sort((a, b) => a - b);              // landing
const median = sorted[Math.floor(sorted.length / 2)];        // expansion
console.log(`mean ${mean.toFixed(2)} median ${median}`);     // reflection
```

```rust
fn main() {                                // ceremony, free
    let nums = [3, 1, 4, 1, 5, 9, 2, 6];
    let sum: i32 = nums.iter().sum();
    let mean = sum as f64 / nums.len() as f64;
    let max = *nums.iter().max().unwrap();
    println!("mean {mean:.2} max {max}");
}
```

For other languages, translate the same structure, setup, turn, landing, then two expanding lines.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
