import sys
nums = [int(x) for x in sys.stdin.read().split()]
count = len(nums)
range = max(nums) - min(nums)
print("range", range, "count", count)