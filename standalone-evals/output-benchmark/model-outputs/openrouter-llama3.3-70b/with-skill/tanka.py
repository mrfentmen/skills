import sys
nums = [int(x) for x in sys.stdin.read().split()]
mean = sum(nums) / len(nums)
print("mean", mean)
range_ = max(nums) - min(nums)
print("range", range_)
print("mean and range", mean, range_)
