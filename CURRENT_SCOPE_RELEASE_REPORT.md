# Current-Scope Release Report

**Release scope:** 28 form skills (public monorepo `mrfentmen/skills`)  
**Report date:** 2026-08-08  
**Repository commit:** `d8707e8` - Green gates: revise-until-checker line fixes for 7 low-scoring forms, updated rhythm checkers, current-scope regression gate, current historical suite, workflow + docs

> **Scope note.** The public monorepo is the **28 form skills** listed below.
> The persona skills `god`, `smoker`, `terry-davis`, `psych`, `no-bullshit`,
> and `quantum-computing` moved to the separate public repo
> `mrfentmen/skills-2` and are **not** part of this release.

## Executive summary

The current scope is **fully green on every active gate**. All 28 skills
pass the static audit at 1.00, the 250-query trigger benchmark validates
clean, the current-scope CI is 36/36 (37/37 with the frozen-historical
compatibility assertion configured), the self-contained current historical
suite is 7/7, and the rhythm gate passes 28 documented examples plus 28 E3
gold references through each skill's own checker.

The only remaining red result is the **raw frozen legacy runner**
(`evals-infra/run_ci_checks.sh`), which is intentionally kept red: it is
frozen to the old 18-skill dataset and pre-reorg layout, so it reports
missing entries for the 15 newer forms and relocated personas. That is
historical evidence, preserved deliberately, and is not a current-skill
defect. See `standalone-evals/HISTORICAL_REGRESSION.md`.

## Skill inventory (28 forms)

| Skill | Category | Skill | Category |
|---|---|---|---|
| `choka` | Japanese long form | `katauta` | Japanese form |
| `dodoitsu` | Japanese form | `kyoka` | Japanese comic form |
| `gogyohka` | Japanese form | `limerick` | Western form (English) |
| `haibun` | Japanese prose+verse | `lunes` | Japanese/American form |
| `haiku` | Japanese form | `monoku` | Japanese one-line form |
| `imayo` | Japanese form | `renga` | Japanese linked verse |
| `kanshi` | Japanese Chinese-style | `renshi` | Japanese linked form |
| `bussokusekika` | Japanese form | `ryuka` | Ryukyuan form |
| `cinquain` | Western form (English) | `sedoka` | Japanese form |
| `etheree` | Western form (English) | `senryu` | Japanese comic form |
| `fibonacci` | Western form (English) | `sijo` | Korean form |
| `somonka` | Japanese exchange form | `sonnet` | Western form (English) |
| `tanka` | Japanese form | `villanelle` | Western form (English) |
| `waka` | Japanese form | `zappai` | Japanese form |

Every skill ships a `SKILL.md` with a form contract, a token-counting
procedure, a check-and-refine `## Workflow` section, and a bundled
`scripts/rhythm_check.py` checker.

## Trigger routing benchmark

**Dataset:** `standalone-evals/standalone_trigger_benchmark_v1.json` — 250
versioned current-scope records:

| Slice | Count | Meaning |
|---|---:|---|
| Explicit / signature | 140 | 28 skills × 5 records, explicit identity or unmistakable contract |
| Boundary | 56 | 28 skills × 2 close-boundary records, no literal skill names |
| Ordinary (`none`) | 36 | Global non-skill prompts |
| Trap | 18 | Global sibling/persona traps |

**Validation:** `validate_standalone_benchmark.py` — PASS. Schema, coverage,
duplicates, anti-leak rules, and local-target existence all check clean.
Boundary/ordinary/trap records contain no literal skill-name tokens.

**Blind routing evidence:** the frozen 54-record held-out set
(`current_scope_heldout_v1.json`, an 18-skill-era artifact) measures fresh
prompts the descriptions were not tuned on. Recorded numbers:

| Scorer | Accuracy | Status |
|---|---:|---|
| Mechanical token-overlap baseline | 34/54 (12/18 paraphrase, 13/18 boundary, 9/9 trap, 0/9 none) | Lower bound (floor) |
| Same-author self-score | 54/54 | Upper bound (consistency, not independence) |
| Independent blind scorer | not yet recorded | The meaningful number when available |

No independent blind-routing score is claimed until a scorer that only saw
the shuffled sheet returns decisions; the scoring tooling
(`make_current_heldout_sheet.py`, `score_blind_decisions.py`) is ready.

## Output-correctness benchmark (E-007 / E3)

**Manifest:** `standalone-evals/output-benchmark/e3-manifest.json` — 28
executable tasks, one per skill, each with stdin input and expected output
tokens. Gold references (28/28) prove every contract is satisfiable.

### Same-author baseline

| Arm | Runs | Output tokens | Form compliance |
|---|---:|---:|---:|
| With skill (gold references) | 28/28 | 28/28 | **28/28** |
| Without skill (plain idiomatic control) | 28/28 | 28/28 | **1/28** (monoku) |

The with-skill result is an upper bound (authored holding the skill spec);
the 28/28 vs 1/28 gap shows the form contracts are real and gradeable.

### Independent model arms (2026-08-07, full 28-item manifest, one-shot)

