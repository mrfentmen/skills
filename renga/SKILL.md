---
name: renga
description: >-
  Write code as a renga: a linked chain of poem-stanzas that becomes one complete working
  program - alternating 5-7-5 stanzas (3 lines) and 7-7 couplets (2 lines), where each
  stanza hands its result to the next through a shared pivot, like the kakekotoba that
  linked ancient linked-verse. Use this skill when the user wants a multi-part pipeline
  shaped as linked verse, a program built from stanzas that chain, or the social form of
  the haiku family - each stanza continues where the last left off. Make sure to use this
  skill whenever the user mentions renga, linked verse, chain poems, stanza pipelines,
  alternating 5-7-5 and 7-7 stanzas, or wants code where each part hands off to the next.
  This skill is NOT for a single 3-line moment (use haiku), NOT for one long alternating
  poem (use choka), NOT for prose-with-verse (use haibun), and NOT for 4 or 5-line single
  forms (use dodoitsu, tanka, or gogyohka). For the rest of the poetic family, use: haiku
  for the single moment, choka for the long alternating poem, and dodoitsu for the 4-line
  folk form.
---
# Renga Skill

A renga is a linked poem: many stanzas written by many poets, each continuing where the last left off. The stanzas alternate, a 5-7-5 (three lines) then a 7-7 couplet (two lines), and each is joined to its neighbor by a pivot: the kakekotoba, a word that ends one stanza and begins the next. A code renga is a program built from linked stanzas, each handing its result to the next through a pivot variable.

## Philosophy

"The renga is the social form of the family. No stanza is complete alone; each exists to be continued. A code renga is a pipeline where every stage is a verse, and the pivot variable is the kakekotoba that carries the poem forward."

The renga mindset:
1. **Stanzas, not lines**: the unit is the stanza, 3 lines (5-7-5) or 2 lines (7-7), and the poem is 3+ stanzas chained
2. **Alternating shape**: 5-7-5 stanza, then 7-7 couplet, then 5-7-5, then 7-7... the classic renga alternation
3. **The pivot**: each stanza ends by binding a variable (the kakekotoba) that the next stanza opens by reading, the hand-off IS the link
4. **Linked, not independent**: unlike sedoka's mirrored stanzas, renga stanzas are sequential, stanza n+1 cannot exist without stanza n's result
5. **Actually runs**: a renga that doesn't run end-to-end is a party where nobody shows up

## The Alternating Structure

```
stanza 1 (hokku, 3 lines):  ~5 / ~7 / ~5     the opening - sets the scene, binds the first pivot
stanza 2 (couplet, 2 lines): ~7 / ~7         develops - opens on the pivot, binds the next
stanza 3 (3 lines):          ~5 / ~7 / ~5     turns - opens on the pivot, binds the next
stanza 4 (couplet, 2 lines): ~7 / ~7         closes - opens on the pivot, lands the result
```

Each stanza is one stage of the computation. The pivot is the variable that flows through the chain, the poem's thread.

## Core Patterns

### The Chain Pipeline
Three stages, two hand-offs, one result:

```python
raw = open("log.txt").read()                    # 5: the words arrive
rows = [l for l in raw.splitlines() if l]       # 7: the lines stand, filtered
errors = [l for l in rows if "ERROR" in l]      # 5: the troubles gather
warns = [l for l in rows if "WARN" in l]        # 7: the near misses too
story = f"{len(errors)} errors, {len(warns)} warns"  # 7: the count becomes the tale
print(story)                                    # 7: the tale is told - the couplet closes
```

### The Transforming Renga
Each stanza reshapes the pivot:

```python
text = open("notes.txt").read().lower()         # 5: the diary speaks
tokens = text.split()                           # 7: the words break free
seen = set(tokens)                              # 5: the kinds are known
freq = sorted(((tokens.count(w), w) for w in seen), reverse=True)  # 7: the loudest first
top = freq[:5]                                  # 7: the five who shout
print("leaders:", " ".join(w for _, w in top))  # 7: the couplet crowns them
```

