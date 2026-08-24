import sys
nums = list(map(int, sys.stdin.read().split()))
hi = max(nums)
lo = min(nums)
print(f"range {hi - lo}")
print(f"count {len(nums)}")