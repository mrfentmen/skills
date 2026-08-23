---
name: monoku
description: >-
  Write a complete runnable monoku: the entire program body on one physical line, with a single continuous transformation and no line breaks in the logic. Activate only for an explicit monoku, one-line program, or single-line code request.
---
# Monoku Skill

A monoku is a haiku compressed to a single line, one breath, one image, one line. A code monoku is the whole task on one line: import, transform, output, and it runs. If it doesn't run, it's a broken line.

## Philosophy

"A haiku captures a moment in three lines. A monoku captures it in one. A code monoku captures an entire task in one line that runs."

The monoku mindset:
1. **One physical line**: the complete program body, including any inline import and final output, lives on exactly one nonblank physical line. Do not put a standalone import or setup line above it.
2. **One breath**: ~17 tokens is the natural budget, the code analog of a monoku's ~17 syllables. Rhythm, not law: ±4 slack, and never pad.
3. **Actually runs**: a one-line program that doesn't execute is just a string of symbols.
4. **The kigo**: one name on the line that names the moment, the seasonal word of the program.
5. **Semicolons are breath marks**: `;` chains, lambdas, comprehensions, and `__import__` are the medium.

## The One-Line Constraint

Everything a normal program spreads across lines happens ON the single line:

- **Imports** join the line: use `import sys;` or `__import__("json")` inline on the same physical line as the transformation and output; a separate import line is not allowed
- **Statements** join with `;`, the semicolon is the breath between beats
- **The main logic** is one dense expression: comprehension, lambda, chain, or walrus
- **Output** ends the line: `print(...)`, `sys.stdout.write(...)`, `console.log(...)`

The line must be a COMPLETE program: given input (or none), it produces the correct result. A function that just defines something is allowed when the task is "write the function", but a complete-program monoku ends in output.

## Core Patterns

### Complete-Program Monoku
The whole task, input, transform, output, on one line.

```python
import sys
print("sum", sum(map(int, sys.stdin.read().split())))
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

## Workflow

1. **Write it plainly.** Implement the task the ordinary way and run it until the output is right. No form pressure yet.
2. **Shape the rhythm.** Rewrite in the monoku form: the line count and token profile in Minimum Requirements are the target; choose short names and tight expressions so each line lands near its count, never pad.
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

- exactly 1 nonblank physical line containing the complete program body, including input, transformation, and output; a shebang or language wrapper may be required by another language, but Python imports/setup must remain on that same line
- no placeholders: no `...`, no `# TODO`, no `YOUR CODE HERE`
- the line actually runs and produces the correct result for the task
- roughly one breath: ~17 tokens (natural budget, ±4 slack, never padded)
- the line reads as one continuous expression of intent, semicolons and chains are the medium
- no mock, fake, or pseudo code: every line is real, runs, and does the actual work

Benchmark signature: report the single visible logic-line token count against `[17]` with ±4 tolerance; the diagnostic must never reward unreadable compression or broken one-liners.

## Boundaries

This skill is not for merely concise code, a one-line explanation, or code that needs line breaks to remain correct. Without an explicit monoku request or the one-physical-line contract, handle the request normally.

## Activation

Activate this skill only when the user explicitly names monoku or requests the entire program on one physical line. Generic coding requests, generic brevity, generic production work, and generic artistic requests do not activate it without this explicit identity or structural signature.

## The Monoku Aesthetic

Write code that:
- is one nonblank physical line, including imports, setup, computation, and output
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
func main() {
    m := map[int]string{}; for i := 1; i <= 100; i++ { s := ""; if i%3 == 0 { s += "Fizz" }; if i%5 == 0 { s += "Buzz" }; if s == "" { s = fmt.Sprint(i) }; m[i] = s }; fmt.Println(m)
}
```

For other languages, translate the same structure: everything on one line, the program runs.

## Bundled Helpers

This skill has no external helper-file dependency. Keep implementations self-contained; an existing repository utility is optional, must be verified first, and must never be assumed or loaded from this skill.

Bundled checker: `scripts/rhythm_check.py solve.py` ships with this skill. Run it after writing; it prints the token profile and fails any line outside the form's tolerance. Refine until it passes, then report the profile with the solution.