### The Long Renga
Four stanzas when the task needs four stages:

```python
nums = [int(x) for x in input().split()]        # 5: the numbers march in
total = sum(nums)                               # 7: the tally swells
n = len(nums)                                   # 5: and its count
mean = total / n                                # 7: the center appears
above = sum(1 for x in nums if x > mean)        # 7: the outliers vote
print(f"mean {mean:.1f}, {above} above it")     # 7: the couplet - the verdict
```

## Boundaries, when NOT to use this skill

- a single 3-line moment -> haiku
- 3-line humor punchlines -> senryu
- the 5-3-5 punch form -> lunes
- the 5-7-7 half-poem -> katauta
- the 3-line Korean twist form -> sijo
- the whole program on one line -> monoku
- 5-line expanded forms -> tanka / gogyohka
- the 4-line folk form -> dodoitsu
- one long alternating poem with a closing couplet -> choka
- prose body with a closing haiku -> haibun
- two mirroring stanzas -> sedoka
- minimal architecture across a codebase -> minimalist-zen

Renga is the chain form: three or more stanzas, alternating 5-7-5 and 7-7, each handing its pivot to the next.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following:

- at least 3 stanzas: alternating 3-line (5-7-5) and 2-line (7-7) stanzas, in that classic alternation
- the FIRST stanza is a 3-line 5-7-5 (the hokku opening)
- every stanza after the first OPENS by reading the previous stanza's pivot variable, the link must be visible in code
- line rhythm within stanzas: ~5 tokens on short lines, ~7 on long (±2 slack, never padded)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`
- the program actually runs end-to-end and produces the correct result
- the LAST stanza lands the result (the closing couplet tells the tale)
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report stanza-visible logic-line counts against `[5, 7, 5, 7, 7, 5, 7, 5]` with ±2 tolerance, while grading stanza count, blank-line boundaries, and pivot reuse independently.

## When to Use Renga Patterns

Use renga code when:
- the task is a pipeline: 3+ sequential stages, each transforming the last
- the user wants "a chain poem", "linked verse", or "stanzas that hand off"
- you want the social form: code that reads like many hands building one thing
- the middle stages are too few for choka's 6+ lines but too many for a single form

## The Renga Aesthetic

Write code that:
- is built from stanzas, each visibly opening on the previous one's pivot
- alternates 5-7-5 and 7-7 like the classical chain
- reads like a relay: every stanza exists to be continued
- lands at the end, the final couplet states what the whole chain achieved

## Cross-Language Examples

```javascript
const fs = require("fs");                              // 5: the door opens
const text = fs.readFileSync("data.txt", "utf8");      // 7: the words arrive
const nums = text.trim().split(/\s+/).map(Number);     // 5: the numbers stand
const mean = nums.reduce((a, b) => a + b, 0) / nums.length;  // 7: the center holds
const devs = nums.map(n => Math.abs(n - mean));        // 7: the distances grow
console.log(`mean ${mean.toFixed(2)}, spread ${devs.reduce((a, b) => a + b, 0).toFixed(2)}`);  // 7: the couplet
```

```bash
#!/bin/bash
words=$(tr '[:upper:]' '[:lower:]' < notes.txt | tr -cs '[:alpha:]' '\n' | grep -v '^$')  # 5-7: the words
top=$(echo "$words" | sort | uniq -c | sort -rn | head -1)                                # 7: the loudest
echo "winner: $top"                                                                       # 7: the couplet
```

## Bundled Helpers

If the task needs ASCII output, randomness, or decorative headers, reuse the shared toolkit, a renga may import a helper in its hokku stanza:

- `shared/ascii_canvas.py`, ASCII canvas with lines, circles, ink-density characters
- `shared/rng.py`, seeded RNG and value noise
- `shared/box_drawing.py`, box-drawing headers
