import sys
nums = [int(x) for x in sys.stdin.read().split()]
lo = min(nums)
hi = max(nums)
print("range", hi - lo)
print("count", len(nums), "elements")
