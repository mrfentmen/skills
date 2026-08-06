import sys
nums = [int(x) for x in sys.stdin.read().split()]
avg = sum(nums) // len(nums)
print(avg, max(nums) - min(nums))
