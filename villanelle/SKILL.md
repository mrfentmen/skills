---
name: villanelle
description: >-
  Write runnable code in a villanelle form: nineteen lines in five tercets and a closing quatrain, where two refrain lines each repeat four times, framing the whole computation. Activate only for an explicit villanelle, 19-line, or repeating-refrain request.
---

# Villanelle Skill

A villanelle is a nineteen-line Western poem: five tercets (three-line stanzas) and a closing quatrain, built on two refrains. Line 1 repeats as lines 6, 12, and 18; line 3 repeats as lines 9, 15, and 19. The refrains are the poem's spine :  the same words returning at intervals while everything around them shifts. A code villanelle is a nineteen-line program where two key expressions (the refrains) are repeated at those exact positions, each time recomputed or re-evaluated, while the other lines evolve the state between them.

## Philosophy

"A villanelle is a song of two refrains. Nineteen lines, and two lines keep coming back, changed each time by what happened between them."

The villanelle mindset:
1. **Nineteen lines**: exactly five tercets (logic lines 1-15) plus one closing quatrain (logic lines 16-19); no preamble or explanatory executable lines are allowed in the counted body
2. **Refrain A (lines 1, 6, 12, 18)**: the same expression, repeated four times, each time seeing new state
3. **Refrain B (lines 3, 9, 15, 19)**: the second expression, repeated four times, evolving with it
4. **The space between**: the non-refrain lines transform the data so the refrain means something new each visit
5. **Actually works**: if it doesn't run, the refrain has no breath

## The Refrain: what counts

The two refrain lines must be **recognizably the same expression** each time :  same function, same computation :  but operating on state that the intervening lines changed. Good code-villanelle refrains:

- **The total**: `total = sum(values)` returning at intervals while `values` changes
- **The check**: `healthy = all(v["up"] for v in services)` re-evaluated as services change
- **The count**: `errors = sum(1 for line in log if "ERR" in line)` growing as log lines arrive

The other lines do the work: parse, filter, transform :  so that each refrain return lands differently.

## Core Patterns

### The Accumulating Villanelle
The count that keeps returning as data grows (the source load is a free ceremony preamble; the nineteen logic lines below carry the refrains):

```python
import sys
print("the", "lines", "grow", "and", "the", "tale", "unfolds")
data = [line for line in sys.stdin.read().splitlines()]
print("and", "the", "errors", "echo", "deep", "through", "the", "long", "dark", "tale")
errors = [line for line in data if "ERR" in line]
print("the", "filter", "keeps", "only", "the", "bad", "lines")
print("the", "lines", "grow", "and", "the", "tale", "unfolds")
warns = [line for line in data if "WARN" in line]
print("the", "warnings", "count", "too", "in", "the", "tale")
print("and", "the", "errors", "echo", "deep", "through", "the", "long", "dark", "tale")
clean = [line for line in data if "ERR" not in line]
print("and", "the", "rest", "are", "the", "quiet", "lines")
print("the", "lines", "grow", "and", "the", "tale", "unfolds")
print("total", len(data), "errors", len(errors), "of", "the", "tale")
print("the", "errors", "are", "the", "loud", "lines", "of", "the", "tale")
print("and", "the", "errors", "echo", "deep", "through", "the", "long", "dark", "tale")
print("the", "tale", "is", "done", "with", "the", "counts", "in")
print("total", len(data), "lines", "and", "errors", len(errors), "now")
print("the", "lines", "grow", "and", "the", "tale", "unfolds")
print("and", "the", "errors", "echo", "deep", "through", "the", "long", "dark", "tale")
```

### The Evolving Villanelle
The health check that changes meaning (refrains A and B are the narration prints that frame the changing state; the assignments between them do the real work):

