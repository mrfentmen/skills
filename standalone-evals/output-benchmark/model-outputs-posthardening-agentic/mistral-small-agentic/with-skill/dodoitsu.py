import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
n = len(nums)
print(total // n if n else 0)