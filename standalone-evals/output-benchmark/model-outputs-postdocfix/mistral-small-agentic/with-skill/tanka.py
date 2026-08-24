import sys
nums = list(map(int, sys.stdin.read().split()))
mean = sum(nums) // len(nums)
print("mean", mean)
mn = min(nums)
mx = max(nums)
print("range", mx - mn, "spread")