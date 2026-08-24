---
name: ryuka
description: >-
  Write runnable code in a ryuka form: the Okinawan four-line verse shaped 8-8-8-6 tokens, three long lines and a short closing line that lands the song. Activate only for an explicit ryuka, Okinawan verse, or 8-8-8-6 request.
---

# Ryuka Skill

A ryuka is a traditional Okinawan poem: four lines, 8-8-8-6 syllables, a song of three long breaths and one short landing. Unlike the Japanese mainland's 5-7-5, the ryuka is roomier :  its 8-syllable lines carry more, and the final 6-syllable line snaps the whole thing shut. A code ryuka is a four-line program shaped 8-8-8-6 tokens: three lines of substantive work, then a short closing line that lands the result.

## Philosophy

"A ryuka is an Okinawan song: three long lines, one short landing. The last line is where the song closes."

The ryuka mindset:
1. **Four lines**: exactly four logic lines, shaped 8-8-8-6 tokens (±2 tolerance per line)
2. **Lines 1-3, 8 tokens each**: the work :  load, process, verify :  roomier than haiku's 5-7-5
3. **Line 4, 6 tokens**: the landing :  shorter, the song's final word
4. **The room**: 8-token lines allow fuller expressions, chained calls, real logic
5. **Actually works**: if it doesn't run, the song has no voice

## The Landing: what counts

Line 4 is deliberately shorter than the first three :  the 6-token closing that seals the song. It should resolve what the three long lines built. Good code-ryuka landings:

- **The verdict**: `print("all systems go")` (6 tokens)
- **The count**: `print(f"{n} failures")` (6 tokens)
- **The name**: `print(mean_result)` (4-6 tokens)

The first three lines carry the weight; line 4 closes it.

## Core Patterns

### The Health Ryuka
Three lines of checking, one line of verdict:

```python
import sys
numbers = [int(x) for x in sys.stdin.read().split()]
up = sum(n > 0 for n in numbers)
down = sum(n < 0 for n in numbers)
print("up", up, "down", down)
```

### The Stats Ryuka
Three lines of math, one line of result:

```python
import statistics as st
nums = [3, 1, 4, 1, 5, 9, 2, 6]
mean = st.mean(nums)  # the mean
spread = max(nums) - min(nums)  # the spread
print("mean", round(mean, 1), "spread", spread, "now")
```

### The Log Ryuka
Three lines of parsing, one line of truth:

```python
import re, sys
lines = sys.stdin.read().splitlines()  # the source
errors = sum("ERR" in l for l in lines)
total = len(lines)  # the total
print("errors", errors, "in", "all")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the ryuka form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

- exactly four lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the ryuka actually runs and produces the correct result for the task
- four lines shaped 8-8-8-6 tokens (±2 tolerance per line)
- line 4 (the 6-token landing) resolves what lines 1-3 built
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the four visible logic-line token counts against `[8, 8, 8, 6]` with ±2 tolerance, and confirm the short landing closes the song; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A ryuka without its short landing is just four lines of code.

## Boundaries

This skill is not for any four-line program, generic compact code, or code that lacks the 8-8-8-6 song shape. Without an explicit ryuka request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names ryuka, requests Okinawan verse, or requests an 8-8-8-6 structure. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Ryuka Aesthetic

Write code that:
- is four lines, shaped 8-8-8-6
- lets the three long lines carry the real work
- ends on the short landing, the song's closing word
- uses a kigo-like name or image in the long lines
- imports only what the lines need

## Examples of Ryuka Beauty

- **The health song**: load, check, count, land
- **The stats song**: values, mean, spread, land
- **The log song**: source, filter, total, land
- **The Okinawan room**: three long lines, one short close

## The Ryuka Promise

Remember: "A ryuka is an Okinawan song: three long lines, one short landing. The last line is where the song closes."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
// 8: the values
const nums = [3, 1, 4, 1, 5, 9];
// 8: the sum
const total = nums.reduce((a, b) => a + b, 0);
// 8: the mean
const mean = total / nums.length;
// 8: the landing
console.log(`the final mean value is ${mean.toFixed(1)}`);
```

```rust
fn main() {
    // 8: the values
    let nums = [3, 1, 4, 1, 5, 9];
    // 8: the sum
    let total: i32 = nums.iter().fold(0, |a, &b| a + b);
    // 8: the mean
    let mean = f64::from(total) / 6.0;
    // 8: the landing
    println!("the final mean value is {mean:.1}");
}
```

For other languages, translate the same structure, three long lines and a short landing.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
