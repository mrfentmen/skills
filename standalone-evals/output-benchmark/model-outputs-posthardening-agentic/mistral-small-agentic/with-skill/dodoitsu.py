import sys
nums = list(map(int, sys.stdin.read().split()))
avg = sum(nums) // len(nums) if nums else 0
print(avg)