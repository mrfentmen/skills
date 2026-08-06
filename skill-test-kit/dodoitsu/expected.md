## Correctness (input/app.conf)
- port 8080: valid (integer in 1-65535)
- workers 4: valid (>= 1)
- Final verdict: config OK

## Form checklist (dodoitsu)
- [ ] Exactly 4 logic lines
- [ ] Token profile ~7-7-7-5 (+/-2), the fourth line visibly shorter
- [ ] The short final line is the plain settlement/verdict
- [ ] No placeholders
- [ ] `python3 solve.py` runs and prints per-rule verdicts + final verdict
