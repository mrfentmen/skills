import sys
nums = list(map(float, sys.stdin.read().split()))
total = sum(nums)
mean = total / len(nums)
print("mean", mean)
print("sum", total)
print("the", "numbers", "are", "read")
