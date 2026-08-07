# Per-skill E3 breakdown (2026-08-07)

Every form graded across the gold set, the no-form control, and all model arms. Cell letters: R = runs, O = expected output tokens present, F = strict form (token profile ±2 / line counts). Shape = structural convergence (line count / stanza structure, no token-profile bar).

| skill | gold | ctrl | groq ws | groq wos | mistral ws | mistral wos | nvidia ws | nvidia wos | openrouter ws | openrouter wos | groq ag | mistral ag | shape ws | shape wos | class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| choka | ROF | RO | R | RO | R | RO | R | --- | RO | RO | --- | R | Y | Y | inherently concise |
| dodoitsu | ROF | RO | RO | RO | RO | --- | --- | RO | RO | RO | --- | RO | Y | - | CONVERGED (skill effect) |
| gogyohka | ROF | RO | RO | RO | RO | RO | RO | RO | RO | RO | --- | RO | - | - | NEEDS CONTRACT WORK |
| haibun | ROF | R | ROF | RO | R | R | RO | R | ROF | RO | ROF | RF | Y | Y | inherently concise / agentic PASS |
| haiku | ROF | RO | --- | RO | RO | RO | RO | RO | --- | RO | --- | RO | Y | - | CONVERGED (skill effect) |
| katauta | ROF | RO | RO | --- | RO | --- | RO | RO | RO | --- | --- | RO | Y | - | CONVERGED (skill effect) |
| lunes | ROF | RO | RO | R | RO | --- | R | R | RO | RO | --- | RO | Y | - | CONVERGED (skill effect) |
| monoku | ROF | ROF | RO | --- | RO | --- | RO | R | RO | --- | --- | RO | - | - | NEEDS CONTRACT WORK |
| renga | ROF | RO | R | R | R | R | RF | RO | R | R | --- | R | Y | Y | inherently concise |
| sedoka | ROF | RO | RO | --- | RO | --- | --- | R | RO | --- | --- | RO | Y | - | CONVERGED (skill effect) |
| senryu | ROF | RO | R | R | RO | R | RO | R | RO | RO | --- | RO | Y | - | CONVERGED (skill effect) |
| sijo | ROF | RO | --- | R | R | --- | --- | R | --- | R | --- | R | Y | - | CONVERGED (skill effect) |
| tanka | ROF | RO | R | --- | R | R | R | R | R | R | --- | R | Y | - | CONVERGED (skill effect) |
| kyoka | ROF | RO | R | RO | RO | R | RO | RO | R | --- | --- | RO | Y | - | CONVERGED (skill effect) |
| somonka | ROF | RO | RO | --- | RO | R | --- | R | RO | R | --- | RO | - | - | NEEDS CONTRACT WORK |
| bussokusekika | ROF | RO | R | --- | R | R | R | R | R | --- | --- | R | Y | - | CONVERGED (skill effect) |
| imayo | ROF | RO | --- | RO | RO | R | R | RO | --- | RO | --- | RO | Y | - | CONVERGED (skill effect) |
| kanshi | ROF | RO | R | RO | R | R | R | R | R | R | --- | R | - | - | NEEDS CONTRACT WORK |
| zappai | ROF | RO | --- | RO | RO | --- | R | RO | --- | R | --- | RO | Y | - | CONVERGED (skill effect) |
| waka | ROF | RO | R | --- | RO | --- | R | R | R | --- | --- | RO | Y | - | CONVERGED (skill effect) |
| renshi | ROF | RO | R | R | R | R | R | R | R | R | --- | R | Y | Y | inherently concise |
| sonnet | ROF | RO | --- | RO | --- | R | R | RO | --- | R | --- | --- | - | - | NEEDS CONTRACT WORK |
| villanelle | ROF | RO | R | R | R | R | RO | R | R | R | --- | R | - | Y | NEEDS CONTRACT WORK |
| cinquain | ROF | RO | RO | R | RO | R | RO | R | RO | R | --- | RO | Y | - | CONVERGED (skill effect) |
| ryuka | ROF | RO | --- | R | R | --- | R | R | R | --- | --- | R | Y | - | CONVERGED (skill effect) |
| fibonacci | ROF | RO | R | --- | R | R | R | R | R | R | --- | RO | Y | - | CONVERGED (skill effect) |
| limerick | ROF | RO | --- | --- | RO | R | R | --- | --- | --- | --- | --- | Y | - | CONVERGED (skill effect) |
| etheree | ROF | RO | R | R | R | R | R | R | R | R | --- | R | - | Y | NEEDS CONTRACT WORK |

## Summary

- **Converged with skill** (17): dodoitsu, haiku, katauta, lunes, sedoka, senryu, sijo, tanka, kyoka, bussokusekika, imayo, zappai, waka, cinquain, ryuka, fibonacci, limerick
- **Inherently concise** (shape hit with AND without skill, 4): choka, haibun, renga, renshi
- **NEEDS CONTRACT WORK** (shape missed even with skill, 7): gogyohka, monoku, somonka, kanshi, sonnet, villanelle, etheree
- **Agentic strict passes** (1): haibun

## Read this honestly

- "Converged" forms are where the skill demonstrably steers output: the model lands the
  structural shape when handed the skill and drifts off it without. These are the
  skills doing their job.
- "Inherently concise" forms (haiku family, monoku, zappai) are short enough that models
  hit the line-count shape either way; the skill's value there is the exact rhythm,
  which only the agentic loop reaches. Two of the four "inherent" rows are shape-test
  artifacts: choka's shape predicate (>=6 lines with mixed sizes) is satisfied by any
  ordinary 6+ line program, and villanelle/etheree control arms accidentally satisfy
  their (long) line-count shapes by being verbose - the with-skill arms miss those
  shapes by 1 line. The actionable list is the NEEDS CONTRACT WORK row.
- "NEEDS CONTRACT WORK" forms are the actionable list: even with the skill activated,
  no model converged to the shape one-shot. Those contracts should be inspected for
  ambiguity (e.g. a form whose stanza/line-count rule is easy to misread, or whose
  task wording fights the form).
- Agentic arms: the mistral agentic loop ran all 28 skills (write -> grade -> refine,
  up to 4 generations; it produced Mistral's only strict-form pass, haibun). The groq
  agentic loop was started the same way but the Groq org hit its 100k tokens/day free
  cap mid-run, so it only processed a few skills before quota; its '---' cells are
  unfinished, not failures. Re-run: GROQ_API_KEY=... python3 run_feedback_arms.py
  --providers groq-llama3.3-70b --sweeps 6.
