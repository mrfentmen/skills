import sys
nums = [int(x) for x in sys.stdin.read().split()]
print("peak", max(nums), "spread", max(nums) - min(nums))
