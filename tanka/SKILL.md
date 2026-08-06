---
name: tanka
description: >-
  Write code as a tanka: a complete, working program in five lines that first captures a
  moment and then expands it - the 5-7-5-7-7 rhythm with tokens as the code analog of
  syllables (setup, turn, landing, then two expanding lines). Use this skill when the user
  wants a 5-line dense program, or a solution that shows a result and then its deeper view
  (mean and median, common and rare, before and after). Make sure to use this skill
  whenever the user mentions tanka, five-line poems, 5-7-5-7-7, or wants a dense working
  program with an expanded second view. This skill is NOT for 3-line forms (use haiku,
  senryu, or lunes) and NOT for code golf (use esoteric-programming).
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
import statistics as st
nums = [3, 1, 4, 1, 5, 9, 2, 6]
mean = st.mean(nums)
spread = max(nums) - min(nums)
print(f"mean {mean:.2f} range {spread}")
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

## Boundaries, when NOT to use this skill (use a different skill instead)

This skill is **not for** every poetic-code request. When the user asks for one of the following, **instead use** the listed skill, the goal is that two skills never coin-flip on the same prompt:

- 3-line forms (nature, humor, or American punch) -> haiku, senryu, or lunes
- shortest-possible / golfed code -> esoteric-programming
- minimal architecture across a codebase -> minimalist-zen

Tanka is the five-line form: core task, then the expansion. If the user wants exactly three lines, it's not a tanka.

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

## When to Use Tanka Patterns

Use tanka code when:
- the task has two layers, a result and its deeper view
- the user wants a five-line dense program
- one number alone isn't enough (mean needs median, count needs rare)
- the user says "expanded", "the deeper view", or "and also show..."

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

If the task needs ASCII output, randomness, or decorative headers, reuse the shared toolkit:

- `shared/ascii_canvas.py`, ASCII canvas with lines, circles, ink-density characters
- `shared/rng.py`, seeded RNG and value noise
- `shared/box_drawing.py`, box-drawing headers

A tanka may import one of these on its setup line, that still counts as one of the five.
