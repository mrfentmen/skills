---
name: imayo
description: >-
  Write runnable code in an imayo form: four long logic lines, each shaped 7-5-7-5, a rolling rhythmic song that alternates a long breath and a short breath four times. Activate only for an explicit imayo, 7-5-7-5, Heian song, or four-line rolling rhythm request.
---

# Imayo Skill

An imayo is a Heian-era popular song: four lines, each 7-5 syllables, the long-short rhythm rolling like a drumbeat. A code imayo is a four-line program where every line alternates a long 7-token phrase and a short 5-token phrase — the song's pulse is in the line itself.

## Philosophy

"An imayo breathes twice per line: seven in, five out, four times over."

The imayo mindset:
1. **Four lines**: exactly four logic lines, each shaped 7-5 tokens (long phrase, short phrase), or fewer, never pad
2. **The internal rhythm**: each line carries its own 7-5 pulse; the reader should feel the beat inside the line
3. **The roll**: the four lines build like a song, verse after verse, each a complete step of the computation
4. **The refrain**: the last short 5-token phrase lands like the chorus hook
5. **Actually works**: if it doesn't run, the song has no voice

## The 7-5 Pulse: what counts

Each line must contain a long 7-token phrase followed by a short 5-token phrase (the split can be marked by an assignment, a comma, a chained call, or a semicolon — the beat is felt, not printed). Good imayo lines:

- **The wave**: `values = parse(input_text)` — long setup, short landing
- **The roll**: `count = len(unique_items)` — long work, short answer
- **The hook**: `print(f"total: {total}")` — long report, short refrain

The four lines should feel like four verses of one song: setup, work, deepen, resolve.

## Core Patterns

### The Rolling Imayo
Four waves of one computation:

```python
import json, sys                     # (ceremony is free)
data = json.load(sys.stdin)          # wave 1: the load (7-5 pulse)
prices = [d["price"] for d in data]  # wave 2: the extract
total = sum(prices)                  # wave 3: the sum
print(f"total: {total}")             # wave 4: the refrain
```

### The Verse Imayo
Each line a stanza of the pipeline:

```python
import re
text = open("log.txt").read()        # verse 1: the source
lines = text.splitlines()            # verse 2: the split
errors = [l for l in lines if "ERR" in l]  # verse 3: the filter
print(f"errors: {len(errors)}")      # verse 4: the chorus
```

### The Rolling Median Imayo
The song of the middle value:

```python
import statistics as st
nums = [3, 1, 4, 1, 5, 9, 2, 6]      # verse 1: the numbers
med = st.median(nums)                # verse 2: the middle
low = sum(1 for n in nums if n < med)  # verse 3: the under-side
print(f"median: {med}")              # verse 4: the refrain
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 4 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the imayo actually runs and produces the correct result for the task
- each line carries the 7-5 pulse: a long ~7-token phrase and a short ~5-token phrase, ±2 tolerance
- the four lines roll: setup, work, deepen, resolve — a complete song
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the four visible logic-line token counts as 7-5 pulses against `[7,5]` per line with ±2 tolerance, and confirm the final short phrase lands like a refrain; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. An imayo without its pulse is just a list of four statements.

## Boundaries

This skill is not for any four-line program, generic compact code, or code that lacks the rolling 7-5 internal pulse. Without an explicit imayo request or that structural contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names imayo, requests a 7-5-7-5 structure, Heian song, or four-line rolling rhythm. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Imayo Aesthetic

Write code that:
- is four lines, no padding
- gives each line its own 7-5 pulse — long breath, short breath
- rolls like a song: setup, work, deepen, resolve
- ends each line on the short phrase, like a chorus hook
- uses a kigo-like seasonal name in a line
- imports only what the lines need

## Examples of Imayo Beauty

- **The wave**: parse, extract, sum, report
- **The verse**: source, split, filter, chorus
- **The roll**: numbers, median, under-side, refrain
- **The song**: load, transform, reduce, sing

## The Imayo Promise

Remember: "An imayo breathes twice per line — seven in, five out, four times over, and the code sings."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const data = JSON.parse(process.stdin.read());  // wave 1: the load
const prices = data.map(d => d.price);          // wave 2: the extract
const total = prices.reduce((a, b) => a + b, 0); // wave 3: the sum
console.log(`total: ${total}`);                  // wave 4: the refrain
```

```rust
fn main() {                                     // ceremony, free
    let nums = [3, 1, 4, 1, 5, 9, 2, 6];        // wave 1: the values
    let total: i32 = nums.iter().sum();         // wave 2: the sum
    let mean = total as f64 / nums.len() as f64;  // wave 3: the mean
    println!("mean: {mean:.2}");                 // wave 4: the refrain
}
```

For other languages, translate the same structure, four waves, each with a long and short phrase.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
