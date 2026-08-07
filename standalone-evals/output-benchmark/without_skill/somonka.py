import sys
nums = [int(x) for x in sys.stdin.read().split()]
print("count", len(nums))
print("sum", sum(nums))
