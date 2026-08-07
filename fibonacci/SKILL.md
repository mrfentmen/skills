---
name: fibonacci
description: >-
  Write runnable code in a fibonacci poem form: lines whose token counts follow the Fibonacci sequence (1, 1, 2, 3, 5, 8, 13...), each line the sum of the two before it, growing until the computation resolves. Activate only for an explicit fibonacci poem, golden-ratio verse, or growing-sequence request.
---

# Fibonacci Skill

A fibonacci poem is a modern Western form whose lines follow the Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13... syllables, each line the sum of the two that preceded it. A code fibonacci poem is a program whose logic-line token counts follow the same sequence :  1, 1, 2, 3, 5, 8, 13... :  each line growing from the sum of the previous two, until the computation resolves.

## Philosophy

"A fibonacci poem grows the way nature grows: one, one, two, three, five, eight, thirteen. Each line is the sum of the two before it."

The fibonacci mindset:
1. **The sequence**: logic-line token counts follow 1, 1, 2, 3, 5, 8, 13... (Fibonacci), each count the sum of the previous two
2. **The growth**: the lines expand naturally, from a single token to the full computation
3. **The resolution**: the poem ends when the task is done :  6-8 lines is typical, and the final line carries the result
4. **The proportion**: long lines appear only after the earlier lines earned them
5. **Actually works**: if it doesn't run, the sequence was just numbers

## The Sequence: what counts

The token counts of consecutive logic lines must follow the Fibonacci progression: 1, 1, 2, 3, 5, 8, 13, 21... Each count equals the sum of the previous two (±1 tolerance per line). The sequence must start at the beginning (1, 1, 2...) :  the growth pattern is the form. Good code-fibonacci shapes:

- **Short**: 1, 1, 2, 3, 5, 8 (six lines, a complete small task)
- **Full**: 1, 1, 2, 3, 5, 8, 13 (seven lines, a fuller computation)
- **Long**: 1, 1, 2, 3, 5, 8, 13, 21 (eight lines, the max practical for AI)

## Core Patterns

### The Sum Fibonacci
The growing count that lands on the total (the annotated counts are the target rhythm, a 2-3-5-8 tail of the sequence):

```python
pass
s = 0
s = 1
total = s
print(s, "then", total)
print("sum", s + total, "of", "the", "count")
```

### The Stats Fibonacci
The sequence that grows to the mean:

```python
import sys                      # 2: the tool
nums = [int(x) for x in sys.stdin.read().split()]  # 3: the values
total = sum(nums)               # 5: the sum
print(f"{total / len(nums):.1f} mean of {len(nums)}")  # 8: the report
```

### The Health Fibonacci
The growing check that lands on the verdict:

```python
import json                     # 2: the tool
h = json.load(open("health.json"))  # 3: the state
down = [k for k, v in h.items() if not v]  # 5: the failures
print(f"{len(down)} down of {len(h)}")  # 8: the verdict
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the fibonacci form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

- 6-8 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free; imports are free ceremony)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the fibonacci poem actually runs and produces the correct result for the task
- the logic-line token counts follow the Fibonacci sequence (1, 1, 2, 3, 5, 8, 13...), each count the sum of the previous two; short 6-8 line poems typically use a contiguous tail of the sequence such as 2, 3, 5, 8 (±1 tolerance per line)
- each line's count is the sum of the previous two :  the growth is the form
- the final line carries or seals the result
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the logic-line token counts and confirm they follow 1, 1, 2, 3, 5, 8... (±1 per line); diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A fibonacci poem that doesn't grow is just a list of numbers.

## Boundaries

This skill is not for any growing program, generic compact code, or code that lacks the Fibonacci token-count progression. Without an explicit fibonacci poem request or that structural contract, handle the request normally. When the request is about computing Fibonacci numbers (not the poem form), handle it as ordinary code.

## Activation

Activate this skill only when the user explicitly names fibonacci poem, requests golden-ratio verse, or requests a growing-sequence program. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Fibonacci Aesthetic

Write code that:
- grows its lines in the Fibonacci sequence, 2-3-5-8 (or the full 1-1-2-3-5-8)
- lets each line earn the length of the next
- ends on a line that carries or seals the result
- uses the golden proportion as the shape of the poem
- imports only what the lines need

## Examples of Fibonacci Beauty

- **The count**: source, filter, report, seal
- **The stats**: values, sum, mean, report
- **The health**: state, failures, verdict
- **The growth**: one, one, two, three, five, eight

## The Fibonacci Promise

Remember: "A fibonacci poem grows the way nature grows :  one, one, two, three, five, eight :  and the last line carries the result."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const nums = [3, 1, 4, 1, 5];                 // 3: the values
const total = nums.reduce((a, b) => a + b, 0); // 5: the sum
const mean = total / nums.length;             // 5: the mean
console.log(`mean ${mean.toFixed(1)}`);       // 8: the report
console.log("settled");                       // 3: the seal
console.log("done");                          // 2: the close
```

```rust
fn main() {                                   // ceremony, free
    let nums = [3, 1, 4, 1, 5];               // 3: the values
    let total: i32 = nums.iter().sum();       // 5: the sum
    let mean = total as f64 / nums.len() as f64;  // 5: the mean
    println!("mean {mean:.1}");               // 8: the report
    println!("settled");                      // 3: the seal
    println!("done");                         // 2: the close
}
```

For other languages, translate the same structure, growing token counts in the Fibonacci sequence.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
