import sys
nums = list(map(int, sys.stdin.read().split()))
hi = max(nums)
lo = min(nums)
print(hi - lo, len(nums))