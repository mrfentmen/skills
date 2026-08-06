#!/usr/bin/env python3
"""Register round-3 skills in all infra files."""
import json
import re
from pathlib import Path

ROOT = Path("/Users/del/Desktop/skills")
AUDIT = Path("/Users/del/Desktop/skills 3 /evals-infra/static_skill_audit.py")
NEW = ["villanelle", "cinquain", "ryuka", "fibonacci", "limerick", "etheree"]

old_list = """SKILLS = [
    "choka", "dodoitsu", "gogyohka", "haibun", "haiku",
    "katauta", "lunes", "monoku", "renga",
    "sedoka", "senryu", "sijo", "tanka",
    "kyoka", "somonka", "bussokusekika", "imayo",
    "kanshi", "zappai", "waka", "renshi", "sonnet",
]"""
new_list = """SKILLS = [
    "choka", "dodoitsu", "gogyohka", "haibun", "haiku",
    "katauta", "lunes", "monoku", "renga",
    "sedoka", "senryu", "sijo", "tanka",
    "kyoka", "somonka", "bussokusekika", "imayo",
    "kanshi", "zappai", "waka", "renshi", "sonnet",
    "villanelle", "cinquain", "ryuka", "fibonacci",
    "limerick", "etheree",
]"""

for fname in ["validate_standalone_benchmark.py", "run_example_smoke.py", "check_skill_isolation.py"]:
    p = ROOT / "standalone-evals" / fname
    s = p.read_text()
    if old_list in s:
        p.write_text(s.replace(old_list, new_list))
        print("patched", fname)
    else:
        print("WARN", fname, "list not found")

# CI loop
p = ROOT / "standalone-evals" / "run_current_ci.sh"
s = p.read_text()
old_ci = """for skill in choka dodoitsu gogyohka haibun haiku katauta lunes monoku \\
  renga sedoka senryu sijo tanka kyoka somonka bussokusekika imayo \\
  kanshi zappai waka renshi sonnet"""
new_ci = """for skill in choka dodoitsu gogyohka haibun haiku katauta lunes monoku \\
  renga sedoka senryu sijo tanka kyoka somonka bussokusekika imayo \\
  kanshi zappai waka renshi sonnet villanelle cinquain ryuka fibonacci \\
  limerick etheree"""
if old_ci in s:
    p.write_text(s.replace(old_ci, new_ci))
    print("patched CI loop")
else:
    print("WARN CI loop not found")

# Theme keywords
s = AUDIT.read_text()
old_theme = """    "sonnet": ["sonnet", "quatrain", "couplet", "volta", "fourteen", "turn"],
}"""
new_theme = """    "sonnet": ["sonnet", "quatrain", "couplet", "volta", "fourteen", "turn"],
    "villanelle": ["villanelle", "refrain", "tercet", "nineteen", "repeat"],
    "cinquain": ["cinquain", "pyramid", "2-4-6-8-2", "swell", "landing"],
    "ryuka": ["ryuka", "okinawan", "8-8-8-6", "landing", "song"],
    "fibonacci": ["fibonacci", "golden", "grow", "sequence", "sum of the previous"],
    "limerick": ["limerick", "punchline", "aabba", "comic", "joke"],
    "etheree": ["etheree", "ladder", "1-2-3-4-5-6-7-8-9-10", "climb", "rung"],
}"""
if old_theme in s:
    AUDIT.write_text(s.replace(old_theme, new_theme))
    print("patched theme keywords")
else:
    print("WARN theme block not found")

# Trigger records
BP = ROOT / "standalone-evals" / "standalone_trigger_benchmark_v1.json"
data = json.loads(BP.read_text())

