import sys
nums = [int(x) for x in sys.stdin.read().split()]
pos = sum(1 for n in nums if n > 0)
neg = sum(1 for n in nums if n < 0)
print(f"positive {pos} negative {neg}")