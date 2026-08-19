pass
import sys
lines = sys.stdin.read().splitlines()
words = [w for l in lines for w in l.split()]
n = len(words)
print(n)
total = sum(len(w) for w in words)
print(total)
report = f"tokens {n} total {total}"
print(report)
print(f"mean {total / max(1, n):.1f}")
print(f"total tokens {total} in {n} words")