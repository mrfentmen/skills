import sys
nums = [float(x) for x in sys.stdin.read().split()]
mean = sum(nums) / len(nums)
spread = max(nums) - min(nums)
print("mean", mean, "range", spread, "now")