# Unconventional Coding Skills

Twenty-eight themed coding skills that change *how* an AI writes code, each one a
philosophy, a set of reusable patterns, and a checkable spec.

## The Skills

The current release contains exactly 28 independently installable skills — 13
short-form poetry skills plus 15 added classical, Asian-adjacent, and Western
forms:

| Skill | Identity | Standalone activation |
|---|---|---|
| `choka` | Long alternating verse with a closing couplet | explicit choka or long-metered-verse request |
| `dodoitsu` | Four-line 7-7-7-5 folk form | explicit dodoitsu or 7-7-7-5 request |
| `gogyohka` | Free-form five-line code | explicit gogyohka or free-form five-line request |
| `haibun` | Narrative code with a three-line poetic landing | explicit haibun or narrated prose-and-verse request |
| `haiku` | Compact three-line 5-7-5 code | explicit code-haiku or 5-7-5 request |
| `katauta` | Directly addressed three-line 5-7-7 fragment | explicit katauta or 5-7-7 fragment request |
| `lunes` | Three-line 5-3-5 form with a short middle | explicit lune or 5-3-5 request |
| `monoku` | Complete program on one physical line | explicit monoku or one-line-program request |
| `renga` | Linked stanzas with visible handoff pivots | explicit renga or chained-stanza request |
| `sedoka` | Two mirrored 5-7-7 stanzas | explicit sedoka or two-stanza-response request |
| `senryu` | Human-nature humor in three 5-7-5 lines | explicit senryu or human-comedy request |
| `sijo` | Three long lines ending in a twist | explicit sijo or three-line-twist request |
| `tanka` | Five-line 5-7-5-7-7 result and reflection | explicit tanka or 5-7-5-7-7 request |
| `kyoka` | Comic tanka: five lines 5-7-5-7-7 ending in a joke | explicit kyoka or comic-verse request |
| `somonka` | Paired exchange of two 5-7-5-7-7 verses | explicit somonka or paired-exchange request |
| `bussokusekika` | Six-line 5-7-5-7-7-7 verse with a sealing verdict | explicit bussokusekika or 5-7-5-7-7-7 request |
| `imayo` | Four lines with a rolling 7-5 pulse per line | explicit imayo or 7-5-7-5 song request |
| `kanshi` | Four lines of paired 7-7 couplets with a turn and resolve | explicit kanshi or couplet-verse request |
| `zappai` | Three-line moment freed from haiku's kigo rules | explicit zappai or free three-line moment request |
| `waka` | Classical five-line 5-7-5-7-7 scene, turn, and resolve | explicit waka or classical verse request |
| `renshi` | Chain of linked short stages passing a torch | explicit renshi or linked-relay request |
| `sonnet` | Fourteen lines in quatrains with a volta and couplet | explicit sonnet or 14-line verse request |
| `villanelle` | Nineteen lines in tercets with two repeating refrains | explicit villanelle or 19-line refrain request |
| `cinquain` | Five lines shaped 2-4-6-8-2, a pyramid with a two-token landing | explicit cinquain or 2-4-6-8-2 request |
| `ryuka` | Four-line Okinawan 8-8-8-6 song with a short landing | explicit ryuka or 8-8-8-6 request |
| `fibonacci` | Lines growing 1-1-2-3-5-8, each the sum of the previous two | explicit fibonacci poem or golden-ratio request |
| `limerick` | Five lines ~8-8-5-5-8 in AABBA rhythm with a comic punchline | explicit limerick or AABBA request |
| `etheree` | Ten lines climbing 1-2-3-4-5-6-7-8-9-10 to the result | explicit etheree or ten-line ladder request |

Every skill is self-contained and carries its own activation contract, minimum
requirements, cross-language examples, and helper policy. Installing one skill
does not require downloading or loading any other skill or repository file.

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
skill({ name: "haiku" })
// ... any of the 18 current skills
```

`COMPREHENSIVE_DOCUMENTATION.md` is a historical four-skill reference; use each current `SKILL.md` as the source of truth for activation and examples.

## Evaluation

- `static_skill_audit.py`, objective SKILL.md quality audit
  (frontmatter, scope, requirements, language coverage, helper policy, and no-mock-code integrity).
  The latest local validation score is **0.79 overall** (all 18 skills above the
  0.75 release floor); earlier **0.80** and **1.00** results are generated
  historical snapshots.
- The external `evals-infra/` repository contains the with-skill vs. baseline
  harness (scaffold → grade → aggregate → viewer). Installed skills do not
  require the harness at runtime. See its `HOW_TO_RUN_EVALS.md` when validating
  a source checkout.

> ⚠️ The historical 180-query trigger set and its recorded decisions predate
> the standalone activation rewrite. They remain reproducible regression data,
> not independent evidence that the revised descriptions generalize. The
> external harness is the source of truth for future independently authored
> routing evaluations.

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

The `evals-infra/` harness lives in its own repository so the standalone skill
repos stay lean. `GITHUB_TOKEN=<pat> bash push_infra_repo.sh` creates or updates
that infrastructure repository. Generated reports, caches, workspaces, and
build artifacts remain outside the standalone skill payloads.

## Safety

Unconventional ≠ broken. All skills must still produce working code, contain
no malware or exploit material, and keep theatrics in the style layer.

## License

Provided as-is for educational and creative purposes. Use responsibly.
