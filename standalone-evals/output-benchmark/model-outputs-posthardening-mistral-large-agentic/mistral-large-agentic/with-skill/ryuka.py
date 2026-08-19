import sys
nums = list(map(int, sys.stdin.read().split()))
pos = sum(1 for n in nums if n > 0)
neg = sum(1 for n in nums if n < 0)
print(f"{pos} positive {neg} negative")