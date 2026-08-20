---
name: kanshi
description: >-
  Write runnable code in a kanshi form: Japanese verse in the classical Chinese style, four logic lines of paired 7-7 couplets (or 5-5), where the third line turns and the fourth resolves. Activate only for an explicit kanshi, Chinese-style verse, or four-line couplet request.
---

# Kanshi Skill

A kanshi is a poem written in classical Chinese by Japanese poets: four lines of seven characters each, the lines paired as couplets, the third line turning the poem and the fourth resolving it. A code kanshi is a four-line program in two couplets: the first couplet states the situation, the second turns and resolves it.

## Philosophy

"A kanshi walks in pairs. Two lines set the scene, two lines turn and settle it."

The kanshi mindset:
1. **Four lines**: exactly four logic-carrying lines, each ~7 tokens; never use fewer or add a fifth line
2. **Couplet 1 (lines 1-2)**: the parallel statement: two lines that mirror each other, the scene and its complement
3. **The turn (line 3)**: the pivot, the surprise, the deeper view
4. **Couplet 2's resolve (line 4)**: the resolution, the settled answer to the turn
5. **Parallelism**: lines 1-2 should rhyme in structure: same shape, mirrored content
6. **Actually works**: if it doesn't run, the couplets are just two lines of noise

## The Couplet: what counts

Lines 1-2 must be structurally parallel: the same computation performed on mirrored data, or a question and its mirror. Good code-kanshi couplets:

- **The mirror**: max and min of the same set
- **The pair**: count of failures and count of successes
- **The echo**: the raw value and the normalized value

Line 3 turns the poem: it takes the couplet's output and looks at it from an angle the first two lines didn't show. Line 4 resolves: the final truth, stated plainly.

## Core Patterns

### The Mirror Kanshi
The couplet, the turn, the resolve:

```python
data = input().split() or []
nums = [int(x) for x in data]
summary = {"sum": sum(nums), "count": len(nums)}
print("sum", summary["sum"], "count", summary["count"], "done")
```

### The Parallel Kanshi
Two mirrored lines, then the turn:

```python
import statistics as st
nums = [4, 8, 15, 23, 42]
lo = min(nums)  # the floor
hi = max(nums)  # the ceiling
print("range", hi - lo, "of", "the", "tale")
```

### The Echo Kanshi
The pair that reveals:

```python
import re, sys
text = sys.stdin.read()  # the source
chars = len(text)  # the characters
words = len(re.findall(r"\S+", text))  # the words
print(f"{chars / max(1, words):.1f} chars per word")
```

## Workflow

1. **Write it plainly.** Implement the task ordinarily and run it until the output is right. No form pressure yet.
2. **Start from the four-line template.** Keep exactly four logic lines. Lines 1 and 2 establish parallel data, line 3 turns it into the key measure, and line 4 resolves with the requested output.
3. **Fill real work into the slots.** Preserve the four line breaks and keep every line within `[7, 7, 7, 7]` with ±2 whitespace-token tolerance. Change expressions only for real task work; never add filler, semicolons, or a fifth line.
4. **Verify the form and result.** Run the program with the real input, then run `scripts/rhythm_check.py solve.py`. If it fails, use the reported profile to reshape only the offending line while preserving the four-line architecture.
5. **Report the counts.** State the four token counts, identify the parallel couplet, and explain the turn and resolution.

## Proven Four-Line Template

Models preserve a demonstrated four-line shape more reliably than an abstract request for four exact counts. Adapt this template to the task, but keep the line roles and line breaks:

```python
data = input().split() or []
nums = [int(x) for x in data]
summary = {"sum": sum(nums), "count": len(nums)}
print("sum", summary["sum"], "count", summary["count"], "done")
```

Its token profile is `[5, 7, 6, 5]`, which is within ±2 of the kanshi target `[7, 7, 7, 7]`. The first two lines establish and parse the input; the third line turns the data into a guarded measure; and the fourth resolves it as the requested output. If a task needs different data, preserve the same sequence: read, parse or mirror, compute the turn, print the resolution.


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

- exactly 4 logic-carrying lines of code; language-mandated ceremony like `fn main()` / braces may surround them but does not replace or add to the four lines
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the kanshi actually runs and produces the correct result for the task
- lines 1-2 form a parallel couplet (~7 tokens each, mirrored structure)
- line 3 turns the couplet's result; line 4 resolves it
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the four visible logic-line token counts (~7-7-7-7 with ±2 tolerance), confirm lines 1-2 are parallel couplets, and confirm line 4 resolves line 3's turn; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A kanshi without its couplets is four loose lines.

## Boundaries

This skill is not for any four-line program, generic compact code, or code that lacks the paired couplet-and-turn shape. Without an explicit kanshi request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names kanshi, requests Chinese-style verse, or requests a four-line couplet structure. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Kanshi Aesthetic

Write code that:
- has exactly four logic-carrying lines, no padding
- pairs the first two lines as a mirror couplet: same shape, mirrored data
- turns on line 3 with a genuine pivot, not a continuation
- resolves on line 4 with the plain truth the turn exposed
- uses a kigo-like seasonal name in the turn line
- imports only what the lines need

## Examples of Kanshi Beauty

- **The mirror**: up and down, counted in parallel
- **The pair**: floor and ceiling, then the span
- **The echo**: characters and words, then the density
- **The parallel**: two views, one truth

## The Kanshi Promise

Remember: "A kanshi walks in pairs. Two parallel lines set the scene, the third turns it, and the fourth settles it."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const nums = [4, 8, 15, 16, 23, 42];       // couplet: the values
const lo = Math.min(...nums);              // couplet: the floor
const hi = Math.max(...nums);              // couplet: the ceiling
console.log(`range ${hi - lo}`);           // the resolve: the measure
```

```rust
fn main() {                                // ceremony, free
    let nums = [4, 8, 15, 16, 23, 42];     // couplet: the values
    let lo = *nums.iter().min().unwrap();  // couplet: the floor
    let hi = *nums.iter().max().unwrap();  // couplet: the ceiling
    println!("range {}", hi - lo);         // the resolve: the measure
}
```

For other languages, translate the same structure, parallel couplet, then the turn and resolve.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
