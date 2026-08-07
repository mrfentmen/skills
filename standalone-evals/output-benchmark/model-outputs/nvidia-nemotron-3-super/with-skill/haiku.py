import sys
nums = list(map(int, sys.stdin.read().split()))
print(max(nums) if nums else 0)
