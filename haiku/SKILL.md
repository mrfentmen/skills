---
name: haiku
description: >-
  Write runnable code in a haiku form: a compact nature-or-moment program with a 5-7-5 token rhythm, at most three logic lines, and a setup, turn, and landing. Activate only when the user explicitly requests a code haiku, 5-7-5 structure, or a three-line moment program.
---

# Haiku Skill

Write code as a haiku, three lines, each doing real work, the whole thing runs. No boilerplate. No filler. No placeholders. A complete moment of computation, captured in three dense lines. Aim each line at its count as you write: line 1 about 5 tokens, line 2 about 7 (the dense turn), line 3 about 5, choosing short names and tight expressions so the rhythm holds without padding; if a line overshoots, simplify it, never split or pad it.

## Philosophy

"A haiku is the distilled essence of a moment. A code haiku is the distilled essence of a task."

The haiku mindset:
1. **Three lines or fewer**: setup, turn, landing, one breath. Prefer three when the shape fits; never pad to make three.
2. **Tokens are syllables**: line 1 ~5 tokens, line 2 ~7 (the dense heart), line 3 ~5, approximate, never padded
3. **Actually works**: if it doesn't run, it's not a haiku, it's a broken poem
4. **The kigo**: one word (variable/function name) that names the moment, like a seasonal word
5. **No boilerplate bullshit**: imports and the one dense line are the haiku, not forty lines of ceremony

## The Syllable Question: what 5-7-5 means in code

Real haiku count syllables, 5 in line one, 7 in line two, 5 in line three. Code has no syllables, but it has **tokens**: the atomic pieces the language reads (`x`, `=`, `42`, `for`, `in`, `range`, `(`). Tokens are the natural "beats" of a line, the closest analog to syllables.

So a code haiku follows the shape:

- **Line 1, 5 tokens**: setup. What we have, the world before.
- **Line 2, 7 tokens**: the turn (the kigo line). The dense transformation, the moment of change.
- **Line 3, 5 tokens**: landing. The result, the world after.

Treat the counts as a rhythm, not a law: ±2 slack is fine, and a line may carry multiple statements (`;`, chained calls, lambdas), density is the point. NEVER pad with dead code to hit a count; a 3-line haiku with three working lines beats a padded one.

The budget is conserved when you use fewer lines: two lines collapse to ~12 tokens (5+7) then ~5, one line to ~17; the landing line stays the short ~5. Fewer lines is legal, rhythm is not optional - `scripts/rhythm_check.py` enforces the silhouette at any line count.

Shaping the counts: the same logic can be written long or tight. Short names and fewer method calls buy tokens back. For a max report, the verbose version runs 3-7-4:

```python
all_nums = input().split()
best = max(int(x) for x in all_nums)
print("the max is", best)
```

The tight version lands 3-7-5, dead on the classic silhouette, with no padding - the turn compresses "the max is" narration so the landing stays short:

```python
import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
print("max", max(nums), "of", "them", "all")
```

(Profiles: [3, 7, 4] → [3, 7, 5]. Verify any tightening with `scripts/rhythm_check.py`.)

When a line overshoots, tighten the expression itself (shorter names, one operation per line, drop an f-string for a plain print, swap a comprehension for a filter). Do not split the line into more lines and do not pad it.

## Workflow

Shape the haiku in passes, correctness first, form second:

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Compress into the moment.** Merge the logic into at most three dense lines with a setup, turn, and landing, aiming each line at the silhouette (5-7-5 on three lines, ~12/5 on two, ~17 on one): shorter names, comprehensions, lambdas, filters, one operation per line. Imports and comments are free ceremony.
3. **Verify the form.** Run it again - the output must be unchanged and correct. Then run `scripts/rhythm_check.py solve.py` (or count by hand) and tighten any line outside ±2 by simplifying the expression; never split a line into more, never pad.
4. **Report the counts.** State the logic-line token profile with the solution so a reviewer can check the rhythm without counting.

If the task cannot fit the silhouette without breaking correctness, say so and deliver the correct plain implementation rather than a fake haiku.


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

## Core Patterns

### Complete-Program Haiku
The whole task in three lines, import, transform, output. Run it and it's done.

```python
import sys
fizz = lambda i: "Fizz" * (i%3<1) + "Buzz" * (i%5<1) or i
sys.stdout.write("\n".join(map(str, map(fizz, range(1, 101)))))
```

