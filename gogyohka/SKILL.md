---
name: gogyohka
description: >-
  Write code as a gogyohka: a 5-line program with no syllable or token counting - five
  lines, each one natural phrase, one breath per line, free verse for code. Use this skill
  when the user wants a 5-line program that is free and natural rather than metered, or
  dense code that breathes. Make sure to use this skill whenever the user mentions
  gogyohka, five-line poems, free-form five-liners, or one-breath-per-line code. This
  skill is NOT for the strict 5-7-5-7-7 tanka and NOT for 3-line forms (use haiku, senryu,
  lunes, or katauta).
---

# Gogyohka Skill

A gogyohka is the liberated tanka, five lines, and nothing else required. No syllable count, no seasonal word, no strict meter: five lines, each one a natural phrase, one breath per line. A code gogyohka is five lines of free verse, each line a complete short statement, with room to breathe instead of a meter to obey.

## Philosophy

"Five lines, five breaths, no rules but the shape."

The gogyohka mindset:
1. **Five lines**: exactly the shape, never the meter
2. **One breath per line**: each line is a natural phrase, a complete small statement
3. **Free verse**: no token counting, no 5-7-5, liberation from meter
4. **Modern rhythm**: the code sounds like how people actually talk
5. **Actually works**: a gogyohka that doesn't run is a breath that was never taken

## The Structure: what free-form means in code

Every other form in the family counts tokens per line. Gogyohka does not. The only rules:

- **Five lines of code** that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- **Each line is one natural phrase**, a short, complete statement that could be spoken in a single breath
- No line-length budget, no rhythm, no seasonal vocabulary, just five clean lines

This is the most forgiving form in the family, and the hardest to fake: free verse still needs each line to be worth its breath.

## Core Patterns

### Sum Gogyohka
Five natural lines, no counting.

```python
import sys
data = sys.stdin.read().split()
numbers = [int(x) for x in data]
total = sum(numbers)
print(total)
```

### File Gogyohka
A small report in five breathing lines.

```python
import sys
lines = sys.stdin.read().splitlines()
words = sum(len(l.split()) for l in lines)
print(f"{len(lines)} lines, {words} words")
```

## Boundaries, when NOT to use this skill (use a different skill instead)

This skill is **not for** every poetic-code request. When the user asks for one of the following, **instead use** the listed skill, the goal is that two skills never coin-flip on the same prompt:

- the strict 5-7-5-7-7 metered tanka -> tanka
- 3-line forms -> haiku, senryu, lunes, or katauta
- prose-with-haiku -> haibun
- two-stanza mirror forms -> sedoka
- shortest-possible / golfed code -> esoteric-programming

Gogyohka is the free five-line form. If the user wants a meter, use tanka; if they want three lines, use a 3-line form; if they want five free breaths, this is it.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- exactly 5 lines of code (or fewer) that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the gogyohka actually runs and produces the correct result for the task
- each line is a natural, complete short statement, one breath per line
- no metered padding: lines are as long as the phrase needs, never stretched to fit a count
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report five visible logic-line counts without applying a meter, while checking one-breath-per-line and semicolon/branching constraints separately; this diagnostic must not turn free verse into tanka.

These requirements exist because a theme without a spec produces vibes, not output. A gogyohka that counts tokens is a tanka in disguise; a gogyohka that doesn't run is five dead breaths.

## When to Use Gogyohka Patterns

Use gogyohka code when:
- the task fits naturally in five short steps
- the user wants a 5-line program without meter constraints
- dense code that breathes is more important than a rhythm
- the user says "free form", "five lines", "one breath per line", or "just make it five lines"

## The Gogyohka Aesthetic

Write code that:
- is five lines or fewer, never padded
- makes each line a natural phrase you could say out loud
- keeps no token budget, lines are as long as the thought takes
- reads with modern, natural rhythm
- ends on the last breath, not a formula

## Examples of Gogyohka Beauty

- **Sums**: read, split, convert, add, print, five breaths
- **Reports**: lines, words, and the one number that matters
- **Filters**: the list, the rule, the survivors, the count
- **Small Servers**: import, class, one handler, serve
- **Free Verse Tools**: anything that fits five natural lines

## The Gogyohka Promise

Remember: "Five lines, five breaths, no rules but the shape. The meter is gone, what remains is the honest phrase, and it runs."

## Cross-Language Examples

Free verse translates everywhere:

```javascript
import { readFileSync } from "fs";       // breath one
const data = readFileSync(0, "utf8").split("\n");  // breath two
const words = data.join(" ").split(/\s+/).length;  // breath three
console.log(`${data.length} lines`);     // breath four
console.log(`${words} words`);           // breath five
```

```rust
use std::io::{self, BufRead};            // breath one
fn main() {
    let lines: Vec<String> = io::stdin().lock().lines().map(|l| l.unwrap()).collect();
    let words: usize = lines.iter().map(|l| l.split_whitespace().count()).sum();
    println!("{} lines, {} words", lines.len(), words);
}
```

For other languages, translate the same structure, five natural lines, one breath each.

## Bundled Helpers

If the five lines need randomness or a canvas, reuse the shared toolkit:

- `shared/rng.py`, seeded RNG and choice helpers
- `shared/ascii_canvas.py`, ASCII canvas for the free verse

A gogyohka may import one of these on its first breath, it counts toward the five.