| Arm | Model | Run | Correct | Strict form | Shape convergence |
|---|---|---|---:|---:|---:|
| With skill | Groq llama-3.3-70b | 21/28 | 9/28 | 1/28 (haibun) | 11/28 |
| With skill | Mistral small | 27/28 | 15/28 | 0/28 | 15/28 |
| With skill | NVIDIA Nemotron-3-Super | 24/28 | 9/28 | 1/28 (renga) | 15/28 |
| With skill | OpenRouter llama-3.3-70b | 22/28 | 11/28 | 1/28 (haibun) | 12/28 |
| Without skill | Groq llama-3.3-70b | 19/28 | 10/28 | 0/28 | 3/28 |
| Without skill | Mistral small | 19/28 | 3/28 | 0/28 | 4/28 |
| Without skill | NVIDIA Nemotron-3-Super | 26/28 | 9/28 | 0/28 | 5/28 |
| Without skill | OpenRouter llama-3.3-70b | 20/28 | 8/28 | 0/28 | 3/28 |

**The measurable with-skill effect:** shape convergence (structural
silhouette) runs at roughly **3-4x the control rate** across four
independent providers (Groq 11 vs 3, Mistral 15 vs 4, NVIDIA 15 vs 5,
OpenRouter 12 vs 3), and Mistral's correct-output rate jumps 5x with the
skill (15 vs 3). Strict ±2-token rhythm is not reliably one-shot-achievable
by current models without iterating; that is what the agentic loop
(write → run `rhythm_check.py` → refine) is for. One-shot strict passes
that did land: haibun (Groq, OpenRouter) and renga (NVIDIA); the
checker-feedback loop added Mistral's first strict-form pass (haibun), a
result one-shot Mistral never reached.

**Per-skill classification** (from `per_skill_results.md`):

- **Converged with skill (17):** dodoitsu, haiku, katauta, lunes, sedoka,
  senryu, sijo, tanka, kyoka, bussokusekika, imayo, zappai, waka, cinquain,
  ryuka, fibonacci, limerick
- **Inherently concise (5):** choka, haibun, monoku, renga, renshi
- **Needs contract work (6):** gogyohka, somonka, kanshi, sonnet,
  villanelle, etheree

The six "needs contract work" forms received the 2026-08-07 contract-
hardening pass (tightened rhythm rules, exact rung/line sequences,
"revise until the checker passes" line-fix instructions, updated
`rhythm_check.py`); the committed model-arm files predate that hardening,
so their shape rows remain pre-hardening evidence and the next model-arm
re-run is the follow-up measurement.

## Release gates (all green)

| Gate | Result |
|---|---:|
| Current-scope CI (`run_current_ci.sh`) | **36/36** (37/37 with `HISTORICAL_HARNESS` configured) |
| Current historical suite (`run_current_historical_ci.sh`) | **7/7 GREEN** |
| Rhythm gate (28 documented examples + 28 E3 references) | **PASS** |
| Trigger benchmark validation (250 records) | **PASS** |
| Static skill audit | **1.00** all 28 skills |
| Python compilation | PASS |
| Shell syntax (`bash -n`) | PASS |
| Whitespace/diff (`git diff --check`) | PASS |
| Repeated stability runs | PASS (3 consecutive full matrix runs) |
| Clean-copy run | PASS |
| Code review | no critical issues |

## Known red: frozen historical runner (by design)

`SKILLS_ROOT="$PWD" bash "/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh"`
still exits 1 with a stable mismatch signature (20 missing metadata
entries + 1 historical gogyohka description drift in current-root mode).
Its dataset predates the 15 newer forms and the relocated persona skills.
The current 28-skill tree satisfies 9/11 isolated historical checks; the
raw host-tree invocation reports 8/11 because it also sees old workspace
variance artifacts. This result is **preserved as historical evidence, not
hidden or rewritten** — the self-contained current historical suite is the
authoritative green gate for the current scope.

## Reproduction commands

```bash
cd /Users/del/Desktop/skills

# Current CI (unconfigured: 36/36)
bash standalone-evals/run_current_ci.sh

# Current CI with frozen-historical compatibility assertion (37/37)
EVALS_INFRA_ROOT="/Users/del/Desktop/skills 3 /evals-infra" \
HISTORICAL_HARNESS="/Users/del/Desktop/skills 3 /evals-infra/run_ci_checks.sh" \
  bash standalone-evals/run_current_ci.sh

# Self-contained current historical suite (7/7)
./standalone-evals/run_current_historical_ci.sh

# Rhythm gate
python3 standalone-evals/check_rhythm_examples.py

# Trigger benchmark + static audit
python3 standalone-evals/validate_standalone_benchmark.py --root .
python3 standalone-evals/static_skill_audit.py --root .

# E3 output benchmark (gold + control + a fresh model arm)
cd standalone-evals/output-benchmark
python3 grade_output.py --dir references
python3 grade_output.py --dir without_skill
GROQ_API_KEY=... python3 run_model_arms.py --providers groq-llama3.3-70b
python3 grade_output.py --dir model-outputs/groq-llama3.3-70b/with-skill

# Blind held-out routing (independent scorer protocol)
python3 standalone-evals/make_current_heldout_sheet.py --output /tmp/heldout-blind.md
python3 standalone-evals/score_blind_decisions.py --decisions /path/to/decisions.json
```

## Release conclusion

**Status: release-ready on all active current-scope gates.**

What is proven: the 28 form contracts are satisfiable and gradeable
(28/28 gold references), the skills steer output shape at ~3-4x the control
rate across four independent model providers, routing datasets are
structurally valid and leak-free, and every deterministic gate is green.

What is honestly not proven: independent blind-routing accuracy on fresh
prompts (no external scorer has returned decisions yet), and exact ±2-token
rhythm one-shot (reachable only via the agentic checker loop). The frozen
legacy runner stays red as documented historical evidence.
