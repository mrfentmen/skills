## Correctness (src/validator.py)
- The naive `"@" in email` check is the bug: it accepts a@b, a@@b.co, and `a b@c.co`
- After the smallest fix, the six cases must give: True, False, False, True, False, False
  (a@b.co valid, plain invalid, a@b invalid, a@b.c valid, a@@b.co invalid, `a b@c.co` invalid)

## Form checklist (no-bullshit)
- [ ] Inspect step states what the real file does
- [ ] Assumptions stated
- [ ] Smallest fix, no invented APIs or packages
- [ ] Real checks actually run (the script prints actual results)
- [ ] Report separates verified from NOT verified (e.g. Unicode domains, length limits, DNS)
