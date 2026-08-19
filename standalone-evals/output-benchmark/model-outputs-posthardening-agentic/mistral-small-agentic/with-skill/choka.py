import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
total = sum(nums)
n = len(nums)
print(total)
print(n)