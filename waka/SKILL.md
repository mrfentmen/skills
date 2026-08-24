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
3. **The turn (line 4)**: the pivot: the observation that changes the reading
4. **The resolve (line 5)**: the quiet conclusion the turn earned
5. **The restraint**: nothing loud, nothing padded; the elegance is in the economy
6. **Actually works**: if it doesn't run, the court has no patience for it

## The Turn: what counts

Line 4 must pivot the poem: a change of angle, a hidden fact, a shift in scale: and line 5 resolves it. The turn in a waka is quiet, not dramatic: the anthologies prized the pivot that re-reads the scene. Good code-waka turns:

- **The scale shift**: the individual number, then the pattern behind it
- **The hidden fact**: the value the setup didn't reveal
- **The re-read**: the same data seen from the other side

## Core Patterns

### The Scale-Shift Waka
The individual, then the pattern:

```python
import sys
nums = [int(x) for x in sys.stdin.read().split()]
spread = max(nums) - min(nums)
count = len(nums)
print("range", spread, "count", count, "now")
print("five", "lines", "and", "the", "poem", "is", "done")
```

### The Hidden-Fact Waka
The setup, then the fact it hid:

```python
import json
users = json.load(open("users.json"))  # the users
total = len(users)  # the count
roles = [u["role"] for u in users]
admins = roles.count("admin")  # the admins
print(admins, "of", total, "users", "are", "admins")
```

### The Re-Read Waka
The data, seen twice:

```python
import re, sys
text = sys.stdin.read()  # the source
words = re.findall(r"\S+", text)  # the words
longest = max(words, key=len)  # the longest
rev = longest[:-1]  # the mirror
print(f"'{longest}' reversed is '{rev}' now")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
   **Output contract:** print exactly the numbers the example prints (here the range and the count) and nothing else — do not add a mean, average, or sum; the output check compares the exact number set on every input.
2. **Shape the rhythm.** Rewrite in the waka form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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
- turns quietly on line 4: a scale shift, a hidden fact, a re-read
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
// scene: the requests
const reqs = [12, 45, 30];
// scene: the sum
const sum = reqs.reduce((a, b) => a + b);
// scene: the average
const avg = sum / reqs.length;
// the turn: the peak
const peak = reqs.reduce((a, b) => Math.max(a, b));
// the resolve
console.log(`peak ${peak} and avg ${avg.toFixed(1)}`);
```

```rust
fn main() {
    // scene: the requests
    let reqs = [12, 45, 30];
    // scene: the sum
    let sum: i32 = reqs.iter().sum();
    // scene: the average
    let avg = f64::from(sum) / 3.0;
    // the turn: the peak
    let peak: i32 = *reqs.iter().max().unwrap();
    // the resolve
    println!("peak {peak} and avg {avg:.1}");
}
```

For other languages, translate the same structure, scene, turn, resolve.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
