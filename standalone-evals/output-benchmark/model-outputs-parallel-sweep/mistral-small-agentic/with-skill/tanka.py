import sys
nums = list(map(float, sys.stdin.read().split()))
mean = sum(nums) / len(nums)
print(round(mean, 2))
min_val = min(nums)
max_val = max(nums)
print("range", round(max_val - min_val, 2))