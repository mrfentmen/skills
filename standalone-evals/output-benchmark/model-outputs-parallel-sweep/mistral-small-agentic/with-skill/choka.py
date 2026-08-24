import sys
data = sys.stdin.read().split()
nums = list(map(int, data))
total = sum(nums)
count = len(nums)
print("sum", total)
print("count", count, "numbers")