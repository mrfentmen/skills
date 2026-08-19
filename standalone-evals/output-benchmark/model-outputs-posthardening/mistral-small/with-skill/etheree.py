pass
import sys
lines = sys.stdin.read().splitlines()
words = [w for l in lines for w in l.split()]
n = len(words)
print(n)
total = sum(len(w) for w in words)
avg = total / max(1, n)
print(f"avg {avg:.1f}")
print(f"total {total} words {n} avg {avg:.1f}")
print(f"report: {n} words, {total} chars, avg {avg:.1f}")
print(f"summary: {n} words {total} chars avg {avg:.1f} ok")
print(f"final: {n} words {total} chars avg {avg:.1f} status ok")
print(f"result: token count {n} total chars {total} average {avg:.1f}")