```python
import json
print("the", "services", "turn", "and", "the", "state", "unfolds")
services = {k: v for k, v in json.load(open("health.json")).items()}
print("and", "the", "verdict", "echoes", "deep", "through", "the", "long", "dark", "tale")
services["cache"] = True  # the cache recovers
print("cache", "wakes", "and", "the", "fleet", "stirs", "now")
print("the", "services", "turn", "and", "the", "state", "unfolds")
services["db"] = False  # the db fails
print("the", "db", "falls", "and", "the", "count", "drops")
print("and", "the", "verdict", "echoes", "deep", "through", "the", "long", "dark", "tale")
up = sum(1 for s in services.values() if s)
print("up", up, "of", "the", "services", "are", "up")
print("the", "services", "turn", "and", "the", "state", "unfolds")
services["db"] = True  # the db returns
print("the", "db", "returns", "and", "the", "count", "rises")
print("and", "the", "verdict", "echoes", "deep", "through", "the", "long", "dark", "tale")
down = sum(1 for s in services.values() if not s)
print("down", down, "of", "the", "services", "still", "remain")
print("the", "services", "turn", "and", "the", "state", "unfolds")
print("and", "the", "verdict", "echoes", "deep", "through", "the", "long", "dark", "tale")
```

### The Threshold Villanelle
The load check as traffic shifts (refrains A and B are the narration prints; the assignments between them do the real work):

```python
import statistics as st
print("the", "loads", "shift", "and", "the", "tale", "unfolds")
loads = [int(x) for x in "3 7 2 9 4".split()]
print("and", "the", "mean", "echoes", "deep", "through", "the", "long", "dark", "tale")
loads.append(11)  # the spike lands here now
print("the", "spike", "lands", "and", "the", "peak", "rises")
print("the", "loads", "shift", "and", "the", "tale", "unfolds")
peak = max(loads)  # the new peak
print("peak", peak, "of", "the", "current", "load", "now")
print("and", "the", "mean", "echoes", "deep", "through", "the", "long", "dark", "tale")
loads.pop(0)  # the old line drops off
print("the", "old", "line", "drops", "and", "the", "mean", "falls")
print("the", "loads", "shift", "and", "the", "tale", "unfolds")
avg = sum(loads) / len(loads)  # the mean
print("avg", avg, "of", "the", "current", "load", "now")
print("and", "the", "mean", "echoes", "deep", "through", "the", "long", "dark", "tale")
loads.append(2)  # the calm arrives here now
print("the", "calm", "arrives", "and", "the", "mean", "holds")
print("the", "loads", "shift", "and", "the", "tale", "unfolds")
print("and", "the", "mean", "echoes", "deep", "through", "the", "long", "dark", "tale")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the villanelle form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

## Template-first construction

Do not invent a nineteen-line villanelle from a blank page. Start by copying the first passing Python example in this skill, then adapt its slots to the user's task:

1. Preserve exactly nineteen nonblank, non-comment, non-import logic lines. Blank lines may separate the five tercets and closing quatrain, but they do not count.
2. Keep the refrain slots fixed: A at lines 1, 6, 12, and 18; B at lines 3, 9, 15, and 19. Reuse the same expression shape at each slot, with state changed only by the intervening real work.
3. Replace the example's data and transformations with real task work; never leave poetic filler, dead assignments, or fake output.
4. After every edit, run the program for the requested input, then run `scripts/rhythm_check.py solve.py`. Fix only the flagged line by reshaping its real expression.
5. Do not add a setup statement to the counted body. Imports, comments, and blank separators are the only free ceremony.

This copy-then-adapt method is intentional: it preserves a known-valid nineteen-line shape and exact refrain positions while leaving the computation task-specific.

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

- exactly nineteen logic-carrying lines of code, arranged as five tercets and a closing quatrain; imports or language wrappers may be required outside the counted body, but no extra setup, explanation, or output line may be added to the 19-line body
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the villanelle actually runs and produces the correct result for the task
- two refrain expressions, each recognizably repeated exactly at the canonical positions: Refrain A at logic lines 1, 6, 12, 18; Refrain B at logic lines 3, 9, 15, 19; do not shift either refrain
- the non-refrain lines evolve the state so each refrain return sees new data
- each line ~10 tokens with ±3 tolerance (the iambic pentameter analog)
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report nineteen logic-line token counts (~10 each), confirm the two refrains repeat at the canonical positions with the same expression each return, and confirm the state evolves between returns. The bundled checker verifies line count, token shape, refrain-position token consistency, and refrain-text overlap (each return must share most of its tokens with the first occurrence, comments stripped); state evolution remains a semantic check that the author must confirm. Diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A villanelle without its refrains is nineteen loose lines.

## Boundaries

This skill is not for any nineteen-line program, generic long code, or code that lacks the repeating-refrain architecture. Without an explicit villanelle request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names villanelle, requests a 19-line structure, or requests a repeating-refrain verse program. Generic coding requests, generic length, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Villanelle Aesthetic

Write code that:
- is exactly nineteen logic-carrying lines in five tercets and a closing quatrain; blank lines may separate stanzas but do not add lines
- repeats two refrain expressions at the canonical positions
- makes every refrain return land differently, because the state between changed
- uses the closing quatrain to resolve what the refrains kept circling
- imports only what the lines need

## Examples of Villanelle Beauty

- **The accumulating count**: the total and the errors, returning as data grows
- **The evolving check**: the health verdict, changing meaning each return
- **The threshold**: the peak and the mean, as traffic shifts
- **The circling**: two refrains, one resolution

## The Villanelle Promise

Remember: "A villanelle is a song of two refrains: nineteen lines, and two lines keep coming back, changed each time by what happened between them."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
// refrain A: the total
console.log("the", "total", "is", total, "in", "the", "long", "tale", "of", "old");
// the data
const nums = [3, 1, 4, 1, 5];
// refrain B: the mean
console.log("the", "mean", "is", avg, "and", "still", "more");
// the sum
let total = nums.reduce((a, b) => a + b, 0);
// the mean
let avg = total / nums.length * 1;
// refrain A returns
console.log("the", "total", "is", total, "in", "the", "long", "tale", "of", "old");
// the spike
const spike = 9; nums.push(spike); nums.sort(); nums.reverse();
// the sum returns
total = nums.reduce((a, b) => a + b, 0);
// refrain B returns
console.log("the", "mean", "is", avg, "and", "still", "more");
// the old drops
const first = nums.shift(); nums.unshift(first); nums.sort(); nums.reverse();
// the mean returns
avg = total / nums.length * 1;
// refrain A returns
console.log("the", "total", "is", total, "in", "the", "long", "tale", "of", "old");
// the clean pass
const clean = nums.filter(n => n < 10);
// the sum returns
total = clean.reduce((a, b) => a + b, 0);
// refrain B returns
console.log("the", "mean", "is", avg, "and", "still", "more");
// the mean returns
avg = total / clean.length * 1;
// the seal
console.log("the", "final", "count", "is", "the", "last", "refrain");
// refrain A returns
console.log("the", "total", "is", total, "in", "the", "long", "tale", "of", "old");
// refrain B returns
console.log("the", "mean", "is", avg, "and", "still", "more");
```

