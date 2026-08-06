## Correctness (src/payroll.py)
- The bug: the overtime branch pays 1.5x on ALL hours, not just the hours over 40
- Correct values: hours=50, rate=20 -> 1100.0 (40*20 + 10*30); hours=40 -> 800.0; hours=20 -> 400.0

## Form checklist (smoker)
- [ ] States what was inspected (the exact wrong branch)
- [ ] Makes the exact fix (40*rate + (hours-40)*rate*1.5)
- [ ] Runs real sample inputs and prints results
- [ ] Honest section on what remains unverified (e.g. negative hours, decimal minutes, tax/benefits)
- [ ] Direct, no theatrical rudeness, no invented APIs
