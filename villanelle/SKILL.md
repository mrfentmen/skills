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
1. **Nineteen lines**: five tercets (1-15) plus a quatrain (16-19), each line ~10 tokens (the iambic pentameter analog)
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
import sys                          # (ceremony is free)
data = sys.stdin.read().splitlines()  # (ceremony is free)

total = len(data)                   # line 1: refrain A - the total
errors = sum(1 for l in data if "ERR" in l)  # line 2: the errors
total = len(data)                   # line 3: refrain B - the total returns
data += ["ERR: late"]               # line 4: new data arrives
errors = sum(1 for l in data if "ERR" in l)  # line 5: the errors grow
total = len(data)                   # line 6: refrain A returns
print(f"total {total}")             # line 7: the state
errors = sum(1 for l in data if "ERR" in l)  # line 8: the errors persist
data = [l for l in data if "WARN" not in l]  # line 9: the filter
total = len(data)                   # line 10: the total shrinks
errors = sum(1 for l in data if "ERR" in l)  # line 11: the errors settle
total = len(data)                   # line 12: refrain A returns
print(f"errors {errors}")           # line 13: the report
data += ["ERR: late"]               # line 14: new data arrives
errors = sum(1 for l in data if "ERR" in l)  # line 15: refrain B returns
total = len(data)                   # line 16: the total settles
rate = errors / max(1, total)       # line 17: the rate
total = len(data)                   # line 18: refrain A returns
print(f"rate {rate:.0%}")           # line 19: the closing word
```

### The Evolving Villanelle
The health check that changes meaning:

```python
import json                         # (ceremony is free)
services = json.load(open("health.json"))   # line 1: refrain A - the state
up = sum(1 for s in services.values() if s)  # line 2: the up count
healthy = all(services.values())    # line 3: refrain B - the verdict
services["cache"] = True            # line 4: the cache recovers
up = sum(1 for s in services.values() if s)  # line 5: the count rises
healthy = all(services.values())    # line 6: refrain A returns
print(f"up {up}")                   # line 7: the state
services["db"] = False              # line 8: the db fails
up = sum(1 for s in services.values() if s)  # line 9: refrain B returns
services["db"] = True               # line 10: the db recovers
up = sum(1 for s in services.values() if s)  # line 11: the count returns
healthy = all(services.values())    # line 12: refrain A returns
print(f"healthy {healthy}")         # line 13: the report
up = sum(1 for s in services.values() if s)  # line 14: the count settles
healthy = all(services.values())    # line 15: refrain B returns
final = "all up" if healthy else f"{len(services)-up} down"  # line 16
print(final)                        # line 17: the verdict
up = sum(1 for s in services.values() if s)  # line 18: refrain A returns
print(f"final: {up} up")            # line 19: the closing word
```

### The Threshold Villanelle
The load check as traffic shifts:

```python
import statistics as st             # (ceremony is free)
loads = [3, 7, 2, 9, 4]             # line 1: refrain A - the data
peak = max(loads)                   # line 2: the peak
avg = st.mean(loads)                # line 3: refrain B - the mean
loads.append(11)                    # line 4: the spike
peak = max(loads)                   # line 5: the new peak
avg = st.mean(loads)                # line 6: refrain A returns
print(f"peak {peak}")               # line 7: the state
loads.pop(0)                        # line 8: the old drops
peak = max(loads)                   # line 9: refrain B returns
loads.append(2)                     # line 10: the calm
peak = max(loads)                   # line 11: the peak falls
avg = st.mean(loads)                # line 12: refrain A returns
print(f"avg {avg:.1f}")             # line 13: the report
peak = max(loads)                   # line 14: the peak settles
avg = st.mean(loads)                # line 15: refrain B returns
spread = peak - avg                 # line 16: the gap
print(f"spread {spread:.1f}")       # line 17: the verdict
peak = max(loads)                   # line 18: refrain A returns
print(f"final peak {peak}")         # line 19: the closing word
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- nineteen lines of code that carry logic, arranged as five tercets and a closing quatrain (language-mandated ceremony like `fn main()` / braces is free; blank-line separators between stanzas are free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the villanelle actually runs and produces the correct result for the task
- two refrain expressions, each recognizably repeated four times at the canonical positions: Refrain A at lines 1, 6, 12, 18; Refrain B at lines 3, 9, 15, 19 (with ±1 line tolerance)
- the non-refrain lines evolve the state so each refrain return sees new data
- each line ~10 tokens with ±3 tolerance (the iambic pentameter analog)
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report nineteen logic-line token counts (~10 each), confirm the two refrains repeat at the canonical positions, and confirm the state evolves between returns; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A villanelle without its refrains is nineteen loose lines.

## Boundaries

This skill is not for any nineteen-line program, generic long code, or code that lacks the repeating-refrain architecture. Without an explicit villanelle request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names villanelle, requests a 19-line structure, or requests a repeating-refrain verse program. Generic coding requests, generic length, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Villanelle Aesthetic

Write code that:
- is nineteen lines in five tercets and a quatrain
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
const nums = [3, 1, 4, 1, 5];               // refrain A: the data
let total = nums.reduce((a, b) => a + b, 0); // the sum
let avg = total / nums.length;               // refrain B: the mean
nums.push(9);                                // the spike
total = nums.reduce((a, b) => a + b, 0);     // refrain A returns
avg = total / nums.length;                   // refrain B returns
console.log(`total ${total}`);               // the report
nums.shift();                                // the old drops
total = nums.reduce((a, b) => a + b, 0);     // refrain A returns
avg = total / nums.length;                   // refrain B returns
console.log(`avg ${avg.toFixed(1)}`);        // the verdict
```

```rust
fn main() {                                  // ceremony, free
    let mut nums = vec![3, 1, 4, 1, 5];      // refrain A: the data
    let mut total: i32 = nums.iter().sum();  // the sum
    let mut avg = total as f64 / nums.len() as f64;  // refrain B: the mean
    nums.push(9);                            // the spike
    total = nums.iter().sum();               // refrain A returns
    avg = total as f64 / nums.len() as f64;  // refrain B returns
    println!("total {total}");               // the report
}
```

For other languages, translate the same structure, two refrains, nineteen lines.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
