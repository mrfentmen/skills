---
name: dodoitsu
description: >-
  Write runnable code in a dodoitsu form: exactly four logic lines shaped 7-7-7-5, with three working lines and a plain, shorter settlement line. Activate only for an explicit dodoitsu, folk verse, or 7-7-7-5 request.
---
# Dodoitsu Skill

A dodoitsu is a Japanese folk poem: four lines, 7-7-7-5, three full lines of statement and one short line that settles it. It's the plain-spoken form: work, love, everyday life, said directly. A code dodoitsu is a four-line program: three lines that carry the load, one short line that lands the result.

## Philosophy

"The dodoitsu is the workhorse of the family. Haiku is a moment, sijo is a twist, choka is an epic, dodoitsu is the four-line verse that gets the job done and says it plainly at the end."

The dodoitsu mindset:
1. **Four lines, 7-7-7-5**: the first three lines are full (~7 tokens each, the work), the last line is short (~5 tokens, the landing)
2. **Weight on the front**: lines 1-3 carry the computation; the fourth line is a quick, plain statement of the result
3. **No twist required**: unlike sijo, the dodoitsu doesn't need a volta, it needs a *settlement*. The last line closes the matter plainly
4. **Plain-spoken**: folk form, no preciousness, no ornament; the language of everyday work
5. **Actually runs**: a dodoitsu that doesn't run is a folk song with no chorus

## The 7-7-7-5 Shape

```
line 1   ~7 tokens   the first load: gather or set up
line 2   ~7 tokens   the second load: transform or work
line 3   ~7 tokens   the third load: finish the heavy lifting
line 4   ~5 tokens   the landing: the result, stated plainly
```

The last line is deliberately shorter, the code analog of the dodoitsu's 5-syllable close. It should read like a verdict: short, certain, done. ±2 slack per line, never padded.

## Core Patterns

### The Folk Tally
Count, weigh, and state, the classic everyday task:

```python
import sys
data = [float(x) for x in sys.stdin.read().split()]
mean = sum(data) / len(data)
print("mean", "is", "the", "sum", "over", "the", "count")
print("mean", mean, "of", "all")
```

### The Plain Average
No drama, just the number:

```python
nums = [int(x) for x in input().split()]
total = sum(nums)  # the tally grows
n = len(nums)  # and its count
print(total // n if n else "empty")
```

### The Household Ledger
A two-step transform with a short verdict:

```python
prices = {"milk": 3, "bread": 2, "eggs": 4}
cart = ["milk", "bread", "bread"]
due = sum(prices[i] for i in cart)
print(due, "dollars, cash or card")
```

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the dodoitsu form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

- exactly 4 lines of code that carry logic (language-mandated ceremony is free)
- the first three lines are full: ~7 tokens each (rhythm, ±2 slack, never padded)
- the FOURTH line is the short landing: ~5 tokens (fewer than the other three, the settlement)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`
- the program actually runs and produces the correct result
- the last line states the result plainly, it is the verdict, not a new question
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report four visible logic-line counts against `[7, 7, 7, 5]` with ±2 tolerance, while keeping the shorter final landing as an independent structural assertion.

## Boundaries

This skill is not for any ordinary four-line response or generic short code. Without an explicit dodoitsu request or the 7-7-7-5 contract with a shorter landing, handle the request normally.

## Activation

Activate this skill only when the user explicitly names dodoitsu or requests the 7-7-7-5 four-line form. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Dodoitsu Aesthetic

Write code that:
- is four lines: three full, one short, the last line visibly lighter
- speaks plainly: no ornament, no cleverness for its own sake
- settles the matter: the last line is a verdict, not a hook
- does real work on every one of the first three lines

## Cross-Language Examples

```javascript
// 7: the words arrive
const text = fs.readFileSync("t.txt", "utf8");
// 7: the words stand
const words = text.toLowerCase().match(/[a-z']+/g) || [];
// 7: the kinds are known
const unique = new Set(words);
// 5: the verdict
console.log(`${unique.size} distinct words`);
```

```bash
#!/bin/bash
# 7: the tally
total=0; count=0; echo tally ready
# 7: the loop
while read -r n; do
# 7: the sum and its count
total=$((total + n)); count=$((count + 1)); done < nums.txt
# 5: the settlement
echo "sum=$total over $count numbers"
```

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
