---
name: renshi
description: >-
  Write runnable code in a renshi form: a chain of linked verses, multiple short stages each passing a torch to the next, the output of one stage feeding the next in a modern collaborative chain. Activate only for an explicit renshi, linked verse chain, or relay-style multi-stage request.
---

# Renshi Skill

A renshi is modern linked verse: several poets writing connected stanzas, each taking the last line of the previous and continuing it. A code renshi is a chain of short stages: each stage a small program (2-3 lines) that consumes the previous stage's output and hands a transformed value to the next. The chain is the poem.

## Philosophy

"A renshi is a relay. Each runner takes the baton the previous one passed and carries it further."

The renshi mindset:
1. **A chain of stages**: 3-6 stages, each 2-3 logic lines (shorter is truer to the form)
2. **The torch**: each stage's final value feeds the next stage's first statement
3. **The link**: stage N+1 names or consumes what stage N produced: the chain is visible, not hidden
4. **The evolution**: the value transforms as it passes: raw data → parsed → filtered → summarized → judged
5. **Each stage runs**: the whole chain is one program; if one link breaks, the poem dies

## The Chain: what counts

Each stage must visibly consume the previous stage's result: by variable, by pipe, or by function composition. The chain is the structure; readers should be able to trace the baton from stage 1 to the final line. Good code-renshi links:

- **The parse chain**: raw text → tokens → counts → top word
- **The pipeline**: input → validate → transform → aggregate → report
- **The relay**: each stage's last expression named as the next stage's input

## Core Patterns

### The Parse Renshi
The chain that reads:

```python
import sys
raw = sys.stdin.read()
tokens = raw.split()

count = len(tokens)
print("count", count)

print("first", "three", "tokens", "are", "the")
print("start", "of", "the", "linked", "verse")
```

### The Pipeline Renshi
The chain that transforms:

```python
import json
raw = open("events.json").read()
events = json.loads(raw)

failed = [e for e in events if not e.get("ok")]
ids = [e["id"] for e in failed]

print("failed:", ids)
print("and", "the", "verse", "ends", "here")
```

### The Relay Renshi
The chain that accumulates:

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
total = sum(nums)
mean = total / len(nums)

devs = [abs(n - mean) for n in nums]
spread = sum(devs) / len(devs)

print(f"mean {mean:.1f}, dev {spread:.1f}")
print("and", "the", "verse", "ends", "here")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the renshi form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

- 3-6 visible stages, each 2-3 lines of logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the renshi actually runs and produces the correct result for the task
- each stage visibly consumes the previous stage's output: the chain is traceable
- the value evolves through the chain: raw to parsed to filtered to summarized
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: confirm 3-6 visible stages where each stage names or consumes the previous stage's value, and confirm the final stage lands the result; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A renshi whose stages don't link is a list of one-liners.

## Boundaries

This skill is not for any multi-line program, generic pipelines, or code that lacks the visible linked-stage chain. Without an explicit renshi request or that structural contract, handle the request normally. When the request explicitly asks for classical linked renga with strict alternating 5-7-5/7-7 meter, the renga skill applies instead.

## Activation

Activate this skill only when the user explicitly names renshi, requests modern linked verse, or requests a relay-style multi-stage chain. Generic coding requests, generic pipelines, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Renshi Aesthetic

Write code that:
- is a chain of short stages, each passing the baton
- makes the links visible: each stage names what it received
- lets the value evolve through the chain, raw to refined
- ends on a final verse that the whole chain earned
- imports only what the lines need

## Examples of Renshi Beauty

- **The parse chain**: text → tokens → counts → leader
- **The pipeline**: raw → parse → filter → extract → report
- **The relay**: values → sum → mean → spread → verse
- **The evolution**: each stage transforms the baton

## The Renshi Promise

Remember: "A renshi is a relay in code: each stage takes the baton the last one passed, transforms it, and hands it on: and the whole chain runs."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const raw = process.stdin.read();                // stage 1
const events = JSON.parse(raw);                  // stage 2
const failed = events.filter(e => !e.ok);        // stage 3
const ids = failed.map(e => e.id);               // stage 4
console.log(`failed: ${ids.join(', ')}`);        // stage 5
```

```rust
fn main() {                                      // ceremony, free
    let nums = [3, 1, 4, 1, 5, 9, 2, 6];         // stage 1
    let total: i32 = nums.iter().sum();          // stage 2
    let mean = total as f64 / nums.len() as f64; // stage 3
    let spread: f64 = nums.iter().map(|n| (*n as f64 - mean).powi(2)).sum:<f64>() / nums.len() as f64;  // stage 4
    println!("mean {mean:.1} var {spread:.1}");  // stage 5
}
```

For other languages, translate the same structure, a visible chain of short stages.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
