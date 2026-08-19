words = input().split()
n = len(words)
total = sum(len(w) for w in words)
avg = total / max(1, n)
long = max(len(w) for w in words)
report = f"tokens {total} words {n} avg {avg:.1f} max {long}"
print(report)