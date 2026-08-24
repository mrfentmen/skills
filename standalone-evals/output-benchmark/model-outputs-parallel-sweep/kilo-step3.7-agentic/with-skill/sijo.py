import sys
nums = [float(x) for x in sys.stdin.read().split()]
avg = sum(nums) / len(nums)
print(avg)
print(len([n for n in nums if n > avg]))