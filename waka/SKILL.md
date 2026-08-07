---
name: waka
description: >-
  Write runnable code in a waka form: the classical five-line 5-7-5-7-7 verse of the imperial anthologies, where the upper three lines establish the scene and the lower two lines turn and resolve it with courtly grace. Activate only for an explicit waka, 5-7-5-7-7 classical verse, or imperial anthology request.
---

# Waka Skill

A waka is the classical Japanese verse of the imperial anthologies: five lines, 5-7-5-7-7, refined and formal. Where tanka is the modern sibling, waka carries the court's manners: the upper three lines establish the scene with decorum, the lower two lines turn it with the quiet surprise that the anthologies prized. A code waka is a five-line program: scene, then turn, delivered with restraint.

## Philosophy

"A waka is a tanka with courtly manners. The first three lines set the scene; the last two turn it, gently, inescapably."

The waka mindset:
1. **Five lines**: 5-7-5-7-7 tokens, or fewer, never pad
2. **The scene (lines 1-3)**: the state of things, established with clarity and restraint
3. **The turn (line 4)**: the pivot — the observation that changes the reading
4. **The resolve (line 5)**: the quiet conclusion the turn earned
5. **The restraint**: nothing loud, nothing padded; the elegance is in the economy
6. **Actually works**: if it doesn't run, the court has no patience for it

## The Turn: what counts

Line 4 must pivot the poem — a change of angle, a hidden fact, a shift in scale — and line 5 resolves it. The turn in a waka is quiet, not dramatic: the anthologies prized the pivot that re-reads the scene. Good code-waka turns:

- **The scale shift**: the individual number, then the pattern behind it
- **The hidden fact**: the value the setup didn't reveal
- **The re-read**: the same data seen from the other side

## Core Patterns

### The Scale-Shift Waka
The individual, then the pattern:

```python
import sys
data = [int(x) for x in sys.stdin.read().split()]
mean = sum(data) / len(data)
peak = max(data)
print("peak", peak, "mean", mean, "now")
print("five", "lines", "and", "the", "poem", "is", "done")
```

### The Hidden-Fact Waka
The setup, then the fact it hid:

```python
import json
users = json.load(open("users.json"))        # scene: the users
total = len(users)                           # scene: the count
admins = sum(1 for u in users if u["role"] == "admin")  # scene: the roles
share = admins / max(1, total)               # the turn: the share
print(f"{admins} admins, {share:.0%} of users")  # the resolve: the surprise
```

### The Re-Read Waka
The data, seen twice:

```python
import re, sys
text = sys.stdin.read()                      # scene: the source
words = re.findall(r"\S+", text)             # scene: the words
longest = max(words, key=len)                # scene: the longest
rev = longest[::-1]                          # the turn: the mirror
print(f"'{longest}' reversed: '{rev}'")      # the resolve: the echo
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the waka form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 5 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the waka actually runs and produces the correct result for the task
- lines 1-3 establish the scene; line 4 turns it; line 5 resolves it
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the five visible logic-line token counts against `[5, 7, 5, 7, 7]` with ±2 tolerance, and confirm line 4 turns and line 5 resolves; diagnostics must never reward padding.

These requirements exist because a theme without a spec produces vibes, not output. A waka without its turn is a tanka that forgot its manners.

## Boundaries

This skill is not for any five-line program, generic compact code, or code that lacks the scene-turn-resolve 5-7-5-7-7 shape. Without an explicit waka request or that structural contract, handle the request normally. When the request explicitly asks for a modern tanka with a reflection-expansion (not a turn), the tanka skill applies instead.

## Activation

Activate this skill only when the user explicitly names waka, requests classical 5-7-5-7-7 verse, or requests an imperial-anthology structure. Generic coding requests, generic brevity, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Waka Aesthetic

Write code that:
- is five lines, no padding
- establishes the scene in the first three lines, with restraint
- turns quietly on line 4 — a scale shift, a hidden fact, a re-read
- resolves on line 5 with the verdict the turn earned
- uses a kigo-like seasonal name on the turn line
- imports only what the lines need

## Examples of Waka Beauty

- **The scale shift**: the peak, then the pattern behind it
- **The hidden fact**: the count, then the share it hid
- **The re-read**: the word, then its mirror
- **The courtly turn**: the scene, then the quiet surprise

## The Waka Promise

Remember: "A waka is a tanka with courtly manners: five lines, the scene in three, the quiet turn in the fourth, the resolve in the fifth."

## Cross-Language Examples

The token rhythm is language-agnostic. Same spirit, translated:

```javascript
const reqs = [12, 45, 30, 9, 400, 22];         // scene: the requests
const avg = reqs.reduce((a, b) => a + b, 0) / reqs.length;  // scene: the average
const peak = Math.max(...reqs);                // scene: the loudest
const rate = peak / avg;                       // the turn: the ratio
console.log(`peak ${peak}, ${rate.toFixed(1)}x average`);  // the resolve
```

```rust
fn main() {                                    // ceremony, free
    let reqs = [12, 45, 30, 9, 400, 22];       // scene: the requests
    let total: i32 = reqs.iter().sum();        // scene: the sum
    let avg = total as f64 / reqs.len() as f64; // scene: the average
    let peak = *reqs.iter().max().unwrap();    // the turn: the peak
    println!("peak {peak}, {:.1}x average", peak as f64 / avg);  // the resolve
}
```

For other languages, translate the same structure, scene, turn, resolve.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
