---
name: haibun
description: >-
  Write a runnable haibun: a short narrative program with diary-like processing and a distinct three-line poetic landing that summarizes the journey. Activate only for an explicit haibun, prose-and-verse program, or narrated code journey request.
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
# the log opens like a diary of the long night
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every keyword a sighting
errors = [line for line in lines if "ERROR" in line]
print("errors", len(errors))
print("found")
print("in the night")
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

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the haibun form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

- at most 12 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the haibun actually runs and produces the correct result for the task
- a narrative prose body: multi-step processing with story-like comments; mechanically this means at least 2 diary-style comments of 3+ words each (e.g. `# the log opens like a diary of the long night`), not one-word labels like `# count`
- a final 3-line dense haiku that distills the whole walk into one result; mechanically the final 3 lines must include a poetic line, a print whose string has 3+ words and no numbers (e.g. `print('the errors call out')`), not a bare label line like `print('errors:', errors)`
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: measure the narrative body separately, then report the final three visible logic lines against `[5, 7, 5]` with ±2 tolerance; the report is diagnostic and must not mistake prose ceremony for meter.

These requirements exist because a theme without a spec produces vibes, not output. A haibun without the story is a script; a haibun without the ending haiku is a diary with no last page. The prose comments and the poetic landing are what make the narrative mechanically checkable, a plain script that merely fits the line budget is not a haibun.

## Boundaries

This skill is not for ordinary prose documentation, a plain script, or a poem without narrative processing and its three-line landing. Without the complete haibun contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names haibun or requests a narrative prose-and-verse program with a three-line landing. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

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
// the stream arrives like a morning walk
use std::io::{self, BufRead};
fn main() {
    let lines: Vec<String> = io::stdin().lock().lines().map(|l| l.unwrap()).collect();
    // every line a step, every keyword a sighting
    let errors = lines.iter().filter(|l| l.contains("ERROR")).count();
    let total = lines.len();
    let clean = total - errors;
    // the count: what the day actually held
    println!("{errors} errors, {clean} clean of {total} lines");
}
```

For other languages, translate the same structure, narrative prose body, then the 3-line haiku landing.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
