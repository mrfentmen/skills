---
name: sonnet
description: >-
  Write runnable code in a sonnet form: fourteen logic lines in three quatrains and a couplet (or an octave and sestet), each line ~10 tokens in iambic rhythm, with a volta that turns the poem before the final couplet resolves it. Activate only for an explicit sonnet, 14-line, iambic, or English verse-form request.
---

# Sonnet Skill

A sonnet is a fourteen-line English poem with a fixed architecture: three quatrains building an argument, a volta (the turn) before the final couplet, and the couplet resolving the whole. A code sonnet is a fourteen-line program: three four-line movements that each advance the computation, a turn, and a final two-line resolution.

## Philosophy

"A sonnet is an argument in fourteen lines. Three quatrains build the case, the volta turns it, and the couplet closes it."

The sonnet mindset:
1. **Fourteen lines**: exactly fourteen logic lines, each ~10 tokens (the iambic pentameter analog: ten beats, five stresses), or fewer, never pad
2. **Quatrain 1 (lines 1-4)**: the setup, the world as given
3. **Quatrain 2 (lines 5-8)**: the development, the work
4. **Quatrain 3 (lines 9-12)**: the deepening, the evidence piling up
5. **The volta (around line 9-12)**: the turn — the change of angle, the "but"
6. **The couplet (lines 13-14)**: the resolution — two lines that settle the argument
7. **Actually works**: if it doesn't run, the sonnet is just fourteen broken lines

## The Volta: what counts

The volta is the sonnet's engine: the turn where the argument shifts — from problem to insight, from observation to judgment, from accumulation to revelation. In code, the volta is the line where the computation changes what it's looking at. Good code-sonnet voltas:

- **The contrast**: the pattern, then the exception to it
- **The reveal**: the aggregate, then the outlier behind it
- **The reframe**: the computation's result, then what it actually means
- **The shift**: the data as collected, then the data as it should be judged

The couplet must resolve: two final lines that state plainly what the fourteen lines were establishing.

## Core Patterns

### The Contrast Sonnet
The pattern, the exception, the verdict:

```python
print("the", "health", "of", "the", "fleet", "is", "the", "first", "truth")
print("up", sum(v for v in json.load(open("health.json")).values() if v), "now")
print("down", len(json.load(open("health.json"))) - sum(v for v in json.load(open("health.json")).values() if v), "left")
print("the", "second", "quatrain", "turns", "to", "the", "working", "load")
print("the", "mean", "is", "the", "sum", "over", "the", "count", "here")
print("ratio", "of", "up", "to", "all", "is", "the", "measure", "now")
print("and", "the", "third", "quatrain", "deepens", "the", "evidence", "pile")
print("errors", "in", "the", "logs", "are", "the", "quiet", "tale")
print("warnings", "count", "too", "and", "shape", "the", "final", "view")
print("the", "volta", "turns", "the", "argument", "at", "the", "ninth", "line")
print("and", "the", "couplet", "settles", "the", "whole", "affair", "in")
print("two", "final", "lines", "that", "state", "the", "verdict", "now")
print("the", "fleet", "is", "up", "and", "the", "tale", "is", "told")
print("and", "the", "sonnet", "ends", "with", "the", "resolve", "done")
```

### The Reveal Sonnet
The aggregate, then the truth it hid:

```python
import json, sys                             # quatrain 1: the setup
data = json.load(sys.stdin)                  # quatrain 1: the load
prices = [d["price"] for d in data]          # quatrain 1: the prices
total = sum(prices)                          # quatrain 1: the sum
avg = total / max(1, len(prices))            # quatrain 2: the average
under = sum(1 for p in prices if p < avg)    # quatrain 2: the under
over = sum(1 for p in prices if p > avg)     # quatrain 2: the over
print(f"avg {avg:.2f}")                      # quatrain 3: the report
print(f"{under} below, {over} above")        # quatrain 3: the split
median_p = sorted(prices)[len(prices)//2]    # the volta: the middle
print(f"median {median_p}")                  # the couplet: the truth
print("most prices sit under the mean")      # the couplet: the resolve
```

### The Reframe Sonnet
The computation, then its meaning:

```python
import re                                    # quatrain 1: the setup
log = open("app.log").read()                 # quatrain 1: the source
lines = log.splitlines()                     # quatrain 1: the lines
total_l = len(lines)                         # quatrain 1: the count
errs = [l for l in lines if "ERROR" in l]    # quatrain 2: the errors
n_err = len(errs)                            # quatrain 2: the number
rate = n_err / max(1, total_l)               # quatrain 2: the rate
print(f"{total_l} lines, {n_err} errors")    # quatrain 3: the report
print(f"error rate {rate:.1%}")              # quatrain 3: the ratio
healthy = rate < 0.05                        # the volta: the judgment
print("the system is " + ("healthy" if healthy else "degraded"))  # the couplet
print(f"fix the {sorted(set(e.split(' ')[0] for e in errs))[:3]}")  # the couplet: the resolve
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the sonnet form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- fourteen lines of code that carry logic, in three quatrains plus a couplet (language-mandated ceremony like `fn main()` / braces is free; blank-line separators between quatrains are free)
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
- is fourteen lines in three quatrains and a couplet
- builds the argument in the quatrains, one movement per four lines
- turns with a volta near line 9-12 — the "but" that changes the reading
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
const vals = [4, 8, 15, 16, 23, 42];            // quatrain 1
const mean = vals.reduce((a, b) => a + b, 0) / vals.length;  // quatrain 1
const devs = vals.map(v => Math.abs(v - mean));  // quatrain 2
const big = Math.max(...devs);                   // quatrain 2
console.log(`mean ${mean.toFixed(1)}`);          // quatrain 3
console.log(`max deviation ${big.toFixed(1)}`);  // quatrain 3
const skewed = big > (mean / 2);                 // the volta
console.log(skewed ? "the mean is a lie" : "the mean holds");  // the couplet
console.log("one value carries the set");        // the couplet
```

```rust
fn main() {                                      // ceremony, free
    let vals = [4, 8, 15, 16, 23, 42];           // quatrain 1
    let total: i32 = vals.iter().sum();          // quatrain 1
    let mean = total as f64 / vals.len() as f64; // quatrain 2
    let big = vals.iter().map(|v| (*v as f64 - mean).abs()).fold(0.0, f64::max);  // quatrain 2
    println!("mean {mean:.1}");                  // quatrain 3
    println!("max dev {big:.1}");                // quatrain 3
    let skewed = big > mean / 2.0;               // the volta
    println!("{}", if skewed { "mean is a lie" } else { "mean holds" });  // the couplet
    println!("one value carries the set");       // the couplet
}
```

For other languages, translate the same structure, fourteen lines, quatrains, volta, couplet.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
