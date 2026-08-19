import sys
data = list(map(int, sys.stdin.read().split()))  # numbers
n = len(data)  # count
rng = max(data)-min(data)  # range
ratio = rng / n if n else 0
print(f"range {rng} count {n}")  # resolve
