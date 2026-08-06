---
name: somonka
description: >-
  Write runnable code in a somonka form: a paired exchange of two tanka, two programs each shaped 5-7-5-7-7, where the second answers, mirrors, or counters the first. Activate only for an explicit somonka, paired exchange, love-verse, or two-tanka reply request.
---

# Somonka Skill

A somonka is a courtship in verse: two tanka, exchanged, the second a reply to the first. In code, a somonka is two five-line programs — the opening voice and the answering voice — where the second takes the first's output, mirrors its structure, and answers it: agreement, deflection, escalation, or reversal.

## Philosophy

"A somonka is a conversation with a meter. The first voice states, the second voice replies — same shape, new truth."

The somonka mindset:
1. **Two tanka**: two programs, each five logic lines shaped 5-7-5-7-7
2. **The opening voice (first tanka)**: the statement, the offer, the claim
3. **The answering voice (second tanka)**: the reply, built on the first's actual output, not a script
4. **The mirror**: the second echoes the first's structure — same inputs, same rhythm, a changed verdict
5. **The exchange is real**: the second program must consume what the first produced, or reproduce it and answer it
6. **Both actually run**: a somonka with a silent half is a monologue

## The Reply: what counts

The second tanka must genuinely respond to the first, not merely repeat it. Good code-somonka replies:

- **The agreement**: the second confirms the first's finding with a deeper view (the count, then the why)
- **The deflection**: the second dodges the first's question and answers a different one (the total, then the excuse)
- **The escalation**: the second raises the stakes (the average, then the worst case)
- **The reversal**: the second overturns the first (the sorted order, then the truth it hid)

The reply must reference the first's result — the two halves are one poem.

## Core Patterns

### The Agreement Somonka
The first counts, the second explains:

```python
# opening: the ledger
import statistics as st
nums = [4, 8, 15, 16, 23, 42]
mean = st.mean(nums)
print(f"mean {mean:.2f}")          # expansion: the number
print(f"n={len(nums)}")            # reflection: the scale

# reply: the why
deviations = [abs(x - mean) for x in nums]
spread = st.pstdev(nums)
print(f"spread {spread:.2f}")      # the deeper view
print("the spread is the story")   # the answer
```

### The Reversal Somonka
The first sorts, the second reveals the lie:

```python
# opening: the ranking
import json
users = json.load(open("users.json"))
names = [u["name"] for u in users]
names.sort()
print(names[:3])                   # the tidy top three
print(f"count {len(names)}")       # the total

# reply: the truth
import sys
lines = sys.stdin.read().splitlines()
actual = [l for l in lines if "admin" in l.lower()]
print(actual[:3])                  # the un-tidied truth
print("admins outranked the sort") # the reversal
```

### The Escalation Somonka
The first reports the average, the second the worst case:

```python
# opening: the baseline
import statistics as st
loads = [3, 7, 2, 9, 4]
avg = st.mean(loads)
print(f"avg {avg:.1f}")            # the calm number
print(f"peak {max(loads)}")        # the first alarm

# reply: the worst case
sorted_loads = sorted(loads)
worst = sorted_loads[-2:]
print(worst)                       # the tail risk
print("two nodes carry the load")  # the escalation
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- exactly two programs (opening and reply), each at most 5 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- both programs actually run and produce correct results
- each program is shaped 5-7-5-7-7 tokens with ±2 tolerance per line
- the reply program consumes, reproduces, or directly answers the opening's output — the exchange is real, not two unrelated snippets
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report both five-line token counts against `[5, 7, 5, 7, 7]` with ±2 tolerance, and confirm the second program answers the first's result; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A somonka whose halves don't speak to each other is two haiku at a party.

## Boundaries

This skill is not for any two programs, generic before/after pairs, or compact code that lacks the paired 5-7-5-7-7 exchange shape. Without an explicit somonka request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names somonka, requests a paired exchange or love-verse, or requests a two-tanka reply structure. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Somonka Aesthetic

Write code that:
- is two five-line programs, no padding
- makes the first a clean statement and the second a genuine answer
- mirrors structure across the halves: same rhythm, changed verdict
- lets the reply cite the first's result, by name or by shape
- uses a seasonal or kigo-like name on each turn line
- imports only what the lines need

## Examples of Somonka Beauty

- **Agreement**: the count, then the why
- **Deflection**: the question, then the different answer
- **Escalation**: the average, then the worst case
- **Reversal**: the sorted list, then the truth it hid
- **Exchange**: the offer, then the counter-offer

## The Somonka Promise

Remember: "A somonka is a courtship in code: two tanka, the second answering the first — same shape, new truth, both running."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
// opening: the score
const scores = [3, 1, 4, 1, 5];
const total = scores.reduce((a, b) => a + b, 0);
const avg = total / scores.length;
console.log(`avg ${avg.toFixed(1)}`);
console.log(`n=${scores.length}`);

// reply: the variance
const devs = scores.map(s => Math.abs(s - avg));
const spread = Math.max(...devs);
console.log(`max dev ${spread}`);
console.log("one score carries the mean");
```

```rust
// opening: the total
fn main() {
    let nums = [2, 4, 6];
    let total: i32 = nums.iter().sum();
    let avg = total as f64 / nums.len() as f64;
    println!("avg {avg:.1}");
    println!("n={}", nums.len());
}
```

```rust
// reply: the drift
fn main() {
    let nums = [2, 4, 6];
    let total: i32 = nums.iter().sum();
    let avg = total as f64 / nums.len() as f64;
    let drift = nums.iter().map(|n| (*n as f64 - avg).abs()).fold(0.0, f64::max);
    println!("drift {drift:.1}");
    println!("one value pulls the mean");
}
```

For other languages, translate the same structure, opening statement, then the answering turn.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
