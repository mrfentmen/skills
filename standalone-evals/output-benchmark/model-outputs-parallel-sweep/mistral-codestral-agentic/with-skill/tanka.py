import sys
nums = [int(x) for x in sys.stdin.read().split()]
mean = sum(nums) / len(nums)
range_ = max(nums) - min(nums)
print("mean", mean, "range", range_)