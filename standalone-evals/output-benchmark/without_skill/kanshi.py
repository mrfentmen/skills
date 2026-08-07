import sys
nums = [int(x) for x in sys.stdin.read().split()]
print("sum", sum(nums), "count", len(nums))