NEW_RECORDS = {
    "villanelle": [
        ("Write a villanelle-shaped program: 19 lines in five tercets and a closing quatrain, with two refrain expressions repeated at lines 1,6,12,18 and 3,9,15,19, computing the total and error count of a log while the log changes between refrains", "explicit_or_signature"),
        ("Build a villanelle program with the two-refrain architecture: a health verdict and an up-count, each returning four times as services go up and down", "explicit_or_signature"),
        ("Write a 19-line verse program where two key expressions recur every few lines and the state between them changes each time", "explicit_or_signature"),
        ("Write a nineteen-line program with repeating refrain expressions and a closing quatrain that resolves the computation", "explicit_or_signature"),
        ("Compose a five-tercet plus quatrain program whose two repeated lines are real expressions over shifting data", "explicit_or_signature"),
        ("Write a repeating-refrain verse program that computes a moving average", "boundary"),
        ("Write a nineteen-line program that formats a report table", "boundary"),
    ],
    "cinquain": [
        ("Write a cinquain program: five lines shaped 2-4-6-8-2 tokens that counts errors in a log and lands on a two-token print of the count", "explicit_or_signature"),
        ("Build a cinquain-shaped program with the pyramid silhouette 2-4-6-8-2 that computes mean and spread", "explicit_or_signature"),
        ("Write a five-line pyramid program that swells to an eight-token line and closes on two tokens", "explicit_or_signature"),
        ("Write a 2-4-6-8-2 shaped program that checks service health and lands the down-count", "explicit_or_signature"),
        ("Compose a five-line poem program with a two-token closing word that seals the result", "explicit_or_signature"),
        ("Write a pyramid-shaped verse program that tallies words in a file", "boundary"),
        ("Write a five-line program that builds a small lookup table", "boundary"),
    ],
    "ryuka": [
        ("Write a ryuka program: four lines shaped 8-8-8-6 tokens, three long lines of checking and a short six-token landing line, reading health booleans", "explicit_or_signature"),
        ("Build a ryuka-shaped program with the 8-8-8-6 Okinawan song shape that computes a mean", "explicit_or_signature"),
        ("Write a four-line verse program whose last line is shorter than the first three and lands the result", "explicit_or_signature"),
        ("Write an 8-8-8-6 shaped program that parses a log and prints the error count on the short line", "explicit_or_signature"),
        ("Compose an Okinawan song program: three long lines of work and one short closing line", "explicit_or_signature"),
        ("Write a song-shaped verse program that reports the number of running services", "boundary"),
        ("Write a four-line program that validates JSON config", "boundary"),
    ],
    "fibonacci": [
        ("Write a fibonacci poem program: lines whose token counts follow 1,1,2,3,5,8, summing a list and sealing the result on the final line", "explicit_or_signature"),
        ("Build a fibonacci-shaped program where each line's token count is the sum of the previous two, checking service health", "explicit_or_signature"),
        ("Write a golden-ratio verse program that grows its lines 1,1,2,3,5,8 and lands the verdict", "explicit_or_signature"),
        ("Write a growing-sequence program with token counts 1,1,2,3,5,8 that computes the average load", "explicit_or_signature"),
        ("Compose a poem program whose line lengths follow the fibonacci sequence and carry a real computation", "explicit_or_signature"),
        ("Write a verse program that grows like nature's proportions to report log statistics", "boundary"),
        ("Write a six-to-eight line program that formats a report of uptimes", "boundary"),
    ],
    "limerick": [
        ("Write a limerick program: five lines shaped 8-8-5-5-8 with a comic punchline on the final line, reading health booleans", "explicit_or_signature"),
        ("Build a limerick-shaped program that computes an average load and lands a dry deflation joke about the answer", "explicit_or_signature"),
        ("Write a five-line comic verse program in AABBA rhythm that ends on the real result as the joke", "explicit_or_signature"),
        ("Write an 8-8-5-5-8 shaped program that parses a log and delivers a punchline about the error count", "explicit_or_signature"),
        ("Compose a five-line humorous program with two short middle lines and a long closing punchline", "explicit_or_signature"),
        ("Write a joke-shaped verse program that reports how many services are down", "boundary"),
        ("Write a five-line program that counts words in a config file", "boundary"),
    ],
    "etheree": [
        ("Write an etheree program: ten lines whose token counts climb 1-2-3-4-5-6-7-8-9-10, computing the mean and landing the result on the ten-token final line", "explicit_or_signature"),
        ("Build an etheree-shaped program with the 1-to-10 ladder that checks service health and lands the verdict", "explicit_or_signature"),
        ("Write a ten-line ladder program growing one token per line that counts log errors", "explicit_or_signature"),
        ("Write a 1-2-3-4-5-6-7-8-9-10 shaped program that sums a list and reports on the top rung", "explicit_or_signature"),
        ("Compose a ten-rung poem program where each line is one token longer than the last and the final line carries the answer", "explicit_or_signature"),
        ("Write a ladder-shaped verse program that reports the average response time", "boundary"),
        ("Write a ten-line program that validates an input schema", "boundary"),
    ],
}

existing_ids = {r["id"] for r in data["records"]}
next_id = max(existing_ids) + 1
for skill in NEW:
    assert skill not in data["skills"], f"{skill} already registered"
    data["skills"].append(skill)
    for prompt, rtype in NEW_RECORDS[skill]:
        data["records"].append(
            {"id": next_id, "prompt": prompt, "target": skill, "type": rtype}
        )
        next_id += 1

# renumber sequentially
for i, r in enumerate(sorted(data["records"], key=lambda r: r["id"]), start=1):
    r["id"] = i

BP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print(f"dataset: {len(data['skills'])} skills, {len(data['records'])} records")

# quick hygiene: no cross-skill tokens in new prompts
SKILLS = data["skills"]
for rec in data["records"]:
    low = rec["prompt"].lower()
    for other in SKILLS:
        if other == rec["target"] or other in ("none", "trap"):
            continue
        if re.search(r"(?<![a-z0-9])" + re.escape(other) + r"(?![a-z0-9])", low):
            print("CROSS-TOKEN", rec["id"], other, "->", rec["prompt"][:80])

print("done")
