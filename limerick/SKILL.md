---
name: limerick
description: >-
  Write runnable code in a limerick form: five lines in an AABBA rhyme scheme with a long-short-short-long token rhythm (roughly 8-8-5-5-8) that lands a comic twist in the final line. Activate only for an explicit limerick, five-line comic verse, or AABBA request.
---

# Limerick Skill

A limerick is a five-line comic verse with an AABBA rhyme scheme and a distinctive rhythm: two long lines, two short lines, and a final long line that lands the joke. The first line sets up a character or situation, lines 2-3 build it, and the final line delivers the comic twist. A code limerick is a five-line program shaped ~8-8-5-5-8 tokens: two lines of setup, two quick lines of build, and a closing line that snaps the punchline.

## Philosophy

"A limerick is a joke in five lines: two long, two short, one long landing. The last line is where the laugh is."

The limerick mindset:
1. **Five lines**: exactly five logic lines, shaped ~8-8-5-5-8 tokens (±2 tolerance)
2. **Line 1, 8 tokens**: the setup :  a character, a place, a premise
3. **Lines 2-3, 8 and 5 tokens**: the build :  the work, quickly stated
4. **Line 4, 5 tokens**: the turn :  the twist begins
5. **Line 5, 8 tokens**: the punchline :  the comic landing, the real result
6. **Actually works**: if it doesn't run, the joke has no delivery

## The Punchline: what counts

Line 5 is the whole point :  it must land the comic twist AND resolve the computation. Good code-limerick punchlines:

- **The deflation**: `print(f"so much for {name}")` after a grand setup
- **The reveal**: `print("all that work for a bug")` after a failed check
- **The number**: `print(f"and the answer was {n}")` after elaborate math

Lines 1-4 carry the setup and the work; line 5 delivers the joke and the answer.

## Core Patterns

### The Health Limerick
A grand setup, a quick tally, a deflating verdict:

```python
import json                                # (ceremony is free)
health = json.load(open("health.json"))    # 8: the setup - the services
down = [k for k, v in health.items() if not v]  # 8: the build - the check
up = len(health) - len(down)               # 5: the turn - the tally
print(f"up {up}")                          # 5: the claim - the score
print(f"but {len(down)} are down, the joke's on me")  # 8: the punchline
```

### The Stats Limerick
Elaborate math, anticlimactic answer:

```python
import statistics as st                    # (ceremony is free)
nums = [3, 1, 4, 1, 5, 9, 2, 6]           # 8: the setup - the values
mean = st.mean(nums)                       # 8: the build - the mean
spread = max(nums) - min(nums)             # 5: the turn
print(f"mean {mean:.2f}")                  # 5: the claim
print(f"and yet the spread is {spread}")   # 8: the punchline - the reveal
```

### The Log Limerick
A tired sysadmin's song:

```python
import sys                                 # (ceremony is free)
lines = sys.stdin.read().splitlines()      # 8: the setup - the log
errors = [l for l in lines if "ERR" in l]  # 8: the build - the errors
total = len(lines)                         # 5: the turn
print(f"errors: {len(errors)}")            # 5: the claim
print(f"of {total} lines, what a show")    # 8: the punchline - the scale
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- exactly five lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the limerick actually runs and produces the correct result for the task
- five lines shaped ~8-8-5-5-8 tokens (±2 tolerance per line)
- line 5 delivers a comic twist that is also the real resolution of the computation
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the five visible logic-line token counts against `[8, 8, 5, 5, 8]` with ±2 tolerance, and confirm the final line lands both the joke and the answer; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A limerick without its punchline is five lines of code.

## Boundaries

This skill is not for any five-line program, generic comic code, or code that lacks the AABBA comic structure. Without an explicit limerick request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names limerick, requests a five-line comic verse, or requests an AABBA rhyme structure. Generic coding requests, generic humor, and generic brevity do not activate it without this explicit identity or structural signature.

## The Limerick Aesthetic

Write code that:
- is five lines, shaped ~8-8-5-5-8
- lets line 1 set up the premise and lines 2-4 build it
- ends on the punchline, the comic landing that is also the answer
- keeps the humor dry and the computation real
- imports only what the lines need

## Examples of Limerick Beauty

- **The health song**: setup, check, claim, deflate
- **The stats song**: values, mean, claim, reveal
- **The log song**: source, errors, claim, scale
- **The comic landing**: grand setup, real answer, deflation

## The Limerick Promise

Remember: "A limerick is a joke in five lines: two long, two short, one long landing. The last line is where the laugh is."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const nums = [3, 1, 4, 1, 5, 9, 2, 6];       // 8: the setup - the values
const total = nums.reduce((a, b) => a + b, 0); // 8: the build - the sum
const mean = total / nums.length;            // 5: the turn
console.log(`mean ${mean.toFixed(2)}`);      // 5: the claim
console.log(`but the max is ${Math.max(...nums)}`); // 8: the punchline
```

```rust
fn main() {                                  // ceremony, free
    let nums = [3, 1, 4, 1, 5, 9, 2, 6];     // 8: the setup - the values
    let total: i32 = nums.iter().sum();      // 8: the build - the sum
    let mean = total as f64 / nums.len() as f64;  // 5: the turn
    println!("mean {mean:.2}");              // 5: the claim
    println!("but the max is {}", nums.iter().max().unwrap());  // 8: the punchline
}
```

For other languages, translate the same structure, five lines, comic landing.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
