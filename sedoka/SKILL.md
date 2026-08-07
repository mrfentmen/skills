---
name: sedoka
description: >-
  Write runnable code in a sedoka form: two distinct three-line stanzas shaped 5-7-7 / 5-7-7, with the second stanza mirroring or answering the first. Activate only for an explicit sedoka, two-stanza response, or 5-7-7 / 5-7-7 request.
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
forward = "sum " + str(sum(nums))
print(forward, "is", "the", "sum", "now")

rev = nums[::-1]
backward = "sum " + str(sum(rev))
print(backward, "is", "the", "mirror", "sum")
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

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the sedoka form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
3. **Verify the form.** Run it again, the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py`; it prints the logic-line token profile and fails any line outside the form's tolerance, so tighten what it flags by simplifying the expression, never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

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

## Boundaries

This skill is not for two unrelated snippets or any ordinary paired response. Without an explicit sedoka request and two mirrored 5-7-7 stanzas, handle the request normally.

## Activation

Activate this skill only when the user explicitly names sedoka or requests two 5-7-7 stanzas in a response structure. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

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

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
