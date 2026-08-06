---
name: katauta
description: >-
  Write runnable code in a katauta form: one three-line, 5-7-7 program that addresses its subject directly and ends with a heavy two-line tail. Activate only for an explicit katauta, 5-7-7 half-poem, or directly addressed fragment request.
---

# Katauta Skill

A katauta is the half-poem, three lines, 5-7-7, a fragment of song that was always meant to be answered. It speaks directly to its subject, with the urgency of a message addressed to someone. A code katauta is three lines that address their data head-on, with a short opening and a heavy two-line tail.

## Philosophy

"A katauta is half a conversation, addressed to you."

The katauta mindset:
1. **Three lines**: 5-7-7 tokens, short opening, heavy falling tail
2. **Addressed**: the code speaks directly to its subject, the data, the user, the question
3. **A fragment**: it stands alone but aches to be answered, pair it for a sedoka
4. **Urgency**: the tone is direct, intimate, immediate
5. **Actually works**: a katauta that doesn't run is a message never delivered

## The Syllable Question: what 5-7-7 means in code

Tokens are the code analog of syllables. The katauta's rhythm differs from the haiku's:

- **Line 1, 5 tokens**: the opening. Short, direct, addressed to the subject.
- **Lines 2-3, 7-7 tokens**: the heavy tail. The weight of the message, landing twice.

Where a haiku ends light (5), a katauta ends heavy (7-7), the message falls, then falls again. Approximate ±2; the falling tail is the signature, padding is forbidden.

## Core Patterns

### Addressed Mode
The code answers its data directly, "to you".

```python
from collections import Counter
c = Counter([1, 2, 2, 3, 2, 4])
print("to you:", c.most_common(1)[0][0])
```

### Half-Poem Answer
A question, answered in three lines that feel like the first half of a longer reply.

```python
import sys
words = sys.stdin.read().lower().split()
print(len(words), "words, all yours")
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 3 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the katauta actually runs and produces the correct result for the task
- the code addresses its subject directly (an "to you" output, a direct answer, an intimate print)
- the ending is the heavy part, the last two lines carry the weight
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the three visible logic-line token counts against `[5, 7, 7]` with ±2 tolerance, and assess direct address separately; the heavy tail must not be padded.

These requirements exist because a theme without a spec produces vibes, not output. A katauta without the direct address is just a shorter haiku; a katauta that doesn't run is a message with no recipient.

## Boundaries

This skill is not for any three-line program or an unaddressed short response. Without an explicit katauta request and its directly addressed 5-7-7 fragment contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names katauta or requests a directly addressed 5-7-7 fragment. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Katauta Aesthetic

Write code that:
- is three lines or fewer
- keeps the 5-7-7 rhythm, short opening, heavy tail
- speaks to its subject in the output ("to you:", a direct answer)
- feels like a fragment, complete alone, but aware it could be answered
- ends with the falling weight, not a trailing thought

## Examples of Katauta Beauty

- **Addressed Modes**: "to you: the answer"
- **Direct Answers**: a question, answered without flinching
- **Fragments**: one result that aches to be paired
- **Urgent Counts**: the number that matters, delivered like a message
- **Half-Songs**: three lines that a sedoka would complete

## The Katauta Promise

Remember: "Three lines, heavy at the end, spoken directly to you. A fragment that stands alone, until someone answers it."

## Cross-Language Examples

The 5-7-7 rhythm and the direct address translate everywhere:

```javascript
const counts = new Map();               // opening
[1, 2, 2, 3, 2, 4].forEach(x => counts.set(x, (counts.get(x) ?? 0) + 1));  // the work
console.log("to you:", [...counts].sort((a, b) => b[1] - a[1])[0][0]);     // the falling answer
```

```rust
fn main() {                              // ceremony, free
    let data = [1, 2, 2, 3, 2, 4];
    let mode = data.iter().max_by_key(|x| data.iter().filter(|y| y == x).count()).unwrap();
    println!("to you: {mode}");          // the falling answer
}
```

For other languages, translate the same structure, short opening, direct address, heavy tail.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.
