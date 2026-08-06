---
name: renshi
description: >-
  Write runnable code in a renshi form: a chain of linked verses, multiple short stages each passing a torch to the next, the output of one stage feeding the next in a modern collaborative chain. Activate only for an explicit renshi, linked verse chain, or relay-style multi-stage request.
---

# Renshi Skill

A renshi is modern linked verse: several poets writing connected stanzas, each taking the last line of the previous and continuing it. A code renshi is a chain of short stages — each stage a small program (2-3 lines) that consumes the previous stage's output and hands a transformed value to the next. The chain is the poem.

## Philosophy

"A renshi is a relay. Each runner takes the baton the previous one passed and carries it further."

The renshi mindset:
1. **A chain of stages**: 3-6 stages, each 2-3 logic lines (shorter is truer to the form)
2. **The torch**: each stage's final value feeds the next stage's first statement
3. **The link**: stage N+1 names or consumes what stage N produced — the chain is visible, not hidden
4. **The evolution**: the value transforms as it passes: raw data → parsed → filtered → summarized → judged
5. **Each stage runs**: the whole chain is one program; if one link breaks, the poem dies

## The Chain: what counts

Each stage must visibly consume the previous stage's result — by variable, by pipe, or by function composition. The chain is the structure; readers should be able to trace the baton from stage 1 to the final line. Good code-renshi links:

- **The parse chain**: raw text → tokens → counts → top word
- **The pipeline**: input → validate → transform → aggregate → report
- **The relay**: each stage's last expression named as the next stage's input

## Core Patterns

### The Parse Renshi
The chain that reads:

```python
import re, sys
text = sys.stdin.read()                 # stage 1: the raw text
tokens = re.findall(r"[a-z']+", text.lower())  # stage 2: the tokens
counts = {t: tokens.count(t) for t in set(tokens)}  # stage 3: the counts
top = max(counts, key=counts.get)       # stage 4: the leader
print(f"'{top}' x {counts[top]}")       # stage 5: the verse
```

### The Pipeline Renshi
The chain that transforms:

```python
import json
raw = open("events.json").read()        # stage 1: the raw
events = json.loads(raw)                # stage 2: the parse
failed = [e for e in events if not e.get("ok")]  # stage 3: the filter
ids = [e["id"] for e in failed]         # stage 4: the extract
print(f"failed: {ids}")                 # stage 5: the verse
```

### The Relay Renshi
The chain that accumulates:

```python
import statistics as st
nums = [3, 1, 4, 1, 5, 9, 2, 6]         # stage 1: the values
total = sum(nums)                       # stage 2: the sum
mean = total / len(nums)                # stage 3: the mean
deviations = [abs(n - mean) for n in nums]  # stage 4: the spread
print(f"mean {mean:.1f}, dev {st.pstdev(nums):.1f}")  # stage 5: the verse
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- 3-6 visible stages, each 2-3 lines of logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the renshi actually runs and produces the correct result for the task
- each stage visibly consumes the previous stage's output — the chain is traceable
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
- makes the links visible — each stage names what it received
- lets the value evolve through the chain, raw to refined
- ends on a final verse that the whole chain earned
- imports only what the lines need

## Examples of Renshi Beauty

- **The parse chain**: text → tokens → counts → leader
- **The pipeline**: raw → parse → filter → extract → report
- **The relay**: values → sum → mean → spread → verse
- **The evolution**: each stage transforms the baton

## The Renshi Promise

Remember: "A renshi is a relay in code: each stage takes the baton the last one passed, transforms it, and hands it on — and the whole chain runs."

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
    let spread: f64 = nums.iter().map(|n| (*n as f64 - mean).powi(2)).sum::<f64>() / nums.len() as f64;  // stage 4
    println!("mean {mean:.1} var {spread:.1}");  // stage 5
}
```

For other languages, translate the same structure, a visible chain of short stages.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
