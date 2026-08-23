---
name: cinquain
description: >-
  Write runnable code in a cinquain form: five lines shaped 2-4-6-8-2 tokens, a pyramid that builds to a wide middle and lands on a two-token closing word. Activate only for an explicit cinquain, 2-4-6-8-2, or pyramid-shaped request.
---

# Cinquain Skill

A cinquain is a five-line Western form with a fixed shape: 2-4-6-8-2 syllables, a pyramid that swells to its widest line and collapses to a two-syllable landing. A code cinquain is a five-line program shaped 2-4-6-8-2 tokens: a two-token opener, a growing middle, and a two-token final word that closes the whole thing.

## Philosophy

"A cinquain is a pyramid in five lines: it swells to eight, then lands on two. The shape is the poem."

The cinquain mindset:
1. **Five lines**: exactly five logic lines, shaped 2-4-6-8-2 tokens (±1 tolerance per line)
2. **Line 1, 2 tokens**: the opener, the seed
3. **Lines 2-3, 4-6 tokens**: the growing body, the work expanding
4. **Line 4, 8 tokens**: the widest line, the full computation
5. **Line 5, 2 tokens**: the landing, a two-token word that closes it
6. **Actually works**: if it doesn't run, the pyramid has no base

## The Shape: what counts

The 2-4-6-8-2 silhouette must be visible in the token counts. The final two-token line is the signature :  a short landing that names or seals the result. Good code-cinquain landings:

- **The name**: `print("done")` or `print(total)`
- **The seal**: `sys.exit(0)` or `print("ok")`
- **The verdict**: `print(mean)` or `print("up")`

The wide line 4 carries the real computation; the landing closes it.

## Core Patterns

### The Tally Cinquain
The count that builds and lands:

```python
import sys
text = sys.stdin.read()
words = text.split()
total = sum(1 for w in words)
print("total", total, "words", "in", "the", "whole", "verse")
print(total)
```

### The Stats Cinquain
The mean that builds and lands:

```python
import sys
d = {}
d = dict(zip("ab", (1, 2)))
total = sum(d.values())  # the sum
print("the", "sum", "is", total, "of", "the", "values")
print(total)
```

### The Health Cinquain
The check that builds and lands:

```python
import json
h = {}
h = json.load(open("health.json"))
down = len(h) - sum(h.values())
print("the", "down", "count", "is", down, "of", "the", "fleet")
print(down)
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the cinquain form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

- exactly five lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the cinquain actually runs and produces the correct result for the task
- five lines shaped 2-4-6-8-2 tokens (±1 tolerance per line)
- line 4 (the widest) carries the core computation; line 5 (the two-token landing) names or seals the result
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the five visible logic-line token counts against `[2, 4, 6, 8, 2]` with ±1 tolerance, and confirm the two-token landing closes the computation; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A cinquain without its pyramid is five loose lines.

## Boundaries

This skill is not for any five-line program, generic compact code, or code that lacks the 2-4-6-8-2 pyramid shape. Without an explicit cinquain request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names cinquain, requests a 2-4-6-8-2 structure, or requests a pyramid-shaped verse program. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Cinquain Aesthetic

Write code that:
- is five lines, shaped 2-4-6-8-2
- swells to the wide line 4, then lands on two tokens
- makes the landing the seal: a name, a verdict, a number
- imports only what the lines need

## Examples of Cinquain Beauty

- **The tally**: count the errors, land the number
- **The stats**: mean and spread, land the mean
- **The health**: the down list, land the count
- **The pyramid**: build to eight, land on two

## The Cinquain Promise

Remember: "A cinquain is a pyramid in five lines: it swells to eight, then lands on two. The shape is the poem."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
// 2: the values
const nums=[3];
// 4: the sum
const total = nums[0]+nums[0];
// 6: the mean
const mean = total / nums.length;
// 8: the report
console.log("the final mean value is " + mean.toFixed(1));
// 2: the landing
console.log(mean.toFixed(1));
```

```rust
fn main() {
    // 2: the values
    let nums=[3];
    // 4: the sum
    let total = nums.iter().sum::<i32>();
    // 6: the mean
    let mean = total as f64;
    // 8: the report
    println!("the final mean value is now {mean:.1}");
    // 2: the landing
    println!("{mean:.1}");
}
```

For other languages, translate the same structure, five lines, pyramid to a two-token landing.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
