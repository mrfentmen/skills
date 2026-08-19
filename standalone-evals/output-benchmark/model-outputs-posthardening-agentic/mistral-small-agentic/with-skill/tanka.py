import sys
nums = [float(x) for x in sys.stdin.read().split()]
mean = sum(nums) / len(nums)
print(f"mean {mean}")
print(f"range {max(nums)-min(nums)}")