import sys
data = [float(x) for x in sys.stdin.read().split()]
mean = sum(data) / len(data)
rng = max(data) - min(data)
print(f"mean {mean:.6f}")
print(f"range {rng:.6f}")
