import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
s = sum(nums)
print(s)