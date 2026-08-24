import sys
nums = list(map(int, sys.stdin.read().split()))
mx = max(nums) if nums else None
print(mx)  # max value now