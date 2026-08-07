import sys
nums = [float(x) for x in sys.stdin.read().split()]
print(max(nums) if nums else 0)
