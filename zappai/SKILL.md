---
name: zappai
description: >-
  Write runnable code in a zappai form: a haiku-shaped poem freed from haiku's rules — no seasonal kigo required, no cutting word required, just three lines of roughly 5-7-5 tokens that land a single vivid moment. Activate only for an explicit zappai, free haiku, or unconstrained three-line moment request.
---

# Zappai Skill

A zappai is a haiku-shaped poem that refuses haiku's discipline: same three lines, same rough 5-7-5 rhythm, but no kigo (season word) required, no kireji (cutting word) required. It is the haiku of the moment, unlicensed. A code zappai is a three-line program that does the task in three lines and lands the moment — the snapshot, the observation, the small truth — without ceremony.

## Philosophy

"A zappai is a haiku off duty. Three lines, a moment, no season required."

The zappai mindset:
1. **Three lines**: exactly three logic lines, roughly 5-7-5 tokens, or fewer, never pad
2. **No kigo required**: the subject can be anything — code, config, weather, traffic, a stack trace
3. **No kireji required**: the cutting pause is optional; the moment just needs to land
4. **The moment**: the third line should deliver the observation the first two earned
5. **Actually works**: if it doesn't run, it's a moment that never happened

## The Moment: what counts

The zappai's third line must land like a snapshot — a single observation that completes the picture. It does not need to be profound; it needs to be true and complete. Good code-zappai moments:

- **The observation**: the number that summarizes the mess (the 3 errors in 200 lines)
- **The snapshot**: the state of the system at a single instant (the cache with 2 entries)
- **The small truth**: the humble finding (the config key that was misspelled)

The three lines should read as one breath: do the work, show the work, land the moment.

## Core Patterns

### The Snapshot Zappai
The state, the moment:

```python
import json
data = json.load(open("health.json"))       # the load
down = [k for k, v in data.items() if not v]  # the check
print(f"down: {', '.join(down) or 'none'}")  # the moment
```

### The Observation Zappai
The count, the truth:

```python
import re
log = open("app.log").read()                # the source
errs = len(re.findall(r"ERROR", log))       # the count
print(f"{errs} errors, {len(log.splitlines())} lines")  # the moment
```

### The Small Truth Zappai
The find, the truth:

```python
import json
cfg = json.load(open("config.json"))        # the load
keys = set(cfg)
print(f"keys: {sorted(keys)}")              # the moment: what's really there
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 3 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the zappai actually runs and produces the correct result for the task
- three lines roughly 5-7-5 tokens (±2 tolerance per line)
- the third line lands a moment: an observation, snapshot, or small truth that the first two lines earned
- no kigo or kireji requirements — the moment stands alone
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the three visible logic-line token counts against `[5, 7, 5]` with ±2 tolerance, and confirm the third line lands the moment; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A zappai that doesn't land its moment is just three lines of code.

## Boundaries

This skill is not for any three-line program, generic compact code, or code that lacks the haiku-shaped moment. Without an explicit zappai request or that structural contract, handle the request normally. When the request explicitly asks for haiku discipline (kigo, kireji, season), the haiku skill applies instead.

## Activation

Activate this skill only when the user explicitly names zappai, requests a free haiku or unconstrained three-line moment, or requests haiku shape without haiku rules. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Zappai Aesthetic

Write code that:
- is three lines, no padding
- does the work in the first two lines, lands the moment in the third
- needs no season, no cutting word, no ceremony
- lets the moment be small and true — a snapshot, an observation, a count
- imports only what the lines need

## Examples of Zappai Beauty

- **The snapshot**: the system at one instant
- **The count**: the errors in the log
- **The small truth**: the misspelled key
- **The moment**: the observation that completes the picture

## The Zappai Promise

Remember: "A zappai is a haiku off duty: three lines, a moment, no season required, and the code runs."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const data = JSON.parse(process.stdin.read());  // the load
const down = Object.entries(data).filter(([, v]) => !v).map(([k]) => k);  // the check
console.log(`down: ${down.join(', ') || 'none'}`);  // the moment
```

```rust
fn main() {                                 // ceremony, free
    let vals = [3, 1, 4, 1, 5];             // the values
    let total: i32 = vals.iter().sum();     // the sum
    println!("total: {total}");             // the moment
}
```

For other languages, translate the same structure, three lines, the moment in the third.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
