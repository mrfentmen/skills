---
name: haiku
description: >-
  Write code as a haiku: a complete, working program in three lines or fewer, following
  the 5-7-5 spirit with tokens as the code analog of syllables - a short setup, a dense
  middle turn, a short landing, and a kigo that names the moment. Use this skill when the
  user wants ultra-dense, boilerplate-free code that actually runs: 3-line solutions, one-
  shot scripts, terse functions, compact expressions that do real work. Make sure to use
  this skill whenever the user mentions code haiku, haiku style code, 5-7-5 code, 3-line
  programs, dense one-liners, no-boilerplate snippets, or asks to write it in three lines,
  condense a script, or finish a whole task in a few working lines. This skill is NOT for
  code golf or shortest-possible code (use esoteric-programming), NOT for minimal
  architecture across a whole codebase (use minimalist-zen), NOT for production
  scaffolding or enterprise review (use no-bullshit), and NOT for poetic comments or brush
  art (use zen-calligraphy). For the rest of the poetic family, use: tanka for a 5-line
  expanded form with reflection, senryu for a human-nature humor 3-liner with a punchline,
  lunes for the American 5-3-5 punch form, haibun for prose-with-a-closing-haiku, sedoka
  for two mirroring 5-7-7 stanzas, katauta for the 5-7-7 half-poem addressed to its
  subject, and gogyohka for free-form five-liners. For the newer family extremes, use:
  monoku for the one-line form, sijo for a 3-line twist ending, choka for long alternating
  verse, dodoitsu for the 4-line folk form, and renga for a linked chain of stanzas.
---

# Haiku Skill

Write code as a haiku, three lines, each doing real work, the whole thing runs. No boilerplate. No filler. No placeholders. A complete moment of computation, captured in three dense lines.

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

## Core Patterns

### Complete-Program Haiku
The whole task in three lines, import, transform, output. Run it and it's done.

```python
import sys
fizz = lambda i: "Fizz"*(i%3<1)+"Buzz"*(i%5<1) or i
sys.stdout.write("\n".join(map(str, map(fizz, range(1, 101)))))
```

### Function Haiku
A dense function/expression you can drop into existing code, the task as a unit.

```python
factors = lambda n, p=2: [p] + factors(n//p, p) if n % p == 0 else factors(n, p+1) if n > 1 else []
print(factors(int(input())))
```

### The Kigo Line
One name carries the moment, like a seasonal word in a poem. The middle line does the heavy lifting and the name says what season this is.

```python
from collections import Counter
import re, sys
print(Counter(re.findall(r"[a-z']+", sys.stdin.read().lower())).most_common(5))
```

### Zero-Ceremony Server
Even a server fits in three lines when you stop treating boilerplate as sacred.

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
H = type("H", (BaseHTTPRequestHandler,), {"do_GET": lambda s: (s.send_response(200), s.end_headers(), s.wfile.write(b"haiku"))})
HTTPServer(("", 8000), H).serve_forever()
```

## Boundaries, when NOT to use this skill (use a different skill instead)

This skill is **not for** every brevity request. When the user asks for one of the following, **instead use** the listed skill, the goal is that two skills never coin-flip on the same prompt:

- shortest-possible / golfed code where size is the trophy -> esoteric-programming
- minimal architecture across a whole codebase (services, functions, modules) -> minimalist-zen
- production scaffolding, verification, enterprise review -> no-bullshit
- poetic comments or ink/brush art -> zen-calligraphy
- 5-line expanded forms (result plus reflection) -> tanka
- human-nature humor, 3 lines with a punchline -> senryu
- the American 5-3-5 form (razor-thin middle) -> lunes
- prose-with-haiku (narrative body + poetic ending) -> haibun
- two-stanza mirror forms -> sedoka
- the 5-7-7 half-poem, addressed to its subject -> katauta
- free-form five-liners (no meter) -> gogyohka

Haiku is the middle ground: dense enough to feel like a poem, structured enough to always run.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following so a reviewer can check them without judgment calls:

- at most 3 lines of code that carry logic (language-mandated ceremony like `fn main()` / braces is free)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`, no fake output
- the haiku actually runs and produces the correct result for the task
- every line is a real statement or expression, semicolons, lambdas, chained calls, and comprehensions are the medium
- the middle line (the turn) does the heaviest lifting whenever the task has a natural setup/turn/landing shape
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the three visible logic-line token counts against `[5, 7, 5]` with ±2 tolerance; this is a diagnostic, never a reason to pad or add dead code.

These requirements exist because a theme without a spec produces vibes, not output. A haiku that doesn't run is just a broken poem, the run is the whole point.

## When to Use Haiku Patterns

Use haiku code when:
- the whole task fits in a moment, parse, transform, print
- the user wants a dense one-shot script with zero boilerplate
- you need a drop-in 3-line function, not a module
- the user says "no boilerplate bullshit" or "just make it work"
- a single focused operation deserves a single dense expression

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
const sum = (a, b) => a + b;          // setup: the add
const total = [1, 2, 3, 4].reduce(sum, 0);  // turn: the fold
console.log(total);                    // landing: the number
```

```rust
fn main() {                            // ceremony, free
    let fib = |n: u64| (0..n).fold((0, 1), |(a, b), _| (b, a + b)).0;  // turn
    println!("{}", fib(10));           // landing
}
```

```go
package main
import "fmt"
func main() {
    total := 0                                       // setup: the empty ledger
    for _, n := range []int{3, 1, 4, 1, 5} { total += n }  // turn: the tally
    fmt.Println(total)                               // landing: the answer
}
```

```bash
#!/bin/bash
nums=(3 1 4 1 5)                                # setup: the flock
for n in "${nums[@]}"; do ((total += n)); done  # turn: the tally
printf '%s\n' "$total"                          # landing: 14
```

For other languages (C...), translate the same structure, imports/setup, the dense turn, the landing output.

## Bundled Helpers

If the task needs ASCII output, randomness, or decorative headers, reuse the shared toolkit instead of importing it line-by-line:

- `shared/ascii_canvas.py`, ASCII canvas with lines, circles, ink-density characters
- `shared/rng.py`, seeded RNG and value noise
- `shared/box_drawing.py`, box-drawing headers

A haiku may import one of these on its setup line, that still counts as one of the three.
