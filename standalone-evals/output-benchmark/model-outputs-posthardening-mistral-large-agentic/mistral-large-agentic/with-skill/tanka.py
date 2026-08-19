import sys
nums = list(map(int, sys.stdin.read().split()))
mean = sum(nums) / len(nums)
print(f"mean {mean:.2f}")
print(f"range {max(nums)-min(nums)}")