import sys
nums = list(map(int, sys.stdin.read().split()))
mean = sum(nums) / len(nums)
print("the mean is", mean, "and the sum is", sum(nums))