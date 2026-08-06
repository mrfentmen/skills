---
name: lunes
description: >-
  Write code as a lune: a complete, working 3-line program with the American 5-3-5 token
  rhythm - a short setup, a razor-thin 3-token middle line that is the punch, and a short
  landing. Use this skill when the user wants a minimal 3-line program with an abrupt
  decisive middle, or a tiny one-shot where the middle line does exactly one sharp thing.
  Make sure to use this skill whenever the user mentions lune, lunes, 5-3-5, or wants a
  very short dense program with a punchy middle line. This skill is NOT for the Japanese
  5-7-5 (use haiku), NOT for the 5-line expanded form (use tanka), and NOT for human-humor
  forms (use senryu).
---

# Lunes Skill

The lune is the American haiku, invented, not inherited, with its own rhythm: 5-3-5. Where the haiku's middle line is the longest, the lune's middle line is the thinnest, three tokens, one sharp act. A code lune is three lines: setup, a razor-thin decisive middle, landing.

## Philosophy

"A lune is a haiku that punches. Short breath, one strike, done."

The lune mindset:
1. **Three lines**: 5-3-5 tokens, the middle is the smallest
2. **The punch**: the middle line does exactly one sharp thing in ~3 tokens
3. **Setup and landing**: the world before, the world after
4. **No wasted motion**: every token earns its place
5. **Actually works**: a lune that doesn't run is just a broken rhythm

## The Syllable Question: what 5-3-5 means in code

Tokens are the code analog of syllables. The lune's shape is the mirror of the haiku's:

- **Line 1, 5 tokens**: setup. The world, the data, the situation.
- **Line 2, 3 tokens**: the punch. One decisive operation, `total = sum(nums)`, `data.sort()`, `return mode(x)`.
- **Line 3, 5 tokens**: landing. The result, shown.

Approximate ±1, the middle line especially, because 3 tokens is the whole point. If the middle line is as long as the others, it's not a lune, it's a haiku with a limp.

## Core Patterns

### Summation Lune
Setup, one 3-token strike, landing.

```python
nums = [3, 1, 4, 1, 5]
total = sum(nums)
print(total)
```

### Mode Lune
The punchline middle: one expression that finds the answer.

```python
xs = [1, 2, 2, 3, 2, 4]
mode = max(set(xs), key=xs.count)  # the strike
print(mode)
```

### Line-Count Lune
A tiny tool with a 3-token strike in the middle.

```python
import sys
lines = sys.stdin.read().splitlines()
print(len(lines))
```

## Boundaries, when NOT to use this skill (use a different skill instead)

This skill is **not for** every poetic-code request. When the user asks for one of the following, **instead use** the listed skill, the goal is that two skills never coin-flip on the same prompt:

- the Japanese 5-7-5 (long middle line) -> haiku
- the 5-line expanded form -> tanka
- human-nature humor forms -> senryu
- shortest-possible / golfed code -> esoteric-programming

Lune is the American 5-3-5 form. If the middle line isn't dramatically shorter than the others, it's not a lune.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 3 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the lune actually runs and produces the correct result for the task
- the middle line is the shortest line, roughly 3 tokens, one decisive operation
- every token earns its place; no filler to reach any count
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

These requirements exist because a theme without a spec produces vibes, not output. The short middle line is what separates a lune from a haiku, grade it like you mean it.

## When to Use Lune Patterns

Use lune code when:
- the task reduces to one sharp operation on a small input
- the user wants the tightest possible 3-line one-shot
- a single decisive middle line can carry the whole task
- the user says "punchy", "minimal middle", or "just the one move"

## The Lune Aesthetic

Write code that:
- is three lines or fewer
- keeps the 5-3-5 rhythm, middle line shortest
- makes the middle line exactly one decisive operation
- imports only what the punch needs
- ends with the result, no commentary

## Examples of Lune Beauty

- **Sums**: setup, `sum(nums)`, print
- **Modes**: setup, one expression, print
- **Counts**: read, count, show
- **Sorts**: setup, one call, show
- **One-liners**: the whole task as one breath and one strike

## The Lune Promise

Remember: "The lune says it in five, then three, then five, the middle is the strike, the rest is the breath around it. Three lines, one punch, it runs."

## Cross-Language Examples

The 5-3-5 rhythm translates everywhere, keep the middle short:

```javascript
const add = (a, b) => a + b;            // setup
const total = [3, 1, 4, 1, 5].reduce(add);  // punch (short)
console.log(total);                     // landing
```

```rust
fn main() {                              // ceremony, free
    let sum: i32 = [3, 1, 4].iter().sum();  // the punch
    println!("{sum}");                   // landing
}
```

For other languages, translate the same structure, setup, one sharp middle, landing.

## Bundled Helpers

If the task needs randomness or ASCII output, reuse the shared toolkit:

- `shared/rng.py`, seeded RNG and choice helpers
- `shared/ascii_canvas.py`, ASCII canvas for one-stroke output

A lune may import one of these on its setup line, that still counts as one of the three.
