---
name: gogyohka
description: >-
  Write runnable code in a gogyohka form: exactly five natural logic lines with free rhythm, one complete breath per line, and no meter requirement. Activate only for an explicit gogyohka, free-form five-line, or five-breath code request.
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

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

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

## Boundaries

This skill is not for any arbitrary five-line snippet or generic brevity. Without an explicit gogyohka request or the free-rhythm five-line contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names gogyohka or requests free-form five-line code. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

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

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
