# Unconventional Coding Skills

Eighteen themed coding skills that change *how* an AI writes code, each one a
philosophy, a set of reusable patterns, and a checkable spec.

## The Skills

| Skill | Theme | NOT for (use instead) |
|---|---|---|
| `terry-davis` | HolyC / TempleOS, cosmic variable names, goto spaghetti | production code → `no-bullshit`; surreal → `psych` |
| `psych` | psychedelic, fractal, emergent algorithms | genetic algos → `biomimicry`; quantum → `quantum-computing`; esolangs → `esoteric-programming` |
| `no-bullshit` | production-minded, zero hallucination, honest verification | themed code → the matching theme skill; golf → `esoteric-programming` |
| `smoker` | battle-tested senior-engineer voice, inspect-first | themed code → theme skill; diplomatic → `no-bullshit` |
| `retro-computing` | 8-bit / DOS / C64, direct memory, chiptune | CRT glitches → `glitch-art`; generative art → `artistic-creative` |
| `mathematical-elegance` | proofs, invariants, pure function beauty | quantum → `quantum-computing`; golden ratio → `renaissance` |
| `minimalist-zen` | fewest honest lines, no gold-plating | ink art → `zen-calligraphy`; golf → `esoteric-programming` |
| `artistic-creative` | generative art, particles, procedural beauty | glitch → `glitch-art`; math proofs → `mathematical-elegance` |
| `quantum-computing` | qubits, superposition, entanglement | psychedelic → `psych` |
| `esoteric-programming` | Brainfuck, Befunge, golf, quines | security obfuscation → security review; readable code → `no-bullshit` |
| `biomimicry` | evolution, swarms, neural nets, ecosystems | psychedelic → `psych` |
| `glitch-art` | pixel sorting, data bending, CRT artifacts | intentional pixel art → `retro-computing` |
| `steampunk` | gears, brass, Babbage, Victorian computing | 8-bit → `retro-computing`; Victorian horror → `cosmic-horror` |
| `cosmic-horror` | sanity systems, non-Euclidean dread | game AI w/o horror → no theme; generative art → `artistic-creative` |
| `renaissance` | golden ratio, perspective, classical proportion | pure math → `mathematical-elegance` |
| `zen-calligraphy` | brush strokes, ink, haiku comments | minimal code → `minimalist-zen`; mechanics → `steampunk` |
| `haiku` | 3-line dense code that actually runs (5-7-5 token rhythm) | code golf → `esoteric-programming`; minimal architecture → `minimalist-zen` |
| `tanka` | 5-line dense code (5-7-5-7-7): result plus reflection | 3-line forms → `haiku`/`senryu`/`lunes`; golf → `esoteric-programming` |
| `senryu` | 3-line human-nature humor (5-7-5) with a punchline | nature → `haiku`; 5-line → `tanka`; 5-3-5 → `lunes` |
| `lunes` | 3-line American form (5-3-5) with a razor-thin punch middle | 5-7-5 → `haiku`; 5-line → `tanka` |
| `haibun` | narrative prose-like code + 3-line haiku ending (≤12 lines) | pure 3-line forms → `haiku`/`senryu`/`lunes`/`katauta` |
| `sedoka` | 6 lines in two mirroring 5-7-7 stanzas (question/response) | single 3-line stanzas → `katauta`; 5-line → `tanka`/`gogyohka` |
| `katauta` | 3-line 5-7-7 half-poem, addressed to its subject | 5-7-5 → `haiku`/`senryu`; 5-3-5 → `lunes` |
| `gogyohka` | free-form 5-liner, one breath per line, no meter | metered tanka → `tanka`; 3-line forms → `haiku`/`senryu`/`lunes`/`katauta` |

Every skill has:

- **Boundaries**, an explicit "when NOT to use this skill / use X instead"
  section plus a boundary sentence in the description, so overlapping skills
  never coin-flip on the same prompt.
- **Minimum Requirements (checkable)**, objective items a reviewer can grade
  without judgment calls (these power the eval assertions).
