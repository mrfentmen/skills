---
name: zappai
description: >-
  Write runnable code in a zappai form: a haiku-shaped poem freed from haiku's rules: no seasonal kigo required, no cutting word required, just three lines of roughly 5-7-5 tokens that land a single vivid moment. Activate only for an explicit zappai, free haiku, or unconstrained three-line moment request.
---

# Zappai Skill

A zappai is a haiku-shaped poem that refuses haiku's discipline: same three lines, same rough 5-7-5 rhythm, but no kigo (season word) required, no kireji (cutting word) required. It is the haiku of the moment, unlicensed. A code zappai is a three-line program that does the task in three lines and lands the moment: the snapshot, the observation, the small truth: without ceremony.

## Philosophy

"A zappai is a haiku off duty. Three lines, a moment, no season required."

The zappai mindset:
1. **Three lines**: exactly three logic lines, roughly 5-7-5 tokens, or fewer, never pad
2. **No kigo required**: the subject can be anything: code, config, weather, traffic, a stack trace
3. **No kireji required**: the cutting pause is optional; the moment just needs to land
4. **The moment**: the third line should deliver the observation the first two earned
5. **Actually works**: if it doesn't run, it's a moment that never happened

## The Moment: what counts

The zappai's third line must land like a snapshot: a single observation that completes the picture. It does not need to be profound; it needs to be true and complete. Good code-zappai moments:

- **The observation**: the number that summarizes the mess (the 3 errors in 200 lines)
- **The snapshot**: the state of the system at a single instant (the cache with 2 entries)
- **The small truth**: the humble finding (the config key that was misspelled)

The three lines should read as one breath: do the work, show the work, land the moment.

## Core Patterns

### The Snapshot Zappai
The state, the moment:

```python
import sys
data = [int(x) for x in sys.stdin.read().split()]
print("max", max(data), "and", "the", "loud")
print("one", "calls", "it", "now")
```

### The Observation Zappai
The count, the truth:

```python
import re
log = open("app.log").read()                # the source
errs = len(re.findall(r"ERROR", log))       # the count
print(f"{errs} errors, {len(log.splitlines())} lines")  # the moment
```

### The Small Truth Zappai
The find, the truth:

```python
import json
cfg = json.load(open("config.json"))  # the load
keys = set(cfg.keys())  # the keys
print(f"keys: {sorted(keys)}")  # the moment
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the zappai form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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
- the zappai actually runs and produces the correct result for the task
- three lines roughly 5-7-5 tokens (±2 tolerance per line)
- the third line lands a moment: an observation, snapshot, or small truth that the first two lines earned
- no kigo or kireji requirements: the moment stands alone
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the three visible logic-line token counts against `[5, 7, 5]` with ±2 tolerance, and confirm the third line lands the moment; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A zappai that doesn't land its moment is just three lines of code.

## Boundaries

This skill is not for any three-line program, generic compact code, or code that lacks the haiku-shaped moment. Without an explicit zappai request or that structural contract, handle the request normally. When the request explicitly asks for haiku discipline (kigo, kireji, season), the haiku skill applies instead.

## Activation

Activate this skill only when the user explicitly names zappai, requests a free haiku or unconstrained three-line moment, or requests haiku shape without haiku rules. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Zappai Aesthetic

Write code that:
- is three lines, no padding
- does the work in the first two lines, lands the moment in the third
- needs no season, no cutting word, no ceremony
- lets the moment be small and true: a snapshot, an observation, a count
- imports only what the lines need

## Examples of Zappai Beauty

- **The snapshot**: the system at one instant
- **The count**: the errors in the log
- **The small truth**: the misspelled key
- **The moment**: the observation that completes the picture

## The Zappai Promise

Remember: "A zappai is a haiku off duty: three lines, a moment, no season required, and the code runs."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
// the load
const data = JSON.parse(process.stdin.read() || "{}");
// the check
const down = Object.entries(data).filter(([, v]) => !v).map(([k]) => k);
// the moment
console.log(`down: ${down.join(", ") || "none"}`);
```

```rust
fn main() {
    // the values
    let vals = [3, 1, 4];
    // the sum
    let total: i32 = vals.iter().sum();
    // the moment
    println!("the total is {total}");
}
```

For other languages, translate the same structure, three lines, the moment in the third.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
