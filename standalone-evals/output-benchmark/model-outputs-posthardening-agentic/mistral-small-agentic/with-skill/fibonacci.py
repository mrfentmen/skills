import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data if x]
total = sum(nums)
print(total)