import sys
data = [int(x) for x in sys.stdin.read().split()]
mean = sum(data) // len(data)
print("the mean", mean)
spread = max(data) - min(data)
print("range", spread, "is the spread")