import sys
nums = list(map(int, sys.stdin.read().split()))
total = sum(nums)
mean = total / len(nums)
print("mean", mean)
print("sum", total)
print("done", "mean", "and", "sum")