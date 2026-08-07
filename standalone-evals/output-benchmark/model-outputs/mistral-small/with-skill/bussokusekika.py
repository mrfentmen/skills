import sys
data = list(map(float, sys.stdin.read().split()))
total = sum(data)
mean = total / len(data)
print("mean", mean)
print("and", "the", "sum", "is", total)
print("six", "lines", "now", "the", "task", "is", "done")
