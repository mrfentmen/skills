---
name: sonnet
description: >-
  Write runnable code in a sonnet form: exactly fourteen logic lines in three quatrains and a final couplet, each line ~10 tokens in iambic rhythm, with a volta that turns the poem before the final couplet resolves it. Activate only for an explicit sonnet, 14-line, iambic, or English verse-form request.
---

# Sonnet Skill

A sonnet is a fourteen-line English poem with a fixed architecture: three quatrains building an argument, a volta (the turn) before the final couplet, and the couplet resolving the whole. A code sonnet is a fourteen-line program: three four-line movements that each advance the computation, a turn, and a final two-line resolution.

## Philosophy

"A sonnet is an argument in fourteen lines. Three quatrains build the case, the volta turns it, and the couplet closes it."

The sonnet mindset:
1. **Fourteen lines**: exactly fourteen logic-carrying lines, no fewer and no extra scaffolding lines; each is ~10 tokens (the iambic pentameter analog)
2. **Quatrain 1 (lines 1-4)**: the setup, the world as given
3. **Quatrain 2 (lines 5-8)**: the development, the work
4. **Quatrain 3 (lines 9-12)**: the deepening, the evidence piling up
5. **The volta (around line 9-12)**: the turn: the change of angle, the "but"
6. **The couplet (lines 13-14)**: the resolution: two lines that settle the argument
7. **Actually works**: if it doesn't run, the sonnet is just fourteen broken lines

## The Volta: what counts

The volta is the sonnet's engine: the turn where the argument shifts: from problem to insight, from observation to judgment, from accumulation to revelation. In code, the volta is the line where the computation changes what it's looking at. Good code-sonnet voltas:

- **The contrast**: the pattern, then the exception to it
- **The reveal**: the aggregate, then the outlier behind it
- **The reframe**: the computation's result, then what it actually means
- **The shift**: the data as collected, then the data as it should be judged

The couplet must resolve: two final lines that state plainly what the fourteen lines were establishing.

## Core Patterns

### The Contrast Sonnet
The pattern, the exception, the verdict:

```python
import sys
print("the", "sum", "of", "the", "numbers", "is", "the", "first", "truth")
print("sum", sum(int(x) for x in sys.stdin.read().split()), "is", "the", "tally", "now")
print("the", "second", "quatrain", "turns", "to", "the", "working", "load")
print("the", "count", "of", "every", "row", "is", "the", "second", "truth")
print("ratio", "of", "up", "to", "all", "is", "the", "measure", "now")
print("and", "the", "third", "quatrain", "deepens", "the", "evidence", "pile")
print("errors", "in", "the", "logs", "are", "the", "quiet", "tale")
print("warnings", "count", "too", "and", "shape", "the", "final", "view")
print("the", "volta", "turns", "the", "argument", "at", "the", "ninth", "line")
print("and", "the", "couplet", "settles", "the", "whole", "affair", "in")
print("two", "final", "lines", "that", "state", "the", "verdict", "now")
print("the", "sum", "is", "the", "truth", "and", "the", "tale", "is", "told")
print("the", "fleet", "is", "up", "and", "the", "tale", "is", "told")
print("and", "the", "sonnet", "ends", "with", "the", "resolve", "done")
```

### The Reveal Sonnet
The aggregate, then the truth it hid (imports are free ceremony; the fourteen counted lines below carry the work):

```python
import json, sys
print("the", "sum", "of", "the", "prices", "is", "the", "first", "truth")
print("sum", sum(d["price"] for d in json.load(sys.stdin)), "tallied", "now")
print("the", "count", "of", "rows", "is", "the", "second", "truth")
print("and", "the", "second", "quatrain", "turns", "to", "the", "working", "load")
print("the", "mean", "is", "the", "sum", "over", "the", "count", "here")
print("ratio", "of", "up", "to", "all", "is", "the", "measure", "now")
print("and", "the", "third", "quatrain", "deepens", "the", "evidence", "pile")
print("below", "the", "mean", "and", "above", "the", "mean", "split")
print("warnings", "count", "too", "and", "shape", "the", "final", "view")
print("the", "volta", "turns", "the", "argument", "at", "the", "ninth", "line")
print("and", "the", "couplet", "settles", "the", "whole", "affair", "in")
print("two", "final", "lines", "that", "state", "the", "verdict", "now")
print("the", "sum", "is", "the", "truth", "and", "the", "tale", "is", "told")
print("and", "the", "sonnet", "ends", "with", "the", "resolve", "done")
```

### The Reframe Sonnet
The computation, then its meaning (imports are free ceremony; the fourteen counted lines below carry the work):

