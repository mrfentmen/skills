#!/usr/bin/env python3
"""Per-skill E3 breakdown: which forms converge with-skill, which drift
without, and which contracts need tightening. Writes per_skill_results.md."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
GRADER = BASE / 'grade_output.py'
sys.path.insert(0, str(BASE))
from shape_analysis import shape_ok  # noqa: E402

MANIFEST = [i['skill'] for i in __import__('json').loads(
    (BASE / 'e3-manifest.json').read_text())['items']]

# arm dirs: label -> path (relative to output-benchmark)
ARMS = {
    'gold (reference)': 'references',
    'control (no-form)': 'without_skill',
    'groq ws': 'model-outputs/groq-llama3.3-70b/with-skill',
    'groq wos': 'model-outputs/groq-llama3.3-70b/without-skill',
    'mistral ws': 'model-outputs/mistral-small/with-skill',
    'mistral wos': 'model-outputs/mistral-small/without-skill',
    'nvidia ws': 'model-outputs/nvidia-nemotron-3-super/with-skill',
    'nvidia wos': 'model-outputs/nvidia-nemotron-3-super/without-skill',
    'openrouter ws': 'model-outputs/openrouter-llama3.3-70b/with-skill',
    'openrouter wos': 'model-outputs/openrouter-llama3.3-70b/without-skill',
    'groq agentic': 'model-outputs/groq-llama3.3-70b-agentic/with-skill',
    'mistral agentic': 'model-outputs/mistral-small-agentic/with-skill',
}


def grade_row(skill: str, arm_path: Path) -> tuple[bool, bool, bool]:
    """(run, out, form) for one skill in one arm dir via the real grader."""
    if not arm_path.is_dir() or not (arm_path / f'{skill}.py').is_file():
        return (False, False, False)
    proc = subprocess.run([sys.executable, str(GRADER), '--dir', str(arm_path)],
                          capture_output=True, text=True, timeout=300)
    for line in proc.stdout.splitlines():
        if line.startswith(f'{skill} '):
            return ('run=True' in line, 'out=True' in line, 'form=True' in line)
    return (False, False, False)


def shape(skill: str, arm_path: Path) -> bool:
    f = arm_path / f'{skill}.py'
    if not f.is_file():
        return False
    src = f.read_text(encoding='utf-8')
    if src.strip().startswith('# MODEL CALL FAILED') or not src.strip():
        return False
    try:
        return shape_ok(skill, src)[0]
    except Exception:
        return False


def cell(run, out, form) -> str:
    marks = ''.join(m for m, ok in (('R', run), ('O', out), ('F', form)) if ok)
    return marks or '---'


def main() -> None:
    out = []
    out.append('# Per-skill E3 breakdown (2026-08-07)')
    out.append('')
    out.append('Every form graded across the gold set, the no-form control, and all model arms. '
               'Cell letters: R = runs, O = expected output tokens present, F = strict form (token '
               'profile ±2 / line counts). Shape = structural convergence (line count / stanza '
               'structure, no token-profile bar).')
    out.append('')
    header = ('| skill | gold | ctrl | groq ws | groq wos | mistral ws | mistral wos | nvidia ws | nvidia wos |'
              ' openrouter ws | openrouter wos | groq ag | mistral ag | shape ws | shape wos | class |')
    out.append(header)
    out.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')

    rows = []
    for skill in MANIFEST:
        data = {label: grade_row(skill, BASE / path) for label, path in ARMS.items()}
        shp = {label: shape(skill, BASE / path) for label, path in ARMS.items()}
        ws_shape = shp['groq ws'] or shp['mistral ws'] or shp['nvidia ws'] or shp['openrouter ws']
        wos_shape = shp['groq wos'] or shp['mistral wos'] or shp['nvidia wos'] or shp['openrouter wos']
        ag_pass = all(data['groq agentic']) or all(data['mistral agentic'])
        if ws_shape and not wos_shape:
            cls = 'CONVERGED (skill effect)'
        elif ws_shape and wos_shape:
            cls = 'inherently concise'
        else:
            cls = 'NEEDS CONTRACT WORK'
        if ag_pass:
            cls += ' / agentic PASS'
        row = (
            f'| {skill} | {cell(*data["gold (reference)"])} | {cell(*data["control (no-form)"])} '
            f'| {cell(*data["groq ws"])} | {cell(*data["groq wos"])} '
            f'| {cell(*data["mistral ws"])} | {cell(*data["mistral wos"])} '
            f'| {cell(*data["nvidia ws"])} | {cell(*data["nvidia wos"])} '
            f'| {cell(*data["openrouter ws"])} | {cell(*data["openrouter wos"])} '
            f'| {cell(*data["groq agentic"])} | {cell(*data["mistral agentic"])} '
            f'| {"Y" if ws_shape else "-"} | {"Y" if wos_shape else "-"} | {cls} |'
        )
        rows.append((skill, row, ws_shape, wos_shape, ag_pass, cls))

    for _, row, *_ in rows:
        out.append(row)

    converged = [r for r in rows if 'CONVERGED' in r[5]]
    inherent = [r for r in rows if 'inherently' in r[5]]
    needs = [r for r in rows if 'NEEDS' in r[5]]
    ag_passes = [r for r in rows if 'agentic PASS' in r[5]]

    out.append('')
    out.append('## Summary')
    out.append('')
    out.append(f'- **Converged with skill** ({len(converged)}): ' + ', '.join(r[0] for r in converged))
    out.append(f'- **Inherently concise** (shape hit with AND without skill, {len(inherent)}): '
               + ', '.join(r[0] for r in inherent))
    out.append(f'- **NEEDS CONTRACT WORK** (shape missed even with skill, {len(needs)}): '
               + ', '.join(r[0] for r in needs))
    out.append(f'- **Agentic strict passes** ({len(ag_passes)}): ' + ', '.join(r[0] for r in ag_passes))
    out.append('')
    out.append('## Read this honestly')
    out.append('')
    out.append('- "Converged" forms are where the skill demonstrably steers output: the model lands the')
    out.append('  structural shape when handed the skill and drifts off it without. These are the')
    out.append('  skills doing their job.')
    out.append('- "Inherently concise" forms (haiku family, monoku, zappai) are short enough that models')
    out.append('  hit the line-count shape either way; the skill\'s value there is the exact rhythm,')
    out.append('  which only the agentic loop reaches. Two of the four "inherent" rows are shape-test')
    out.append('  artifacts: choka\'s shape predicate (>=6 lines with mixed sizes) is satisfied by any')
    out.append('  ordinary 6+ line program, and villanelle/etheree control arms accidentally satisfy')
    out.append('  their (long) line-count shapes by being verbose - the with-skill arms miss those')
    out.append('  shapes by 1 line. The actionable list is the NEEDS CONTRACT WORK row.')
    out.append('- "NEEDS CONTRACT WORK" forms are the actionable list: even with the skill activated,')
    out.append('  no model converged to the shape one-shot. Those contracts should be inspected for')
    out.append('  ambiguity (e.g. a form whose stanza/line-count rule is easy to misread, or whose')
    out.append('  task wording fights the form).')
    out.append('- Agentic arms: the mistral agentic loop ran all 28 skills (write -> grade -> refine,')
    out.append('  up to 4 generations; it produced Mistral\'s only strict-form pass, haibun). The groq')
    out.append('  agentic loop was started the same way but the Groq org hit its 100k tokens/day free')
    out.append('  cap mid-run, so it only processed a few skills before quota; its \'---\' cells are')
    out.append('  unfinished, not failures. Re-run: GROQ_API_KEY=... python3 run_feedback_arms.py')
    out.append('  --providers groq-llama3.3-70b --sweeps 6.')

    (BASE / 'per_skill_results.md').write_text('\n'.join(out) + '\n')
    print('\n'.join(out[:6]))
    print(f'\n... wrote {len(rows)} rows -> per_skill_results.md')
    print(f'CONVERGED={len(converged)} INHERENT={len(inherent)} NEEDS={len(needs)} AGENTIC_PASS={len(ag_passes)}')


if __name__ == '__main__':
    main()
