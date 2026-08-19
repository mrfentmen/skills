import sys
nums = list(map(int, sys.stdin.read().split()))
peak = max(nums)
spread = max(nums) - min(nums)
print("peak", peak, "spread", spread)
print("spread", "is", "just", "a", "number", "now", "boring")
