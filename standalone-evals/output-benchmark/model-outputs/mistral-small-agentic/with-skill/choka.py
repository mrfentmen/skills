import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
total = sum(nums)
count = len(nums)
print(total)
print(count)