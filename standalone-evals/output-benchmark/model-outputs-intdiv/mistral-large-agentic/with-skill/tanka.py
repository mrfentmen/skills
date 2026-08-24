import sys
data = list(map(int, sys.stdin.read().split()))
mean = sum(data) // len(data)
print("mean", mean)
spread = max(data) - min(data)
print("range", spread)