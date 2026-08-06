---
name: sijo
description: >-
  Write code as a sijo: a complete, working 3-line program in the Korean form - three
  LONGER lines (~15 tokens each) with a strict dramatic structure: line 1 states the
  theme, line 2 develops it, and line 3 delivers the TWIST, the surprise that reframes the
  whole task. Use this skill when the user wants a 3-line program whose ending turns the
  meaning, a solution with a volta or surprise ending, or Korean-style verse in code. Make
  sure to use this skill whenever the user mentions sijo, twist endings, volta, or wants
  three longer lines where the last one lands the surprise. This skill is NOT for the
  5-7-5 haiku (shorter lines, no twist requirement - use haiku), NOT for humor punchlines
  (use senryu), NOT for 1-line programs (use monoku), and NOT for 5-line forms (use tanka
  or gogyohka). For the rest of the poetic family, use: haiku for the 5-7-5 moment, senryu
  for humor, lunes for the 5-3-5 punch, katauta for the 5-7-7 half-poem, and monoku for
  the one-line extreme.
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
prices = [120, 8, 400, 15, 3, 99]                 # statement: the prices, unremarkable
avg = sum(prices) / len(prices)                   # development: the ledger sums
print(f"{avg:.2f} average, {len([p for p in prices if p > avg])} above it")  # twist: the average is a stranger to most
```

### The Reveal Sijo
The third line exposes what lines 1-2 were building toward:

```python
text = open("diary.txt").read().lower()           # statement: the diary
words = text.split()                              # development: the words
print("most said:", max(set(words), key=words.count), "- said", words.count(max(set(words), key=words.count)), "times")  # twist: one word confesses everything
```

### The Turn on the Reader
The output reframes the task:

```python
queries = ["login", "login", "logout", "login"]   # statement: the requests
print("unique:", len(set(queries)))               # development: counting kinds
print("actual:", len(queries), "- repetition is the real story")  # twist: the count that mattered was the boring one
```

## Boundaries, when NOT to use this skill

- short 5-7-5 lines, nature moment, kigo -> haiku
- humor punchline as the point -> senryu
- the razor-thin 5-3-5 middle -> lunes
- the 5-7-7 half-poem addressed to its subject -> katauta
- the whole program on one line -> monoku
- 5-line expanded forms -> tanka / gogyohka
- 4-line folk form -> dodoitsu
- long alternating verse -> choka
- linked chains of stanzas -> renga

Sijo is the twist form: longer lines than haiku, and the third line must turn the meaning.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following:

- exactly 3 lines of code that carry logic (language-mandated ceremony is free)
- lines are LONGER than haiku's: each ~15 tokens (14-16 rhythm, ±3 slack)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`
- the program actually runs and produces the correct result
- **the third line contains a genuine twist**: a surprise, inversion, reframe, or reveal that changes the meaning of lines 1-2, explainable as "line 3 reveals that ..."
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

## When to Use Sijo Patterns

Use sijo code when:
- the user wants three lines but with room to breathe, longer lines, real structure
- the task has a natural reveal: the data's shape, a hidden property, an irony
- the user asks for a "twist ending", a "surprise", or "make the last line change everything"
- you want a program whose OUTPUT reframes its INPUT

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
words=$(tr '[:upper:]' '[:lower:]' < notes.txt | tr -cs '[:alpha:]' '\n' | grep -v '^$')  # statement
counts=$(echo "$words" | sort | uniq -c | sort -rn | head -1)                            # development
echo "winner: $counts - the rest are noise"                                               # twist
```

## Bundled Helpers

If the task needs ASCII output, randomness, or decorative headers, reuse the shared toolkit:

- `shared/ascii_canvas.py`, ASCII canvas with lines, circles, ink-density characters
- `shared/rng.py`, seeded RNG and value noise
- `shared/box_drawing.py`, box-drawing headers

A sijo may import one of these on its statement line, that still counts as one of the three.
