---
name: monoku
description: >-
  Write code as a monoku: the ENTIRE working program on a single line - the one-line
  haiku, a whole task in one breath of code that runs. Use this skill when the user wants
  an ultra-dense single-line solution, a one-shot script squeezed onto one line, a
  complete program in one expression, or the extreme of the haiku family. Make sure to use
  this skill whenever the user mentions monoku, one-line haiku, single-line programs, or
  asks to write the whole thing on one line. This skill is NOT for 3-line forms (use
  haiku, senryu, lunes, or katauta), NOT for code golf or shortest-possible trophy code
  (use esoteric-programming), NOT for minimal architecture across a codebase (use
  minimalist-zen), and NOT for 5-line forms (use tanka or gogyohka). For the rest of the
  poetic family, use: sijo for a 3-line Korean twist form, choka for a long alternating
  verse, dodoitsu for the 4-line folk form, and renga for a linked chain of stanzas.
---
# Monoku Skill

A monoku is a haiku compressed to a single line, one breath, one image, one line. A code monoku is the whole task on one line: import, transform, output, and it runs. If it doesn't run, it's a broken line.

## Philosophy

"A haiku captures a moment in three lines. A monoku captures it in one. A code monoku captures an entire task in one line that runs."

The monoku mindset:
1. **One line**: the complete program lives on a single line of code. No exceptions, no ceremony.
2. **One breath**: ~17 tokens is the natural budget, the code analog of a monoku's ~17 syllables. Rhythm, not law: ±4 slack, and never pad.
3. **Actually runs**: a one-line program that doesn't execute is just a string of symbols.
4. **The kigo**: one name on the line that names the moment, the seasonal word of the program.
5. **Semicolons are breath marks**: `;` chains, lambdas, comprehensions, and `__import__` are the medium.

## The One-Line Constraint

Everything a normal program spreads across lines happens ON the single line:

- **Imports** join the line: `import sys;` or `__import__("json")` inline
- **Statements** join with `;`, the semicolon is the breath between beats
- **The main logic** is one dense expression: comprehension, lambda, chain, or walrus
- **Output** ends the line: `print(...)`, `sys.stdout.write(...)`, `console.log(...)`

The line must be a COMPLETE program: given input (or none), it produces the correct result. A function that just defines something is allowed when the task is "write the function", but a complete-program monoku ends in output.

## Core Patterns

### Complete-Program Monoku
The whole task, input, transform, output, on one line.

```python
import sys;print(__import__("collections").Counter(sys.stdin.read().split()).most_common(5))
```

### Monoku FizzBuzz
One line, runs, prints 1..100 with Fizz/Buzz:

```python
import sys;print("\n".join("Fizz"*(i%3<1)+"Buzz"*(i%5<1) or str(i) for i in range(1, 101)))
```

### One-Line Function
When the task is "write a function", the monoku is the definition, dense but readable:

```python
factors=lambda n,p=2:[p]+factors(n//p,p) if n%p==0 else factors(n,p+1) if n>1 else []
```

### The Kigo on the Line
One name carries the moment, the middle of the line is where the transformation breathes:

```python
import sys;print(max(sys.stdin.read().split(), key=len))
```

## Boundaries, when NOT to use this skill

- shortest-possible / golfed trophy code, obfuscation as sport -> esoteric-programming
- 3-line forms (setup/turn/landing) -> haiku
- human-nature humor 3-liners -> senryu
- the American 5-3-5 punch form -> lunes
- the 5-7-7 half-poem addressed to its subject -> katauta
- 5-line expanded forms -> tanka (strict) or gogyohka (free)
- 4-line folk form with a short landing -> dodoitsu
- long alternating verse -> choka
- linked chains of stanzas -> renga
- minimal architecture across a codebase -> minimalist-zen
- production scaffolding or verification -> no-bullshit

Monoku is the one-line extreme: denser than haiku, but it must still read as a breath, not a scramble.

## Minimum Requirements (checkable)

Every deliverable produced with this skill must be gradeable. You must include ALL of the following:

- exactly 1 line of code that carries logic (language-mandated ceremony like a shell shebang line or `package main` is free, but the program body is one line)
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`
- the line actually runs and produces the correct result for the task
- roughly one breath: ~17 tokens (natural budget, ±4 slack, never padded)
- the line reads as one continuous expression of intent, semicolons and chains are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the single visible logic-line token count against `[17]` with ±4 tolerance; the diagnostic must never reward unreadable compression or broken one-liners.

## When to Use Monoku Patterns

Use monoku code when:
- the whole task collapses to a single transformation, read, transform, print
- the user wants the haiku extreme: "can you do it in one line?"
- you need a drop-in single-expression function
- the user says "no boilerplate bullshit" and means it absolutely

## The Monoku Aesthetic

Write code that:
- is one line, the entire program
- reads like a single breath: nothing wasted, nothing missing
- uses a kigo, one name that captures the moment
- prefers the densest honest expression (walrus, comprehension, `__import__`, `;`)
- still RUNS, the one-line program that runs is the whole point

## Cross-Language Examples

```javascript
console.log([...Array(100)].map((_, i) => (i % 15 ? (i % 3 ? (i % 5 ? i : "Buzz") : "Fizz") : "FizzBuzz")).join("\n"))
```

```bash
#!/bin/bash
tr ' ' '\n' < file.txt | sort | uniq -c | sort -rn | head -5
```

```go
package main
import "fmt"
func main() { m := map[int]string{}; for i := 1; i <= 100; i++ { s := ""; if i%3 == 0 { s += "Fizz" }; if i%5 == 0 { s += "Buzz" }; if s == "" { s = fmt.Sprint(i) }; m[i] = s }; fmt.Println(m) }
```

For other languages, translate the same structure: everything on one line, the program runs.

## Bundled Helpers

If the task needs ASCII output, randomness, or decorative headers, reuse the shared toolkit, but a monoku may import it inline:

- `shared/ascii_canvas.py`, ASCII canvas with lines, circles, ink-density characters
- `shared/rng.py`, seeded RNG and value noise
- `shared/box_drawing.py`, box-drawing headers
