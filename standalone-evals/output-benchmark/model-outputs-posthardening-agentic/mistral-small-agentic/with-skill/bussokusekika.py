import sys
data = list(map(float, sys.stdin.read().split()))
total = sum(data)
mean = total / len(data)
print("mean", mean)
print("sum", total)
print("six", "lines", "and", "the", "poem", "is", "done")