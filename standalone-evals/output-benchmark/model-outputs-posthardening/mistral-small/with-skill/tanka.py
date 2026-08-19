import sys
nums = list(map(float, sys.stdin.read().split()))
mean = sum(nums) / len(nums)
print(f"mean {mean:.2f}")
range_ = max(nums) - min(nums)
print(f"range {range_:.2f} now")
