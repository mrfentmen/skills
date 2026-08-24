import sys
nums = list(map(int, sys.stdin.read().split()))
lo = min(nums)
hi = max(nums)
print("range", hi - lo)
print("count", len(nums), "now")