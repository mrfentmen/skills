---
name: sijo
description: >-
  Write runnable code in a sijo form: exactly three deliberately long logic lines, with the third line delivering a genuine twist, inversion, or reframe of the first two. Activate only for an explicit sijo, Korean verse, or three-line twist-ending request.
---
# Sijo Skill

A sijo is a Korean classical poem: three lines, each ~14-16 syllables, with a strict dramatic arc, statement, development, twist. A code sijo is a three-line program where the third line turns the whole thing: the surprise that reframes what the first two lines did.

## Philosophy

"A sijo is the art of the twist. The first line sets the stage, the second builds, and the third, quietly, inevitably, turns everything on its head. A code sijo is three longer lines where the ending is the point."

The sijo mindset:
1. **Three lines, longer lines**: ~15 tokens each (~14-16, the code analog of Korean syllables), these are NOT haiku's short 5-7-5 lines
2. **Line 1, statement**: the theme, the world as given (setup, but roomier than haiku's)
3. **Line 2, development**: the work, the expansion, the tension building
4. **Line 3, the twist**: the volta, a genuine surprise that reframes lines 1-2. The twist is the form.
5. **Actually runs**: a sijo that doesn't run is a monologue, not a program

## The Twist: what counts

The third line must contain a **genuine turn**, not just a punchline, not just the answer. Good code-sijo twists:

- **The inversion**: the data reveals the opposite of what the setup implied (the "average" that hides the outlier)
- **The reframe**: the same computation seen from a different angle (counting what was supposed to be summed)
- **The reveal**: a hidden property of the input surfaces only in line 3 (the sorted list's first element was there all along)
- **The turn on the reader**: the program's output comments on the task itself

The twist must be explainable in one sentence: "line 3 reveals that...", if you can't finish that sentence, there is no twist.

## Core Patterns

### The Inversion Sijo
The setup promises a total; the twist reveals the shape of the data:

```python
print("the", "sum", "of", "the", "numbers", "is", "the", "first", "long", "line", "of", "the")
print("song", "and", "the", "count", "of", "every", "row", "is", "the", "second", "long", "line")
print("the", "third", "line", "twists", "the", "tale", "yet", "the", "sum", "still", "stands", "tall")
```

### The Reveal Sijo
The third line exposes what lines 1-2 were building toward:

```python
print("the", "diary", "says", "most", "often", "the", "word", "is", "the", "first", "truth", "here")
print("and", "the", "count", "of", "every", "row", "is", "the", "second", "long", "line", "of")
print("the", "third", "line", "twists", "the", "tale", "yet", "the", "word", "still", "stands", "tall")
```

### The Turn on the Reader
The output reframes the task:

```python
print("the", "queries", "arrive", "and", "the", "count", "of", "kinds", "is", "the", "first", "truth")
print("and", "the", "count", "of", "all", "the", "calls", "is", "the", "second", "long", "line")
print("the", "third", "line", "twists", "the", "tale", "yet", "repetition", "is", "the", "real", "story")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the sijo form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

Every deliverable produced with this skill must be gradeable. You must include ALL of the following:

- exactly 3 lines of code that carry logic (language-mandated ceremony is free)
- lines are LONGER than haiku's: each ~15 tokens (14-16 rhythm, ±3 slack)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`
- the program actually runs and produces the correct result
- **the third line contains a genuine twist**: a surprise, inversion, reframe, or reveal that changes the meaning of lines 1-2, explainable as "line 3 reveals that ..."
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

## Boundaries

This skill is not for any three-line script or a final line that merely repeats the setup. Without an explicit sijo request and three long lines ending in a genuine twist, handle the request normally.

## Activation

Activate this skill only when the user explicitly names sijo or requests three long lines ending in a genuine twist. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Sijo Aesthetic

Write code that:
- is three lines, each doing real work, longer and more deliberate than haiku
- builds tension across lines 1-2 and detonates it on line 3
- uses the twist as the organizing idea: the whole program exists for that last line
- names things so the twist lands (the variable that seemed boring turns out to be the story)

## Cross-Language Examples

```javascript
const nums = [3, 1, 4, 1, 5, 9, 2, 6];       // statement: the numbers
const total = nums.reduce((a, b) => a + b, 0);  // development: the sum
console.log(total - Math.max(...nums), "without the largest");  // twist: the total minus the outlier
```

```bash
#!/bin/bash
# statement: the counts
words=$(tr '[:upper:]' '[:lower:]' < notes.txt | tr -cs '[:alpha:]' '\n' | grep -v '^$')
# development: the loudest
counts=$(echo "$words" | sort | uniq -c | sort -rn | head -1)
# twist: the outlier wins
echo "the winner is $counts, and all of the rest is noise"
```

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
