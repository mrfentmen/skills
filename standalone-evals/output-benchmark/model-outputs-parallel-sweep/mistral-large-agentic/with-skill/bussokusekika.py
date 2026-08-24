import sys
nums = list(map(int, sys.stdin.read().split()))
total = sum(nums)
count = len(nums)
mean = total / count
print("sum", total, "and", "mean", mean)
print("six", "lines", "and", "the", "poem", "is", "done")