- **Cross-Language Examples**, Python + JavaScript + Rust (and C for
  terry-davis), so the theme translates to any stack.
- **Bundled Helpers**, pointers to the shared toolkit below.

## Shared Helpers (`shared/`)

The themed skills kept reinventing the same primitives. They now share:

- `shared/ascii_canvas.py`, ASCII canvas with Bresenham lines, circles,
  rectangles, ink-density characters (█ ▓ ▒ ░)
- `shared/box_drawing.py`, box-drawing headers and sections (╔══╗ ║ ╚══╝)
- `shared/rng.py`, seeded RNG, gaussian/choice, value noise

## Installation

### Packaged `.skill` files

```bash
cd skills
python3 package_skills.py            # writes dist/<name>.skill for all 18
python3 package_skills.py --target .agents/skills   # or install directly
```

### Copy the directories

```bash
cp -r skills/terry-davis ~/.agents/skills/   # repeat for each skill
```

- **Codex**: `.codex/skills/`
- **Gemini CLI**: `.gemini/skills/`
- **Freebuff**: place in `.agents/skills/`

## Loading / Usage

```javascript
skill({ name: "terry-davis" })
skill({ name: "psych" })
skill({ name: "retro-computing" })
// ... any of the 16
```

Example prompts per theme are listed in `COMPREHENSIVE_DOCUMENTATION.md`.

## Evaluation

- `static_skill_audit.py`, objective SKILL.md quality audit
  (frontmatter, boundaries, requirements, language coverage, helpers, and no-mock-code integrity).
  Baseline: **0.39 overall** → after this pass: **1.00 overall** (18/18).
- `evals-infra/`, the real with-skill vs. baseline harness (scaffold →
  grade → aggregate → viewer). See `evals-infra/HOW_TO_RUN_EVALS.md`.

> ⚠️ The older "benchmark" percentages for the 12 newer skills were simulated
> by a local script, not measured with LLM runs. The harness in `evals-infra/`
> is the real thing, run it in an environment with LLM subagents and treat
> its output as the source of truth.

## GitHub Actions CI (per-skill repos)

Each skill can live in its own repository (`mrfentmen/<skill>`). Every push to
any of them runs the **Audit & Package** workflow (`ci/audit-and-package.yml`,
distributed by `push_all_skills.sh` into `.github/workflows/`):

1. **Static audit** (`static_skill_audit.py`), scores SKILL.md on 9
   dimensions. Below `AUDIT_MIN_SCORE` (default **0.75**) the run fails red
   and nothing ships, *bad quality doesn't publish*.
2. **Repackage** (`package_skills.py`), rebuilds `dist/<skill>.skill` from
   the current tree (CI machinery excluded).
3. **Artifacts**, `SKILL_AUDIT.json` + the `.skill` upload on every run,
   even failures, for diagnostics.
4. **Auto-commit**, on the default branch, refreshed artifacts are committed
   back with `[skip actions]` so the loop can't re-trigger.

The audit + packager scripts are layout-aware: they run identically in the
monorepo (`skills/`) and inside a per-skill repo (`SKILL.md` at the root).

> **Deploy:** existing repos were seeded before CI existed, so re-run
> `GITHUB_TOKEN=<pat> bash push_all_skills.sh` once to install the workflow
> + scripts into all 18 skill repos (the "name already exists" message is expected
> and harmless; it still pushes the new `.github/` files).

## The infra repo (`mrfentmen/skills-infra`)

The `shared/` helpers and the `evals-infra/` harness live in their own repo
so the skill repos stay lean. `GITHUB_TOKEN=<pat> bash push_infra_repo.sh`
creates/updates it with: `shared/`, `evals-infra/` (incl. legacy history),
`package_skills.py`, `ci/audit-and-package.yml`, and a README, caches,
`dist/`, workspaces, and generated reports are excluded.

## Safety

Unconventional ≠ broken. All skills must still produce working code, contain
no malware or exploit material, and keep theatrics in the style layer.

## License

Provided as-is for educational and creative purposes. Use responsibly.
