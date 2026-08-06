import sys
nums = [int(x) for x in sys.stdin.read().split()]
avg = sum(nums) // len(nums)
above = sum(1 for x in nums if x > avg)
print(avg, above)
