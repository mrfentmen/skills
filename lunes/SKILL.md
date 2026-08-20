---
name: lunes
description: >-
  Write runnable code in a lune form: three logic lines shaped 5-3-5, with a single decisive middle operation that is visibly shorter than its setup and landing. Activate only for an explicit lune, lunes, or 5-3-5 request.
---

# Lunes Skill

The lune is the American haiku, invented, not inherited, with its own rhythm: 5-3-5. Where the haiku's middle line is the longest, the lune's middle line is the thinnest, three tokens, one sharp act. A code lune is three lines: setup, a razor-thin decisive middle, landing.

## Philosophy

"A lune is a haiku that punches. Short breath, one strike, done."

The lune mindset:
1. **Three lines**: 5-3-5 tokens, the middle is the smallest
2. **The punch**: the middle line does exactly one sharp thing in ~3 tokens
3. **Setup and landing**: the world before, the world after
4. **No wasted motion**: every token earns its place
5. **Actually works**: a lune that doesn't run is just a broken rhythm

## The Syllable Question: what 5-3-5 means in code

Tokens are the code analog of syllables. The lune's shape is the mirror of the haiku's:

- **Line 1, 5 tokens**: setup. The world, the data, the situation.
- **Line 2, 3 tokens**: the punch. One decisive operation, `total = sum(nums)`, `data.sort()`, `return mode(x)`.
- **Line 3, 5 tokens**: landing. The result, shown.

Approximate ±1, the middle line especially, because 3 tokens is the whole point. If the middle line is as long as the others, it's not a lune, it's a haiku with a limp.

## Core Patterns

### Summation Lune
Setup, one 3-token strike, landing.

```python
nums = [3, 1, 4, 1, 5]
total = sum(nums)
print("sum", total, "now")
```

### Mode Lune
The punchline middle: one expression that finds the answer.

```python
xs = [1, 2, 2, 3]
mode = max(set(xs), key=xs.count)
print(mode, "repeats", "the", "most")
```

### Line-Count Lune
A tiny tool with a 3-token strike in the middle.

```python
import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
print(total, "is", "the", "sum")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the lunes form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

- at most 3 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the lune actually runs and produces the correct result for the task
- the middle line is the shortest line, roughly 3 tokens, one decisive operation
- every token earns its place; no filler to reach any count
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

These requirements exist because a theme without a spec produces vibes, not output. The short middle line is what separates a lune from a haiku, grade it like you mean it.

## Boundaries

This skill is not for generic brevity or any three-line program whose middle is not deliberately short. Without an explicit lune request or the 5-3-5 contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names lune/lunes or requests a 5-3-5 program. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Lune Aesthetic

Write code that:
- is three lines or fewer
- keeps the 5-3-5 rhythm, middle line shortest
- makes the middle line exactly one decisive operation
- imports only what the punch needs
- ends with the result, no commentary

## Examples of Lune Beauty

- **Sums**: setup, `sum(nums)`, print
- **Modes**: setup, one expression, print
- **Counts**: read, count, show
- **Sorts**: setup, one call, show
- **One-liners**: the whole task as one breath and one strike

## The Lune Promise

Remember: "The lune says it in five, then three, then five, the middle is the strike, the rest is the breath around it. Three lines, one punch, it runs."

## Cross-Language Examples

The 5-3-5 rhythm translates everywhere, keep the middle short:

```javascript
const add = (a, b) => a + b;            // setup
const total = [3, 1, 4, 1, 5].reduce(add);  // punch (short)
console.log(total);                     // landing
```

```rust
fn main() {                              // ceremony, free
    let sum: i32 = [3, 1, 4].iter().sum();  // the punch
    println!("{sum}");                   // landing
}
```

For other languages, translate the same structure, setup, one sharp middle, landing.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
