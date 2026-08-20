---
name: somonka
description: >-
  Write runnable code in a somonka form: a paired exchange of two tanka, two programs each shaped 5-7-5-7-7, where the second answers, mirrors, or counters the first. Activate only for an explicit somonka, paired exchange, love-verse, or two-tanka reply request.
---

# Somonka Skill

A somonka is a courtship in verse: two tanka, exchanged, the second a reply to the first. In code, a somonka is two five-line programs: the opening voice and the answering voice: where the second takes the first's output, mirrors its structure, and answers it: agreement, deflection, escalation, or reversal.

## Philosophy

"A somonka is a conversation with a meter. The first voice states, the second voice replies: same shape, new truth."

The somonka mindset:
1. **Two tanka**: one file containing exactly two blank-line-separated stanzas, each exactly five logic lines shaped 5-7-5-7-7
2. **The opening voice (first tanka)**: the statement, the offer, the claim
3. **The answering voice (second tanka)**: the reply, built on the first's actual output, not a script
4. **The mirror**: the second echoes the first's structure: same inputs, same rhythm, a changed verdict
5. **The exchange is real**: the second program must consume what the first produced, or reproduce it and answer it
6. **Both actually run**: a somonka with a silent half is a monologue

## The Reply: what counts

The second tanka must genuinely respond to the first, not merely repeat it. Good code-somonka replies:

- **The agreement**: the second confirms the first's finding with a deeper view (the count, then the why)
- **The deflection**: the second dodges the first's question and answers a different one (the total, then the excuse)
- **The escalation**: the second raises the stakes (the average, then the worst case)
- **The reversal**: the second overturns the first (the sorted order, then the truth it hid)

The reply must reference the first's result: the two halves are one poem. The deliverable is exactly two blank-line-separated five-line stanzas, with no executable setup stanza before them. Put any shared input/read/setup inside one of those ten counted lines, and make the reply consume a named result established by the opening.

## Core Patterns

### The Agreement Somonka
The first counts, the second explains:

```python
nums = [3, 1, 4, 1, 5]
mean = sum(nums) / len(nums)
print("count", len(nums), "nums", "arrive")
print("mean", mean, "is", "the", "ask")
print("reply", "with", "the", "spread", "now")

spread = max(nums) - min(nums)
answer = f"mean {mean} and spread {spread}"
print("one", "value", "pulls", "the", "mean")
print("the", "rest", "huddle", "near", "the", "sum")
print("reply", answer, "and", "done", "now")
```

### The Reversal Somonka
The first sorts, the second reveals the lie:

```python
nums = [3, 1, 4, 1, 5]
order = sorted(nums); low = order[0]
print("sorted", "clean", "from", "low")
print("ascending", "all", "the", "way", "down")
print("order", order, "tells", "the", "tale")

rev = order[::-1]
print("reverse", "the", "order", "reveals", "the", "lie")
print("the", "mean", "hides", "the", "tails")
print("sorted", "clean", "is", "the", "first", "act")
print("now", "descending", "states", "the", "truth")
```

### The Escalation Somonka
The first reports the average, the second the worst case:

```python
import statistics as st
loads = [3, 7, 2, 9, 4]
avg = st.mean(loads); peak = max(loads)
print("avg", f"{avg:.1f}", "now")
print("peak", peak, "is", "the", "first", "alarm")
print("count", len(loads), "loads", "arrive", "now")

worst = sorted(loads)[-2:]
tail = sum(worst) / len(worst)
print("worst", worst, "the", "tail")
print("two", "nodes", "carry", "the", "load")
print("reply", "with", "the", "worst", "case")
```

## Workflow

1. **Write it plainly.** Implement the task ordinarily and run it until the output is right. No form pressure yet.
2. **Start from the ten-slot template.** Copy the proven two-stanza template below before adapting the task. Keep exactly five logic lines in the opening stanza, one blank line, and exactly five logic lines in the reply stanza. Do not invent the stanza boundary while solving the task.
3. **Fill real work into the slots.** Preserve the line breaks and keep each stanza near `[5, 7, 5, 7, 7]` whitespace tokens. Change expressions or string contents only when needed for the task; never delete a slot, merge lines, or add filler.
4. **Verify the form and result.** Run the program with the real input, then run `scripts/rhythm_check.py solve.py`. If the checker fails, use its reported two profiles to revise the specific lines while preserving the ten-slot structure. Repeat until both the output and form pass.
5. **Report the counts.** State both five-line token profiles and explain how the reply uses the opening result.

## Proven Ten-Slot Template

This template is intentionally concrete because models reliably preserve a demonstrated shape better than they invent ten exact rhythmic lines. Replace the expressions with task-specific real work, but preserve the two stanzas, line count, and approximate token profile:

```python
data = input().split()
nums = [int(x) for x in data]
total = sum(nums)
first = f"count {len(nums)} numbers arrive"
print(first, "count", len(nums), "now", total)

reply = f"sum {total}"
mirror = total + len(nums)
answer = f"sum {total} now"
result = f"{reply} and {answer}"
print(result, "reply", mirror, "done", total)
```

The template's profiles are approximately `[3, 7, 3, 6, 5]` and `[4, 5, 5, 5, 5]`, all within the documented ±2 tolerance. The first stanza establishes a named result; the second stanza reuses it and answers it. If a task needs different data, retain the same role sequence: read, parse, compute, state, print; then reference, transform, answer, combine, print.


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

- exactly two blank-line-separated stanzas in one deliverable file: an opening stanza and a reply stanza, each exactly 5 logic-carrying lines; language-mandated ceremony may surround a stanza but cannot replace, add to, or merge its five lines
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- both programs actually run and produce correct results
- each program is shaped 5-7-5-7-7 tokens with ±2 tolerance per line
- the reply program consumes, reproduces, or directly answers the opening's output: the exchange is real, not two unrelated snippets
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

Remember: "A somonka is a courtship in code: two tanka, the second answering the first: same shape, new truth, both running."

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
    let drift = nums.iter().map(|n| (*n as f64 - avg).abs()).fold(0.0, f64:max);
    println!("drift {drift:.1}");
    println!("one value pulls the mean");
}
```

For other languages, translate the same structure, opening statement, then the answering turn.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
