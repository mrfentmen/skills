---
name: haibun
description: >-
  Write code as a haibun: a flowing, narrative program (the prose - step-by-step code with
  story-like comments) that ends in a 3-line dense haiku (the moment). Use this skill when
  the user wants a program that tells a story about its data, a narrated walkthrough that
  finishes with a poetic summary, or a report that reads like a travel diary. Make sure to
  use this skill whenever the user mentions haibun, prose-and-haiku, narrated code, or a
  story-shaped program with a poetic ending. This skill is NOT for pure 3-line forms (use
  haiku, senryu, lunes, or katauta) and NOT for strict-meter forms (use tanka or sedoka).
---

# Haibun Skill

A haibun is a journey: prose that walks, and a haiku that arrives. Bashō's travel diaries, a paragraph of the road, then the moment it was all for. A code haibun is the same: a narrative program that walks through its data with story-like comments and clear steps, then ends in three dense lines that say what the whole walk meant.

## Philosophy

"The prose is the road; the haiku is the view from the top."

The haibun mindset:
1. **Prose first**: flowing, step-by-step code with comments that read like a diary
2. **The walk matters**: the journey through the data is the poem's body
3. **The haiku lands last**: the final 3 dense lines are the moment everything meant
4. **One trip, one insight**: the program tells one story, then ends it
5. **Actually works**: a haibun that doesn't run is a diary that was never written

## The Structure: what prose-and-haiku means in code

Tokens are the code analog of syllables. In a haibun there are two voices:

- **The prose (lines 1-N)**: the narrative body. Multi-step processing with
  comments that describe the scene like a diary ("the log opens like a diary
  of the long night"). Any number of lines, no rhythm rule, prose has no
  meter.
- **The haiku (the final 3 lines)**: the dense moment. Three lines in the
  5-7-5 token spirit that distill the whole walk into a single result.

The haiku is the destination, a 3-line landing that the prose has been
walking toward. Keep the whole program at most ~12 lines: a haibun is short
prose, not an essay.

## Core Patterns

### Log-Walk Haibun
The prose reads through the logs; the haiku counts what the night left behind.

```python
# the stream arrives like a morning walk
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every keyword a sighting
errors = [l for l in lines if "ERROR" in l]
# the count: what the day actually held
n_errors = len(errors)
n_total = len(lines)
print(f"{n_errors} errors of {n_total} lines")
```

### Weather Haibun
The prose sorts the seasons; the haiku balances cold against warm.

```python
# a walk through the dataset, as one walks a garden
import csv, sys
rows = list(csv.DictReader(sys.stdin))
# every row a season, every column a small weather
cold = [r for r in rows if int(r["temp"]) < 0]
warm = [r for r in rows if int(r["temp"]) > 20]
# the walk ends where the seasons balance
winter = len(cold)
summer = len(warm)
print(f"{winter} cold days, {summer} warm")
```

## Boundaries, when NOT to use this skill (use a different skill instead)

This skill is **not for** every poetic-code request. When the user asks for one of the following, **instead use** the listed skill, the goal is that two skills never coin-flip on the same prompt:

- pure 3-line forms with no prose body -> haiku, senryu, lunes, or katauta
- strict-meter forms -> tanka or sedoka
- free-form 5-liners -> gogyohka
- shortest-possible / golfed code -> esoteric-programming

Haibun is the story-shaped form: prose that walks, then a haiku that lands. Without the narrative body, it's just a haiku; without the final haiku, it's just a script.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 12 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the haibun actually runs and produces the correct result for the task
- a narrative prose body: multi-step processing with story-like comments; mechanically this means at least 2 diary-style comments of 3+ words each (e.g. `# the log opens like a diary of the long night`), not one-word labels like `# count`
- a final 3-line dense haiku that distills the whole walk into one result; mechanically the final 3 lines must include a poetic line, a print whose string has 3+ words and no numbers (e.g. `print('the errors call out')`), not a bare label line like `print('errors:', errors)`
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: measure the narrative body separately, then report the final three visible logic lines against `[5, 7, 5]` with ±2 tolerance; the report is diagnostic and must not mistake prose ceremony for meter.

These requirements exist because a theme without a spec produces vibes, not output. A haibun without the story is a script; a haibun without the ending haiku is a diary with no last page. The prose comments and the poetic landing are what make the narrative mechanically checkable, a plain script that merely fits the line budget is not a haibun.

## When to Use Haibun Patterns

Use haibun code when:
- the task is a journey, a file to read, a walk to take, a story to tell
- the user wants narrated, readable processing with a poetic payoff
- a report should read like a travel diary and end in a single insight
- the user says "narrate it", "walk me through it", or "with a poetic ending"

## The Haibun Aesthetic

Write code that:
- flows: step-by-step, with comments that tell the story
- walks one journey per program, one file, one question, one insight
- ends in a 3-line haiku that says what the walk meant
- uses prose comments like diary entries, not technical notes
- keeps the whole trip short, a haibun is not an essay

## Examples of Haibun Beauty

- **Log Walks**: through error lines, ending in a count that feels like dawn
- **Weather Walks**: through rows of seasons, ending in cold vs warm
- **Trip Reports**: through a dataset, ending in the one number that mattered
- **Garden Tours**: through nested structures, ending in the flower found
- **Night Diaries**: through midnight writes, ending in what the morning saw

## The Haibun Promise

Remember: "The prose is the road and the haiku is the view from the top. Walk through the data, tell its story, and end with the three lines it was all for."

## Cross-Language Examples

The two voices translate everywhere:

```javascript
// the stream arrives like a morning walk
import { readFileSync } from "fs";
const lines = readFileSync(0, "utf8").split("\n");
// every line a step, every keyword a sighting
const errors = lines.filter(l => l.includes("ERROR"));
// the count: what the day actually held
const nErrors = errors.length;
const nTotal = lines.length;
console.log(`${nErrors} errors of ${nTotal} lines`);
```

```rust
use std::io::{self, BufRead};          // prose: the road
fn main() {
    let lines: Vec<String> = io::stdin().lock().lines().map(|l| l.unwrap()).collect();
    let errors = lines.iter().filter(|l| l.contains("ERROR")).count();
    let total = lines.len();           // haiku: the view
    println!("{errors} errors of {total} lines");
}
```

For other languages, translate the same structure, narrative prose body, then the 3-line haiku landing.

## Bundled Helpers

If the walk needs randomness or ASCII scenery, reuse the shared toolkit:

- `shared/rng.py`, seeded RNG and choice helpers
- `shared/ascii_canvas.py`, ASCII canvas for rendering the walk

A haibun may import one of these in its prose body, it counts toward the 12 lines.
