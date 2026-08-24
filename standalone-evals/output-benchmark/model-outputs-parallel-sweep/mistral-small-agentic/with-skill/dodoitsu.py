import sys
nums = list(map(int, sys.stdin.read().split()))
t = sum(nums)
n = len(nums)
print(t // n if n else 0)