```rust
fn main() {
    // refrain A: the total
    println!("the total is {} in the long tale of old", total);
    // the data
    let mut nums = vec![3, 1, 4, 1, 5];
    // refrain B: the mean
    println!("the mean is {} and more", avg);
    // the sum
    let mut total: i32 = nums.iter().sum() as i32;
    // the mean
    let mut avg = total as f64 / nums.len() as f64;
    // refrain A returns
    println!("the total is {} in the long tale of old", total);
    // the spike
    let spike = 9; nums.push(spike); nums.sort_unstable(); nums.reverse();
    // the sum returns
    total = nums.iter().fold(0, |a, &b| a + b);
    // refrain B returns
    println!("the mean is {} and more", avg);
    // the old drops
    let first = nums.remove(0); nums.push(first); nums.sort_unstable(); nums.reverse();
    // the mean returns
    avg = total as f64 / nums.len() as f64;
    // refrain A returns
    println!("the total is {} in the long tale of old", total);
    // the clean pass
    let clean: Vec<i32> = nums.iter().filter(|&&n| n < 10).cloned().collect();
    // the sum returns
    total = clean.iter().fold(0, |a, &b| a + b);
    // refrain B returns
    println!("the mean is {} and more", avg);
    // the mean returns
    avg = total as f64 / clean.len() as f64;
    // the seal
    println!("the final count is the last refrain");
    // refrain A returns
    println!("the total is {} in the long tale of old", total);
    // refrain B returns
    println!("the mean is {} and more", avg);
}
```

For other languages, translate the same structure, two refrains, nineteen lines.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
