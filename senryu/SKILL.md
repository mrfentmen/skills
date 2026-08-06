---
name: senryu
description: >-
  Write runnable code in a senryu form: at most three logic lines with a 5-7-5 rhythm, a human subject, and a working humorous landing. Activate only for an explicit senryu, human-nature code joke, or 5-7-5 human-comedy request.
---

# Senryu Skill

A senryu looks like a haiku but points the other way, haiku watches nature, senryu watches people. Three lines, 5-7-5, and the moment is human: a quirk, a habit, a joke the reader recognizes. A code senryu is three lines that do something about people, and land the punchline in the code itself.

## Philosophy

"A haiku is about the moon. A senryu is about the person staring at the moon."

The senryu mindset:
1. **Three lines**: 5-7-5 tokens, human-focused
2. **The subject is people**: users, habits, bugs, excuses, second-guessing
3. **The kigo is a punchline**: the name or output that makes you smirk
4. **Humor that runs**: the joke is in what the code does, not in breaking it
5. **Actually works**: a senryu that fails is just a sad error message

## The Syllable Question: what 5-7-5 means in code

Same token math as haiku, tokens are the code analog of syllables:

- **Line 1, 5 tokens**: setup. The human situation.
- **Line 2, 7 tokens**: the turn. The behavior, the habit, the honest truth.
- **Line 3, 5 tokens**: landing. The punchline, a name, an output, a number that says it all.

Approximate ±2. The budget is conserved when you use fewer lines: two lines collapse to ~12 tokens (5+7) then ~5, one line to ~17; the punchline landing stays the short ~5. Fewer lines is legal, rhythm is not optional — `scripts/rhythm_check.py` enforces the silhouette at any line count.

The difference from haiku is subject, not shape: nature and seasons are out; people, humor, and recognizably human failure are in.

## Core Patterns

### Excuse Generator
Three lines, a human truth everyone has lived.

```python
import random
blame = random.choice(["the dog", "the wifi", "mercury retrograde"])
print(blame, "ate my commit")
```

### Honest Estimator
The oldest joke in software, estimates, and what they become.

```python
def time_to(hours, done):
    return hours if done else hours * 2
print(time_to(1, False))
```

### Procrastination Detector
Code that knows the user better than they do.

```python
def due(hours, started): return "now" if not started else f"{hours} more"
verdict = due(8, False)
print(verdict, "you knew this was coming")
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 3 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the senryu actually runs and produces the correct result for the task
- the subject is human: a person, a habit, a user, a bug with a personality
- the output or a name carries the punchline, the humor is in the code, not a comment
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work
- rhythm self-check: after writing, count the tokens on each logic line (imports and comments are free) and tighten any line that is outside ±2 of the silhouette (`[5, 7, 5]` on three lines, `[12, 5]` on two, `[17]` on one) by shortening names or simplifying expressions; never split a line into more, never pad
- bundled checker: `scripts/rhythm_check.py solve.py` prints the token profile and fails any line outside ±2; run it when you can, or count by hand, and report the counts with the solution

Benchmark signature: report the visible logic-line token counts against the conserved 5-7-5 silhouette — `[5, 7, 5]` on three lines, `[12, 5]` on two, `[17]` on one — with ±2 tolerance, separately from the human-subject and punchline assertions; never pad for the meter.

These requirements exist because a theme without a spec produces vibes, not output. A senryu without the human subject is just a haiku; a senryu that doesn't run is just a dead joke.

## Boundaries

This skill is not for generic humor, nature imagery, or any compact three-line program without human-nature comedy. Without an explicit senryu request or its 5-7-5 human-comedy contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names senryu or requests a human-comedy program with a 5-7-5 structure. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Senryu Aesthetic

Write code that:
- is three lines or fewer, no padding
- keeps the 5-7-5 token rhythm
- puts a person (or a very human bug) in the middle of the moment
- lands a punchline in a name or the output
- stays respectful, humor about shared human failure, not cruelty

## Examples of Senryu Beauty

- **Excuse Generators**: the dog, the wifi, and the stars, all guilty
- **Honest Estimators**: the estimate, the reality, the doubling
- **Procrastination Detectors**: code that knows what you'll actually do
- **User-Simulators**: bots that behave like people, warts and all
- **Bug Personas**: errors with attitude and names

## The Senryu Promise

Remember: "The moon is haiku's business; people are senryu's. Three lines, human truth, and a punchline that runs."

## Cross-Language Examples

The rhythm and the human subject translate everywhere:

```javascript
const blame = ["the dog", "the wifi", "mercury retrograde"];
const excuse = blame[Math.floor(Math.random() * blame.length)];
console.log(`${excuse} ate my commit`);
```

```rust
fn main() {                              // ceremony, free
    let estimate = |h: u32, done: bool| if done { h } else { h * 2 };
    println!("{}", estimate(1, false));
}
```

For other languages, translate the same structure, setup, human turn, punchline.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
