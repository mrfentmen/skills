import sys
data = list(map(int, sys.stdin.read().split()))
mean = sum(data) // len(data)
print("mean", mean)
lo, hi = min(data), max(data)
print("range", hi - lo, "from", lo, "to", hi)