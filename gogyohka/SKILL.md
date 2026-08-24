---
name: gogyohka
description: >-
  Write runnable code in a gogyohka form: exactly five natural logic lines with free rhythm, one complete step per line, and no meter requirement. Activate only for an explicit gogyohka, free-form five-line, or five-line code request.
---

# Gogyohka Skill

A gogyohka is the liberated tanka, five lines, and nothing else required. No syllable count, no seasonal word, no strict meter: five lines, each one a natural phrase, one meaningful step per line. A code gogyohka is five lines of free verse, each line a complete short statement, with room for the logic instead of a meter to obey.

## Philosophy

"Five lines, five meaningful steps, no rules but the shape."

The gogyohka mindset:
1. **Five lines**: exactly five logic-carrying lines, never four or fewer; never add a sixth line to hold explanation
2. **One meaningful step per line**: each line is a natural phrase, a complete small statement
3. **Free verse**: no token-count target, no 5-7-5, liberation from meter
4. **Modern rhythm**: the code sounds like how people actually talk
5. **Actually works**: a gogyohka that doesn't run is a step that was never completed

## The Structure: what free-form means in code

Other forms may impose numeric line measures; gogyohka does not. The only rules:

- **Exactly five logic-carrying lines of code**; language-mandated ceremony such as `fn main()` / braces may surround them, but it does not replace or add to the five lines
- **Each line is one natural phrase**, a short, complete statement that could be spoken in a single breath
- No line-length budget, no rhythm, no seasonal vocabulary, just five clean lines

This is the most forgiving form in the family, and the hardest to fake: free verse still needs each line to be worth its place.

## Core Patterns

### Sum Gogyohka
Five natural lines, no counting.

```python
words = input().split()
total_words = len(words)
the_count = total_words
result = str(the_count)
print(result)
```

### File Gogyohka
A small report in five meaningful lines.

```python
import sys
lines = sys.stdin.read().splitlines()
words = sum(len(l.split()) for l in lines)
nonempty = [line for line in lines if line.strip()]
print(f"{len(nonempty)} lines, {words} words")
print("the report is complete")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the lines.** Rewrite the correct program as exactly five complete logic lines. Make each line carry one natural step; do not split or merge lines to imitate a numeric meter.
3. **Verify the form.** Run it again, and confirm the output is unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it checks the five-line boundary. Treat any whitespace-length profile it prints as diagnostic only, not a target to optimize.
4. **Report the line roles.** State what each of the five lines does in one short phrase so a reviewer can verify the five-step arc without treating token counts as a target.

## Template-first construction

Do not invent a five-line gogyohka from a blank page. Start by copying the first passing Python example in this skill, then adapt its slots to the user's task:

1. Preserve exactly five nonblank, non-comment, non-import logic lines — never four (the dominant failure mode is collapsing to 4) and never six.
2. Each line is one natural step of the computation: read, split, convert, compute, print. Do not merge two steps onto one line with a semicolon — gogyohka is one-breath-per-line, so a semicolon-packed line is a violation.
3. The five lines form the full arc of the task: if your solution is only 3-4 lines, split a real step into its own line (e.g. separate the conversion from the computation) rather than padding.
4. Replace the example's data handling with the real task work; never leave poetic filler, dead assignments, or fake output.
5. After every edit, run the program for the requested input, then run `scripts/rhythm_check.py solve.py`; it verifies the five-line boundary. If it reports 4 lines, split a real step into its own line.

This copy-then-adapt method is intentional: it preserves a known-valid five-line shape while leaving the computation task-specific.


## Token Counts and Line Roles

Tokens are a mechanical diagnostic, not a meter. A token count is a reproducible whitespace-based measurement of a visible logic line; it does not decide whether the line is meaningful or how long it should be. The checker may print token diagnostics for automated tests, but never pad or compress code to hit a number.

Build five meaningful line roles:

1. **Name the input step.** Read or receive the data the task actually needs.
2. **Name the preparation step.** Parse, normalize, or select the useful values.
3. **Name the computation step.** Perform the central transformation or calculation.
4. **Name the result step.** Derive the value or report that answers the task.
5. **Name the landing step.** Print or return the answer in the required format.

These are roles, not a mandatory algorithm. A task may combine or reorder roles when that is the cleanest correct five-line solution, but it must still contain exactly five real logic lines. Do not add filler, explanatory print statements, dead assignments, or artificial line breaks. Do not collapse several required steps into three lines merely because the code can be shorter.

After adjusting, run `scripts/rhythm_check.py solve.py`; it verifies the five-line boundary and prints the token profile. Use that profile to spot accidental extra or missing logic lines, never to manufacture a meter.

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- exactly 5 logic-carrying lines of code (not fewer and not more); language-mandated ceremony like `fn main()` / braces may surround them but does not count as a logic line
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the gogyohka actually runs and produces the correct result for the task
- each line is a natural, complete short statement, one meaningful step per line
- no metered padding: lines are as long as the phrase needs, never stretched to fit a count
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report five visible logic-line counts without applying a meter, while checking one-breath-per-line and semicolon/branching constraints separately; this diagnostic must not turn free verse into tanka.

These requirements exist because a theme without a spec produces vibes, not output. A gogyohka that chases numeric measures is a tanka in disguise; a gogyohka that doesn't run is five dead breaths.

## Boundaries

This skill is not for any arbitrary five-line snippet or generic brevity. Without an explicit gogyohka request or the free-rhythm five-line contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names gogyohka or requests free-form five-line code. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Gogyohka Aesthetic

Write code that:
- has exactly five logic-carrying lines, never padded
- makes each line a natural phrase you could say out loud
- keeps no numeric token budget; lines are as long as the thought takes
- reads with modern, natural rhythm
- ends on the last line, not a formula

## Examples of Gogyohka Beauty

- **Sums**: read, split, convert, add, print, five lines
- **Reports**: lines, words, and the one number that matters, without padding token counts
- **Filters**: the list, the rule, the survivors, the count
- **Small Servers**: import, class, one handler, serve
- **Free Verse Tools**: anything that fits five natural lines

## The Gogyohka Promise

Remember: "Five lines, no token target, no rules but the shape. The meter is gone, what remains is the honest phrase, and it runs."

## Cross-Language Examples

Free verse translates everywhere:

```javascript
import { readFileSync } from "fs";
// breath one
const data = readFileSync(0, "utf8").split("\n");
// breath two
const nonempty = data.filter(line => Boolean(line));
// breath three
const words = nonempty.join(" ").split(/\s+/).length;
// breath four
const report = `${nonempty.length} lines`;
// breath five
console.log(`final report ${report}, ${words} words`);
```

```rust
use std::io::{self, BufRead};
fn main() {
// breath one
let lines: Vec<String> = io::stdin().lock().lines().map(|l| l.unwrap()).collect();
// breath two
let nonempty: Vec<&String> = lines.iter().filter(|l| !l.trim().is_empty()).collect();
// breath three
let words: usize = nonempty.iter().map(|l| l.split_whitespace().count()).sum();
// breath four
let report = format!("{} lines", nonempty.len());
// breath five
println!("count {}, {} words", report, words);
}
```

For other languages, translate the same structure: five natural lines, one meaningful step each.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it verifies the five-line boundary and prints a whitespace profile for diagnostics. Refine until the five-line check passes, then report the five line roles with the solution rather than optimizing the diagnostic profile.
