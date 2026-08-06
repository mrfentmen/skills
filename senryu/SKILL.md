---
name: senryu
description: >-
  Write code as a senryu: a complete, working 3-line program with the haiku's 5-7-5 token
  rhythm but about human nature - humor, quirks, and the comedy of people, not nature and
  seasons. Use this skill when the user wants a witty 3-line program, a code joke that
  actually runs, or dense code about users, habits, bugs, and human behavior. Make sure to
  use this skill whenever the user mentions senryu, funny code, human-nature code, or
  wants a 3-line program with a punchline. This skill is NOT for nature/season poems (use
  haiku), NOT for 5-line forms (use tanka), and NOT for the American 5-3-5 form (use
  lunes). If the user wants the 5-7-7 half-poem, use katauta.
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

Approximate ±2. The difference from haiku is subject, not shape: nature and seasons are out; people, humor, and recognizably human failure are in.

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

## Boundaries, when NOT to use this skill (use a different skill instead)

This skill is **not for** every poetic-code request. When the user asks for one of the following, **instead use** the listed skill, the goal is that two skills never coin-flip on the same prompt:

- nature, seasons, or abstract systems -> haiku
- 5-line expanded forms -> tanka
- the American 5-3-5 punch form -> lunes
- the 5-7-7 half-poem, addressed to its subject -> katauta
- shortest-possible / golfed code -> esoteric-programming

Senryu is the three-line human form. If the subject isn't people and the output isn't a little funny, it's not a senryu.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 3 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the senryu actually runs and produces the correct result for the task
- the subject is human: a person, a habit, a user, a bug with a personality
- the output or a name carries the punchline, the humor is in the code, not a comment
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the three visible logic-line token counts against `[5, 7, 5]` with ±2 tolerance, separately from the human-subject and punchline assertions; never pad for the meter.

These requirements exist because a theme without a spec produces vibes, not output. A senryu without the human subject is just a haiku; a senryu that doesn't run is just a dead joke.

## When to Use Senryu Patterns

Use senryu code when:
- the task is about people, users, habits, excuses, estimation, procrastination
- the user wants a witty or funny dense one-shot
- a small human truth can be the output
- the user says "make it funny" or "the human version"

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

If the task needs randomness for its punchline, reuse the shared toolkit:

- `shared/rng.py`, seeded RNG and choice helpers (perfect for excuse generators)

A senryu may import it on its setup line, that still counts as one of the three.
