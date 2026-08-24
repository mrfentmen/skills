import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
total = sum(nums)
count = len(nums)
print("sum", total)
print("count", count)
print("the sum is", total, "and the count is", count)