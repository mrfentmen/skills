import sys
nums = [float(x) for x in sys.stdin.read().split()]
total = sum(nums)
print(f"sum: {total}")
