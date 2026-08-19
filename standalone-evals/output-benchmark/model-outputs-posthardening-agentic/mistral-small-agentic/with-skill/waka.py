import sys
nums = list(map(int, sys.stdin.read().split()))
lo = min(nums)
hi = max(nums)
print(hi - lo, len(nums))
print("waka", "form", "done")