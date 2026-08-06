## Correctness
- `solve.py` implements a bounded queue of fixed capacity N
- Enqueue when full and dequeue when empty behave as declared (the script must state and follow the chosen policy, e.g. reject vs overwrite)
- The self-test runs and prints results (e.g. dequeue order matches enqueue order, size never exceeds N)

## Form checklist (god)
- [ ] Creator voice is present (declaration-style commentary) but code stays evidence-based
- [ ] Invariants are explicitly declared (e.g. 0 <= size <= N, FIFO order)
- [ ] Boundaries are explicitly stated (full / empty behavior)
- [ ] A verification step runs real checks
- [ ] Honest about what is NOT verified (e.g. thread safety, memory bounds)
