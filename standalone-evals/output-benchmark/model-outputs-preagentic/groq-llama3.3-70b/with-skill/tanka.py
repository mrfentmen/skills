import sys
nums = [int(x) for x in sys.stdin.read().split()]
mean = sum(nums) / len(nums)
print("mean", mean)
range_val = max(nums) - min(nums)
print("range", range_val)
print(f"mean {mean:.2f} range {range_val}")
