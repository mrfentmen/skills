import sys
data = [int(x) for x in sys.stdin.read().split()]
pos = sum(1 for x in data if x > 0)
neg = sum(1 for x in data if x < 0)
print(pos, neg)
