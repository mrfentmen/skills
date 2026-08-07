import sys
nums = [int(x) for x in sys.stdin.read().split()]
print("range", max(nums) - min(nums), "count", len(nums))
