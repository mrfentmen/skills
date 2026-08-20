---
name: etheree
description: >-
  Write runnable code in an etheree form: ten lines whose token counts climb 1-2-3-4-5-6-7-8-9-10, a ladder of growing expressions that ascends to the result. Activate only for an explicit etheree, ten-line ladder, or 1-2-3-4-5-6-7-8-9-10 request.
---

# Etheree Skill

An etheree is a ten-line poem whose syllable counts climb from one to ten: 1-2-3-4-5-6-7-8-9-10, an unbroken ladder of growing lines. The single-syllable first line sets the theme; each line adds a syllable until the ten-syllable final line completes the thought. A code etheree is a ten-line program whose token counts climb 1-2-3-4-5-6-7-8-9-10: the smallest line states the seed, each line grows the computation, and the ten-token final line lands the result.

## Philosophy

"An etheree is a ladder: ten lines, one to ten. Each rung grows the thought until the top rung lands it."

The etheree mindset:
1. **Ten lines**: exactly ten logic-carrying lines, no preamble or explanatory executable lines; their measured counts must match 1,2,3,4,5,6,7,8,9,10 within ±1 per line
2. **Line 1, 1 token**: the seed :  a single variable or call that states the theme
3. **Lines 2-9**: the climb :  each line grows the computation by one token
4. **Line 10, 10 tokens**: the landing :  the largest line, the result
5. **The ladder**: every line must genuinely be more substantial than the last
6. **Actually works**: if it doesn't run, the ladder has no top

## The Climb: what counts

The token count must follow the fixed ten-rung sequence, not merely increase: line 1 targets 1 token, line 2 targets 2, and so on through line 10 targeting 10, each within ±1. A monotonic but otherwise arbitrary profile is not an etheree. The growth must be real, not padding. Good code-etheree climbs:

- **The seed**: `nums` (1) → `nums = [...]` (2-4) → `sorted(nums)` (5+) → `sum(sorted(nums))` → `print(f"mean {sum(sorted(nums)) / len(nums):.1f}")` (10)
- **The filter**: `lines` (1) → `errors = [...]` (3) → `[l for l in lines if "ERR" in l]` (8) → the full report (10)

The top rung is the whole point: a ten-token line that resolves everything the ladder built.

## Core Patterns

### The Stats Etheree
A ladder that grows the mean, one rung at a time:

```python
import sys
sys.stdin
data=[]
data += sys.stdin.read().split()
n = len(data)
total = sum(map(len, data))
avg = total / max(1, n)
long = max(map(len, data), default = 0)
summary = ("count", n, "total", total, "average", avg)
report = (*summary, "score", n + total, "ok")
print("report", report, "items", len(report), "score", n+total, "status", "ok", "done", "valid")
```

### The Health Etheree
A ladder that grows the verdict:

```python
import json
json
h = json.load(open("health.json"))
up = sum(h.values())
down = len(h) - up
print("up", up, "down", down)
print("the", "fleet", "is", "up", "now")
print("healthy", down == 0, "of", "the", "fleet")
print("fleet", "is", "healthy" if down == 0 else "degraded")
print("report", "up", up, "down", down, "of", "the", "fleet")
print("the", "final", "report", "is", "up", up, "and", "down", down, "now")
```

### The Log Etheree
A ladder that grows the count:

```python
import sys
sys.stdin
lines = sys.stdin.read().splitlines()
total = len(lines)
print("errors", "in", "the", "log")
print("count", "of", "lines", "now")
print("the", "ladder", "climbs", "up", "now")
e=sum("ERR" in l for l in lines)
print("errors", e, "of", "the", "lines", "seen", "now")
print("rate", round(e / max(1, total), 2), "per", "line")
print("clean", total - e, "lines", "of", "the", "tale", "now")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the etheree form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

## Template-first construction

Do not invent a ten-rung etheree from a blank page. Start by copying the first passing Python example in this skill, then adapt its slots to the user's task:

1. Preserve exactly ten nonblank, non-comment, non-import logic lines. Blank lines do not count.
2. Keep one rung per line and preserve the target profile `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` within the checker tolerance. Adapt real expressions rather than adding separate setup lines.
3. Make the climb real: each rung must load, transform, measure, or report the task. Remove `pass`, dead assignments, and poetic-only output when adapting the template.
4. After every edit, run the program for the requested input, then run `scripts/rhythm_check.py solve.py`. Fix only the flagged rung by reshaping its real expression.
5. Do not add a setup statement to the counted body. Imports, comments, and blank separators are the only free ceremony.

This copy-then-adapt method is intentional: it preserves a known-valid ten-rung shape while leaving the computation task-specific.

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

- exactly ten logic-carrying lines of code, no fewer and no more; language-mandated ceremony like `fn main()` / braces may surround them but does not replace or add to the ten rungs
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the etheree actually runs and produces the correct result for the task
- ten lines whose token counts climb 1-2-3-4-5-6-7-8-9-10 (±1 tolerance per line)
- line 10 (the 10-token landing) resolves what the ladder built
- the climb is real: each line carries at least as much logic as the last
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the ten visible logic-line token counts against `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` with ±1 tolerance, and confirm the top rung lands the result. The bundled checker verifies line count and token shape; the real climb and landing semantics remain checks that the author must confirm. Diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. An etheree without its ladder is ten lines of code.

## Boundaries

This skill is not for any ten-line program, generic growing code, or code that lacks the 1-to-10 ladder. Without an explicit etheree request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names etheree, requests a ten-line ladder, or requests a 1-2-3-4-5-6-7-8-9-10 structure. Generic coding requests, generic length, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Etheree Aesthetic

Write code that:
- is exactly ten logic-carrying lines, with the fixed 1-2-3-4-5-6-7-8-9-10 target profile
- starts from a one-token seed and grows the computation rung by rung
- lands the result on the ten-token top rung
- makes the growth real :  longer expressions, more work, never padding
- imports only what the lines need

## Examples of Etheree Beauty

- **The stats ladder**: seed, values, sum, mean, landing
- **The health ladder**: seed, load, check, report, landing
- **The log ladder**: seed, source, filter, report, landing
- **The climb**: one token to ten, then the result

## The Etheree Promise

Remember: "An etheree is a ladder: ten lines, one to ten. Each rung grows the thought until the top rung lands it."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const nums = [3, 1, 4, 1, 5];         // 1: the seed
let s = nums.reduce((a, b) => a + b, 0);  // 2: the sum
let avg = s / nums.length;            // 3: the mean
console.log(`mean ${avg.toFixed(1)}`);    // 4: the report
console.log(`mean ${nums.reduce((a, b) => a + b, 0) / nums.length}`);  // 5: the landing
```

```rust
fn main() {                            // ceremony, free
    let nums = [3, 1, 4, 1, 5];        // 1: the seed
    let s: i32 = nums.iter().sum();    // 2: the sum
    let avg = s as f64 / nums.len() as f64;  // 3: the mean
    println!("mean {avg:.1}");         // 4: the report
    println!("mean {}", nums.iter().sum::<i32>() as f64 / nums.len() as f64);  // 5: the landing
}
```

For other languages, translate the same structure, ten rungs, one landing.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
