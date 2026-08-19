import sys

data = sys.stdin.read().split()
pos = sum(1 for x in data if float(x) > 0)
neg = sum(1 for x in data if float(x) < 0)
print(f"positive {pos} negative {neg}")