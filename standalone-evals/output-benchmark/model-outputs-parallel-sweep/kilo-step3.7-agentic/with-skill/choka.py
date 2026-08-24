import sys
raw = sys.stdin.read()
nums = [int(x) for x in raw.split()]
total = sum(nums)
count = len(nums)
print("sum:", total)
print("count:", count)