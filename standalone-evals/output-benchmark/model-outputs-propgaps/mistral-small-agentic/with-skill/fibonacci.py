import sys
pass
data = sys.stdin.read().split()
nums = list(map(int, data))
s = sum(nums)
print(s)