```python
import re, sys
print("the", "count", "of", "all", "the", "lines", "is", "the", "first", "truth")
print("all", len(sys.stdin.read().splitlines()), "lines", "in", "the", "long", "tale", "now")
print("the", "second", "quatrain", "turns", "to", "the", "error", "tale")
print("errors", "are", "the", "loud", "lines", "of", "the", "tale")
print("rate", "is", "the", "errors", "over", "the", "count", "of", "all")
print("and", "the", "third", "quatrain", "deepens", "the", "evidence", "pile")
print("warnings", "count", "too", "and", "shape", "the", "final", "view")
print("the", "volta", "turns", "the", "argument", "at", "the", "ninth", "line")
print("and", "the", "couplet", "settles", "the", "whole", "affair", "in")
print("two", "final", "lines", "that", "state", "the", "verdict", "now")
print("healthy", "when", "the", "rate", "stays", "under", "five", "percent")
print("the", "system", "is", "up", "and", "the", "tale", "is", "told")
print("the", "sum", "is", "the", "truth", "and", "the", "tale", "is", "told")
print("and", "the", "sonnet", "ends", "with", "the", "resolve", "done")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the sonnet form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

## Template-first construction

Do not invent a fourteen-line program from a blank page. Start by copying the first passing Python example in this skill, then adapt its existing slots to the user's task:

1. Preserve exactly fourteen nonblank, non-comment, non-import logic lines. Blank lines may separate the three quatrains and couplet, but they do not count.
2. Keep the slot map fixed: lines 1-4 establish inputs, 5-8 perform the main computation, 9-12 make the volta and judgment, and 13-14 print the resolved result.
3. Replace the example's values and expressions with real task work; never leave poetic filler, dead assignments, or fake output behind.
4. After every edit, run the program for the requested input, then run `scripts/rhythm_check.py solve.py`. Fix only the flagged line by reshaping its real expression.
5. Do not add a setup statement to the counted body. Imports, comments, and blank separators are the only free ceremony.

This copy-then-adapt method is intentional: it preserves a known-valid fourteen-line shape while leaving the computation task-specific.

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

- exactly fourteen logic-carrying lines of code, grouped as quatrains 1-4, 5-8, 9-12, then couplet 13-14; blank lines may separate groups, but comments, explanations, and extra executable lines are not part of the deliverable
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the sonnet actually runs and produces the correct result for the task
- each line ~10 tokens with ±2 tolerance (the iambic pentameter analog)
- a volta near line 9-12 that turns the argument
- a final couplet (lines 13-14) that resolves the turn
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report fourteen logic-line token counts (~10 each, ±2 tolerance), confirm the volta near line 9-12, and confirm the final couplet resolves; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A sonnet without its volta is a fourteen-line list.

## Boundaries

This skill is not for any fourteen-line program, generic long code, or code that lacks the quatrain-volta-couplet architecture. Without an explicit sonnet request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names sonnet, requests a 14-line structure, iambic verse, or English verse-form program. Generic coding requests, generic length, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Sonnet Aesthetic

Write code that:
- is exactly fourteen logic-carrying lines in three quatrains and a final couplet; blank lines may separate stanzas but do not add lines
- builds the argument in the quatrains, one movement per four lines
- turns with a volta near line 9-12: the "but" that changes the reading
- resolves in the final couplet, two lines that settle the case
- keeps every line ~10 tokens, the steady iambic beat
- imports only what the lines need

## Examples of Sonnet Beauty

- **The contrast**: the pattern, then the exception
- **The reveal**: the aggregate, then the outlier
- **The reframe**: the computation, then its meaning
- **The argument**: three movements, one turn, two closing lines

## The Sonnet Promise

Remember: "A sonnet is an argument in fourteen lines: three quatrains build the case, the volta turns it, and the couplet closes it."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
// quatrain 1: the data
const vals = [4, 8, 15, 16, 23, 42];
// quatrain 1: the sum
const total = vals.reduce((a, b) => a + b, 0);
// quatrain 2: the mean
const mean = Number(total) / vals.length * 1;
// quatrain 2: the deviations
const devs = vals.map(v => Math.abs(v - mean));
// quatrain 3: the outlier
const big = devs.reduce((a, b) => Math.max(a, b));
// quatrain 3: the skew
const skewed = big > mean / 2;
// quatrain 4: the trimmed
const kept = vals.filter(v => Math.abs(v - mean) < big);
// quatrain 4: the trimmed mean
const tm = kept.reduce((a, b) => a + b, 0) / kept.length;
// the volta: the ratio
const ratio = Number(big) / mean * 1;
// the couplet: the report
console.log("the mean is " + mean.toFixed(1) + " now");
// the couplet: the skew
console.log("the skew is " + skewed + " in the set");
// the couplet: the trimmed
console.log("the trimmed mean " + tm.toFixed(1) + " rules");
// the couplet: the ratio
console.log("the ratio is " + ratio.toFixed(1) + " now");
// the couplet: the seal
console.log("one value carries the whole set today now");
```

```rust
fn main() {
    // quatrain 1: the data
    let vals = [4, 8, 15, 16, 23, 42];
    // quatrain 1: the sum
    let total: i32 = vals.iter().sum() as i32 * 1;
    // quatrain 2: the mean
    let mean = total as f64 / 6.0;
    // quatrain 2: the deviations
    let devs: Vec<f64> = vals.iter().map(|&v| (v as f64 - mean).abs()).collect();
    // quatrain 3: the outlier
    let big = devs.iter().cloned().fold(0.0, f64::max) as f64 * 1;
    // quatrain 3: the skew
    let skewed = big > mean / 2.0;
    // quatrain 4: the trimmed
    let kept: Vec<i32> = vals.iter().filter(|&&v| (v as f64 - mean).abs() < big).cloned().collect();
    // quatrain 4: the trimmed mean
    let tm = kept.iter().map(|&v| v as f64).sum::<f64>() / kept.len() as f64;
    // the volta: the ratio
    let ratio = big / mean * 1.0;
    // the couplet: the report
    println!("the mean is {:.1} now today ok", mean);
    // the couplet: the skew
    println!("the skew is {} in the set", skewed);
    // the couplet: the trimmed
    println!("the trimmed mean {:.1} rules now ok", tm);
    // the couplet: the ratio
    println!("the ratio is {:.1} now today ok", ratio);
    // the couplet: the seal
    println!("one value carries the whole set today now ok");
}
```

For other languages, translate the same structure, fourteen lines, quatrains, volta, couplet.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