### Function Haiku
A dense function/expression you can drop into existing code, the task as a unit.

```python
import sys
nums = [int(x) for x in sys.stdin.read().split()]
print("sum", sum(nums), "is", "the", "tale")
print("and", "the", "count", "is", len(nums), "now")
```

### The Kigo Line
One name carries the moment, like a seasonal word in a poem. The middle line does the heavy lifting and the name says what season this is.

```python
import re, sys
from collections import Counter
text = sys.stdin.read().lower()
words = Counter(re.findall(r"[a-z']+", text))  # the tally
print("top", words.most_common(5), "now")
```

### Zero-Ceremony Server
Even a server fits in three lines when you stop treating boilerplate as sacred.

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
H = type("H", (BaseHTTPRequestHandler,), {"do_GET": lambda s: (s.send_response(200), s.end_headers(), s.wfile.write(b"haiku"))})
HTTPServer(("", 8000), H).serve_forever()
```

## Scope

This file is self-contained. Apply it only when the request explicitly names this skill or matches the exact form, structural contract, or persona described here. Do not search for, load, import, or assume any companion skill, repository path, helper file, or external routing document. If the request does not match this contract, answer normally without activating this skill.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 3 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the haiku actually runs and produces the correct result for the task
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- the middle line (the turn) does the heaviest lifting whenever the task has a natural setup/turn/landing shape
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

- rhythm self-check: after writing, count the tokens on each logic line (imports and comments are free) and tighten any line that is outside ±2 of the silhouette (`[5, 7, 5]` on three lines, `[12, 5]` on two, `[17]` on one) by shortening names or simplifying expressions; never split a line into more, never pad
- bundled checker: `scripts/rhythm_check.py solve.py` prints the token profile and fails any line outside ±2; run it when you can, or count by hand, and report the three counts with the solution

Benchmark signature: the visible logic-line token counts against the conserved 5-7-5 silhouette - `[5, 7, 5]` on three lines, `[12, 5]` on two, `[17]` on one - with ±2 tolerance; a diagnostic that drives the tightening step, never a reason to pad or add dead code.

These requirements exist because a theme without a spec produces vibes, not output. A haiku that doesn't run is just a broken poem, the run is the whole point.

## Boundaries

This skill is not for generic short code, any three-line snippet, or an arbitrary compact program. Without an explicit haiku request or the 5-7-5 moment contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names haiku/code haiku, requests a 5-7-5 structure, or requests a three-line moment program. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Haiku Aesthetic

Write code that:
- is three lines or fewer, as many as the task demands, never more
- reads like a poem: setup, turn, landing
- uses a kigo, one name that captures the moment
- prefers the densest honest expression (lambdas, comprehensions, chained calls)
- imports only what the line needs, nothing decorative

## Examples of Haiku Beauty

- **FizzBuzz**: the classic, in three lines, runnable
- **Word Frequency**: a poem about a text, counting its words
- **Prime Factors**: recursion so tight it fits in a lambda
- **Tiny Servers**: HTTP in three lines, zero framework
- **Dense Reducers**: sums, averages, modes as one-liners

## The Haiku Promise

Remember: "A haiku captures a single moment. A code haiku captures a single task, completely, in three lines, and it runs. If it doesn't run, it's not a haiku, it's a broken poem."

## Cross-Language Examples

The syllable rule is language-agnostic. Same spirit, translated:

```javascript
// setup: the add
const nums = [1, 2, 3, 4];
// turn: the fold
const total = nums.reduce((a, b) => a + b);
// landing: the number
console.log(`sum is ${total}`);
```

```rust
fn main() {
    // setup: the fold
    let nums = [1, 2, 3, 4];
    // turn: the running sum
    let total: i32 = nums.iter().sum();
    // landing: the number
    println!("sum is {total}");
}
```

```go
package main
import "fmt"
func main() {
    // setup: the empty ledger
    total := 0
    // turn: the tally
    for _, n := range []int{3,1,4,1,5} { total+=n }
    // landing: the answer
    fmt.Println("sum is", total)
}
```

```bash
#!/bin/bash
# setup: the flock
nums=(3 1 4 1 5)
# turn: the tally
for n in "${nums[@]}"; do ((total += n)); done
# landing: 14
printf '%s\n' "$total"
```

For other languages (C...), translate the same structure, imports/setup, the dense turn, the landing output.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
