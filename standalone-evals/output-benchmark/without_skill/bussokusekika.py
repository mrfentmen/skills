import sys
nums = [int(x) for x in sys.stdin.read().split()]
print("mean", sum(nums) / len(nums), "sum", sum(nums))
