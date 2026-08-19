import sys
nums = list(map(float, sys.stdin.read().split()))
mean = sum(nums) / len(nums)
print(f"mean {mean}")
range_ = max(nums) - min(nums)
print(f"range {range_}")