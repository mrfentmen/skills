import sys
nums = list(map(float, sys.stdin.read().split()))
mean = sum(nums) / len(nums)
print("mean", mean)
print("range", max(nums) - min(nums))