---
name: cinquain
description: >-
  Write runnable code in a cinquain form: five lines shaped 2-4-6-8-2 tokens, a pyramid that builds to a wide middle and lands on a two-token closing word. Activate only for an explicit cinquain, 2-4-6-8-2, or pyramid-shaped request.
---

# Cinquain Skill

A cinquain is a five-line Western form with a fixed shape: 2-4-6-8-2 syllables, a pyramid that swells to its widest line and collapses to a two-syllable landing. A code cinquain is a five-line program shaped 2-4-6-8-2 tokens: a two-token opener, a growing middle, and a two-token final word that closes the whole thing.

## Philosophy

"A cinquain is a pyramid in five lines: it swells to eight, then lands on two. The shape is the poem."

The cinquain mindset:
1. **Five lines**: exactly five logic lines, shaped 2-4-6-8-2 tokens (±1 tolerance per line)
2. **Line 1, 2 tokens**: the opener, the seed
3. **Lines 2-3, 4-6 tokens**: the growing body, the work expanding
4. **Line 4, 8 tokens**: the widest line, the full computation
5. **Line 5, 2 tokens**: the landing, a two-token word that closes it
6. **Actually works**: if it doesn't run, the pyramid has no base

## The Shape: what counts

The 2-4-6-8-2 silhouette must be visible in the token counts. The final two-token line is the signature :  a short landing that names or seals the result. Good code-cinquain landings:

- **The name**: `print("done")` or `print(total)`
- **The seal**: `sys.exit(0)` or `print("ok")`
- **The verdict**: `print(mean)` or `print("up")`

The wide line 4 carries the real computation; the landing closes it.

## Core Patterns

### The Tally Cinquain
The count that builds and lands:

```python
import re, sys                 # (ceremony is free)
text = sys.stdin.read()        # 2: the source
words = re.findall(r"\S+", text)   # 4: the tokens
errors = [w for w in words if "ERR" in w]  # 6: the errors
print(f"{len(errors)} errors in {len(words)} words")  # 8: the report
print(len(errors))             # 2: the landing
```

### The Stats Cinquain
The mean that builds and lands:

```python
import statistics as st        # (ceremony is free)
nums = [3, 1, 4, 1, 5, 9, 2]   # 4: the values
mean = st.mean(nums)           # 4: the mean
spread = max(nums) - min(nums)  # 6: the spread
print(f"mean {mean:.1f} spread {spread}")  # 8: the report
print(f"{mean:.1f}")           # 2: the landing
```

### The Health Cinquain
The check that builds and lands:

```python
import json                    # (ceremony is free)
data = json.load(open("health.json"))  # 4: the state
down = [k for k, v in data.items() if not v]  # 6: the failures
print(f"down: {', '.join(down) or 'none'}")  # 8: the report
print(len(down))               # 2: the landing
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- exactly five lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the cinquain actually runs and produces the correct result for the task
- five lines shaped 2-4-6-8-2 tokens (±1 tolerance per line)
- line 4 (the widest) carries the core computation; line 5 (the two-token landing) names or seals the result
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the five visible logic-line token counts against `[2, 4, 6, 8, 2]` with ±1 tolerance, and confirm the two-token landing closes the computation; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A cinquain without its pyramid is five loose lines.

## Boundaries

This skill is not for any five-line program, generic compact code, or code that lacks the 2-4-6-8-2 pyramid shape. Without an explicit cinquain request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names cinquain, requests a 2-4-6-8-2 structure, or requests a pyramid-shaped verse program. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Cinquain Aesthetic

Write code that:
- is five lines, shaped 2-4-6-8-2
- swells to the wide line 4, then lands on two tokens
- makes the landing the seal: a name, a verdict, a number
- imports only what the lines need

## Examples of Cinquain Beauty

- **The tally**: count the errors, land the number
- **The stats**: mean and spread, land the mean
- **The health**: the down list, land the count
- **The pyramid**: build to eight, land on two

## The Cinquain Promise

Remember: "A cinquain is a pyramid in five lines: it swells to eight, then lands on two. The shape is the poem."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const nums = [3, 1, 4, 1, 5];                    // 4: the values
const total = nums.reduce((a, b) => a + b, 0);   // 4: the sum
const mean = total / nums.length;                // 6: the mean
console.log(`mean ${mean.toFixed(1)}`);          // 8: the report
console.log(mean.toFixed(1));                    // 2: the landing
```

```rust
fn main() {                                      // ceremony, free
    let nums = [3, 1, 4, 1, 5];                  // 4: the values
    let total: i32 = nums.iter().sum();          // 4: the sum
    let mean = total as f64 / nums.len() as f64; // 6: the mean
    println!("mean {mean:.1}");                  // 8: the report
    println!("{mean:.1}");                       // 2: the landing
}
```

For other languages, translate the same structure, five lines, pyramid to a two-token landing.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
