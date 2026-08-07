---
name: bussokusekika
description: >-
  Write runnable code in a bussokusekika form: exactly six logic lines shaped 5-7-5-7-7-7, a meditation that builds through three long closing lines to a settled, final truth. Activate only for an explicit bussokusekika, 5-7-5-7-7-7, footprint verse, or six-line meditation request.
---

# Bussokusekika Skill

A bussokusekika is an ancient Japanese verse carved on the Buddha's footprint stone at Yakushi-ji: six lines, 5-7-5-7-7-7, a poem that begins like a tanka and then adds a seventh-moment coda that settles the whole thing. A code bussokusekika is a six-line program: the core task in the first three lines, a deepening in lines 4-5, and a final line that lands like a stone — the closing truth, the settled verdict.

## Philosophy

"A bussokusekika is a tanka that refuses to end. Five lines build, the sixth line seals."

The bussokusekika mindset:
1. **Six lines**: 5-7-5-7-7-7 tokens, or fewer, never pad
2. **Lines 1-3, 5-7-5**: the setup, the dense turn, the landing of the core task
3. **Lines 4-5, 7-7**: the deepening, a second and third view of the result
4. **Line 6, 7 tokens**: the seal — the final, settled line that the first five were building toward; it does not add a new idea, it confirms and closes
5. **Actually works**: if it doesn't run, it's not carved in anything

## The Seal: what counts

The sixth line is what makes it a bussokusekika instead of a tanka. It must feel inevitable — the line the poem was heading toward all along. Good code seals:

- **The confirmation**: the last line states plainly what the numbers implied (the trend, named at last)
- **The threshold**: the final line checks the result against a boundary and says what it means (above the line, or not)
- **The verdict**: the last line issues the judgment the computation was gathering evidence for
- **The name**: the final line names the thing the whole program circled

The seal must not introduce new machinery; it draws the conclusion the previous five lines already earned.

## Core Patterns

### The Verdict Bussokusekika
The evidence, then the judgment:

```python
nums = [3, 1, 4, 1, 5]
mean = sum(nums) / len(nums)
spread = max(nums) - min(nums)
print("mean", mean, "and", "the", "spread")
print("and", "the", "sum", "of", "all", "is", "here")
print("six", "lines", "and", "the", "poem", "is", "done")
```

### The Threshold Bussokusekika
The measure, then the judgment against the line:

```python
import json
cfg = json.load(open("config.json"))     # setup: the configuration
required = {"host", "port", "token"}     # turn: the contract
present = required & set(cfg)            # landing: the overlap
missing = required - present             # deepening: the gaps
ratio = len(present) / len(required)     # deepening: the score
print(f"config {ratio:.0%} complete, missing {sorted(missing)}")  # the seal: the judgment
```

### The Naming Bussokusekika
The pattern, then the name:

```python
import re, sys
text = sys.stdin.read().lower()          # setup: the corpus
words = re.findall(r"[a-z']+", text)     # turn: the tokens
from collections import Counter
counts = Counter(words)                  # landing: the tally
top = counts.most_common(1)[0]           # deepening: the leader
share = top[1] / max(1, len(words))      # deepening: the weight
print(f"'{top[0]}' is {share:.0%} of all words")  # the seal: the name
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the bussokusekika form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- exactly 6 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the bussokusekika actually runs and produces the correct result for the task
- lines 1-3 complete the core task; lines 4-5 deepen it; line 6 seals it with a verdict, threshold judgment, or name that the previous lines earned
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the six visible logic-line token counts against `[5, 7, 5, 7, 7, 7]` with ±2 tolerance, and confirm the sixth line seals the result without new machinery; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A bussokusekika without its seal is just a long tanka.

## Boundaries

This skill is not for any six-line program, generic verbose code, or compact code that lacks the sealing 5-7-5-7-7-7 shape. Without an explicit bussokusekika request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names bussokusekika, requests a 5-7-5-7-7-7 structure, footprint verse, or six-line meditation. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Bussokusekika Aesthetic

Write code that:
- is six lines, no padding
- builds the core task in the first three lines, deepens in the next two
- ends with a seal line that settles, confirms, or names — no new machinery
- lets the final line feel inevitable, the verdict the data was earning
- uses a kigo-like seasonal name on the turn line
- imports only what the lines need

## Examples of Bussokusekika Beauty

- **The verdict**: evidence, then judgment
- **The threshold**: measure, then the line it crossed
- **The naming**: the pattern, then its name
- **The settle**: the argument, then the peace
- **The carve**: the computation, then the stone

## The Bussokusekika Promise

Remember: "A bussokusekika is a tanka that refuses to end. Five lines build the case, the sixth line carves the verdict."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const vals = [5, 3, 9, 1, 7];              // setup: the values
const total = vals.reduce((a, b) => a + b, 0);  // turn: the sum
const mean = total / vals.length;          // landing: the mean
const hi = Math.max(...vals);              // deepening: the peak
const gap = hi - mean;                     // deepening: the gap
console.log(`mean ${mean.toFixed(1)}, peak gap ${gap.toFixed(1)}`);  // the seal
```

```rust
fn main() {                                // ceremony, free
    let vals = [5, 3, 9, 1, 7];            // setup: the values
    let total: i32 = vals.iter().sum();    // turn: the sum
    let mean = total as f64 / vals.len() as f64;  // landing: the mean
    let hi = *vals.iter().max().unwrap();  // deepening: the peak
    let gap = hi as f64 - mean;            // deepening: the gap
    println!("mean {mean:.1}, gap {gap:.1}");     // the seal
}
```

For other languages, translate the same structure, setup, turn, landing, deepening, seal.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
