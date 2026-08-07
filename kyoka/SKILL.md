---
name: kyoka
description: >-
  Write runnable code in a kyoka form: a comic tanka, exactly five logic lines shaped 5-7-5-7-7, where the first three complete the immediate result and the final two land the joke, the parody, or the satirical reframe. Activate only for an explicit kyoka, comic tanka, mad verse, or humorous 5-7-5-7-7 request.
---

# Kyoka Skill

A kyoka is a tanka that laughs. Same five lines, same 5-7-5-7-7 shape, but the soul is comic: the upper phrase sets up something perfectly ordinary, the lower phrase lands a punchline that punctures it. A code kyoka is a five-line program that computes something real and then delivers the joke — the absurd edge case, the embarrassing truth of the data, the self-aware comment on the code itself.

## Philosophy

"A kyoka dresses the joke in the tanka's robes. Five lines, a straight face, and then the turn that makes the reader snort."

The kyoka mindset:
1. **Five lines**: 5-7-5-7-7 tokens, or fewer, never pad
2. **The setup (lines 1-3)**: the real computation, done honestly, with a straight face
3. **The punchline (lines 4-5)**: the comic turn — satire, absurdity, parody, deflation
4. **The joke is true**: the funniest kyoka are the ones the data confirms; the punchline must follow from the computation, not be bolted on
5. **Actually works**: if it doesn't run, the joke dies with it

## The Comic Turn: what counts

The final two lines must land a genuine comic beat, not a wry comment. Good code-kyoka turns:

- **The deflation**: the grand computation reveals something small and human (the "high-performance" cache holds 3 entries)
- **The satire**: the code mirrors a real absurdity of the domain (the validator accepts everything; the "secure" login checks nothing)
- **The parody**: a recognizable pattern performed at the wrong scale (an enterprise pipeline for a 2-item list)
- **The self-aware**: the program comments on its own overkill ("solved in O(n²), n was 4")

The joke must be explainable in one sentence: "the punchline is that...". If you can't finish that sentence, it's not a kyoka.

## Core Patterns

### The Deflation Kyoka
The elaborate computation meets the humble truth:

```python
loads = [1, 1, 2, 1, 1]
spread = max(loads) - min(loads)
peak = max(loads)
print("peak", peak, "spread", spread, "now")
print("load", "balancer", "at", "the", "edge", "of", "fun")
```

### The Satire Kyoka
The validator that validates nothing:

```python
import re
password = "password"                       # setup: the credential
checks = [len(password) > 8, any(c.isdigit() for c in password)]
ok = all(checks)                            # landing: the "secure" gate
print(f"password strength: {'strong' if ok else 'weak'}")
print("entropy: 2.1 bits, feel free to reuse it")
```

### The Self-Aware Kyoka
The over-engineering confesses:

```python
nums = [4]                                  # setup: the dataset
total = sum(nums)                           # turn: the aggregation
avg = total / len(nums)                     # landing: the analytics
print(f"mean: {avg:.2f}")                   # expansion: the report
print("O(n) pipeline complete, n was 1")    # punchline: the scale
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the kyoka form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 5 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the kyoka actually runs and produces the correct result for the task
- lines 1-3 complete the real computation; lines 4-5 land a comic turn (deflation, satire, parody, or self-awareness) that follows from that computation
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the five visible logic-line token counts against `[5, 7, 5, 7, 7]` with ±2 tolerance, and confirm the final two lines land the joke; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A kyoka that doesn't run is just a broken joke, and a kyoka without the comic turn is just a tanka with bad posture.

## Boundaries

This skill is not for any five-line program, generic humor, or compact code that lacks the comic 5-7-5-7-7 setup-and-punchline shape. Without an explicit kyoka request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names kyoka, requests a comic tanka or mad verse, or requests a humorous 5-7-5-7-7 structure. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Kyoka Aesthetic

Write code that:
- is five lines or fewer, no padding
- computes something real in the first three lines, with a straight face
- lands the joke in the last two lines, the turn that reframes line 3
- makes the humor come from the data, never from decoration
- uses a kigo-like seasonal name on the turn line, for flavor
- imports only what the lines need

## Examples of Kyoka Beauty

- **The scale joke**: enterprise machinery, tiny data
- **The honest validator**: the security check that checks nothing
- **The over-engineer**: O(n²) for n = 4, proudly reported
- **The deflation**: the grand total that was 3
- **The self-aware**: the program narrating its own overkill

## The Kyoka Promise

Remember: "A kyoka is a tanka that laughs. Five lines, a real computation, and a punchline that the data itself would sign off on."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const nums = [7];                                  // setup: the workload
const total = nums.reduce((a, b) => a + b, 0);     // turn: the total
const avg = total / nums.length;                   // landing: the mean
console.log(`mean ${avg.toFixed(2)}`);             // expansion: the report
console.log("audited 1 value, variance undefined"); // punchline: the scale
```

```rust
fn main() {                                 // ceremony, free
    let nums = [42];                        // setup: the dataset
    let total: i32 = nums.iter().sum();     // turn: the sum
    let avg = total as f64 / nums.len() as f64;  // landing: the mean
    println!("mean {avg:.2}");              // expansion: the report
    println!("sample size: 1, p-value: vibes"); // punchline: the stats
}
```

For other languages, translate the same structure, honest computation, then the comic turn.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
