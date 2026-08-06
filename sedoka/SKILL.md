---
name: sedoka
description: >-
  Write code as a sedoka: a 6-line program in two 3-line stanzas (5-7-7 / 5-7-7 tokens)
  where the second stanza mirrors the first - a question and its answer, a pass and its
  reverse, a count and its echo. Use this skill when the user wants a mirrored or
  response-shaped 6-line program. Make sure to use this skill whenever the user mentions
  sedoka, 6-line poems, two-stanza programs, 5-7-7, or question-and-response code. This
  skill is NOT for single 3-line stanzas (use haiku, senryu, lunes, or katauta) and NOT
  for 5-line forms (use tanka or gogyohka).
---

# Sedoka Skill

A sedoka is two katauta halves answering each other, six lines, two stanzas, and the second stanza mirrors the first like a conversation: a question and its answer, a longing and its reply. A code sedoka is six lines in two 3-line stanzas, where the second stanza processes the same data in a mirrored way.

## Philosophy

"A sedoka is a song sung by two voices."

The sedoka mindset:
1. **Six lines**: two 3-line stanzas, 5-7-7 / 5-7-7 tokens
2. **The mirror**: stanza two answers stanza one, reverse, complement, second pass
3. **Question and response**: the first half asks or acts; the second half answers or reflects
4. **Two katauta halves**: each stanza stands alone, together they converse
5. **Actually works**: a sedoka that doesn't run is a dialogue that never happened

## The Syllable Question: what 5-7-7 / 5-7-7 means in code

Tokens are the code analog of syllables. A sedoka's rhythm is two falls:

- **Stanza one, 5-7-7 tokens (lines 1-3)**: the question. Setup, the act, the result.
- **Stanza two, 5-7-7 tokens (lines 4-6)**: the response. The same data, mirrored, reversed, complemented, recounted.

The 7-7 ending of each stanza is a heavy tail, the stanza lands with weight, and the second stanza echoes that landing. Approximate ±2 per line; the mirror is the point, padding is forbidden.

## Core Patterns

### Forward / Reverse Sedoka
One list, two walks, the question and its echo.

```python
nums = [3, 1, 4, 1, 5]
total = sum(nums)
forward = f"sum {total}"
rev = nums[::-1]
total2 = sum(rev)
print(forward, "reverse", total2)
```

### Count / Rare Sedoka
The first stanza counts; the second answers with what was almost missed.

```python
from collections import Counter
import sys
counts = Counter(sys.stdin.read().lower().split())
common = counts.most_common(1)
rare = min(counts, key=counts.get)
print(common, "and rarely:", rare)
```

## Boundaries, when NOT to use this skill (use a different skill instead)

This skill is **not for** every poetic-code request. When the user asks for one of the following, **instead use** the listed skill, the goal is that two skills never coin-flip on the same prompt:

- a single 3-line stanza -> haiku, senryu, lunes, or katauta
- 5-line forms -> tanka (strict meter) or gogyohka (free form)
- prose-with-haiku -> haibun
- shortest-possible / golfed code -> esoteric-programming

Sedoka is the two-stanza form. One stanza is a katauta; five lines is a tanka or gogyohka; a sedoka needs both halves to converse.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 6 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the sedoka actually runs and produces the correct result for the task
- two 3-line stanzas: the first acts or asks, the second mirrors the same data (reverse, complement, recount)
- every line is a real statement or expression, no filler to reach the count
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report both stanza shapes against `[5, 7, 7, 5, 7, 7]` with ±2 tolerance and retain the blank-line stanza boundary; rhythm is diagnostic, while mirror and pivot checks remain independent.

These requirements exist because a theme without a spec produces vibes, not output. A sedoka without the mirror is two unrelated half-poems; a sedoka that doesn't run is a conversation neither side finished.

## When to Use Sedoka Patterns

Use sedoka code when:
- the same data deserves two views, forward and reverse, common and rare
- the user wants a question-and-response shaped program
- one result needs an echo
- the user says "mirror it", "answer it", or "the other side"

## The Sedoka Aesthetic

Write code that:
- is six lines or fewer, in two clear stanzas
- makes stanza two a true mirror of stanza one
- uses the 5-7-7 rhythm with its heavy falling tail
- names the two halves like a dialogue (forward/reverse, ask/answer)
- ends with the response, not a re-statement

## Examples of Sedoka Beauty

- **Forward / Reverse**: the same sum, walked both ways
- **Count / Rare**: the common word, answered by the almost-missed one
- **Ask / Answer**: a query, then the truth the data returned
- **Fast / Slow**: the same request, timed twice
- **Before / After**: the state, then the change it underwent

## The Sedoka Promise

Remember: "Two voices, one song. The first stanza acts, the second answers, and together six lines say what three never could."

## Cross-Language Examples

The two-voice structure translates everywhere:

```javascript
const nums = [3, 1, 4, 1, 5];            // stanza one: the question
const total = nums.reduce((a, b) => a + b, 0);
const forward = `sum ${total}`;
const rev = [...nums].reverse();         // stanza two: the answer
const total2 = rev.reduce((a, b) => a + b, 0);
console.log(forward, "reverse", total2);
```

```rust
fn main() {                              // ceremony, free
    let nums = [3, 1, 4, 1, 5];
    let total: i32 = nums.iter().sum();
    let forward = format!("sum {total}");
    let rev: i32 = nums.iter().rev().sum();   // the mirror
    println!("{forward} reverse {rev}");
}
```

For other languages, translate the same structure, stanza one, then the mirror.

## Bundled Helpers

If the walk needs randomness or ASCII scenery, reuse the shared toolkit:

- `shared/rng.py`, seeded RNG and choice helpers
- `shared/ascii_canvas.py`, ASCII canvas for rendering the mirror

A sedoka may import one of these in its first stanza, it counts toward the six lines.
