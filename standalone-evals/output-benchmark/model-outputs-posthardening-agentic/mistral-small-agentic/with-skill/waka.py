import sys
nums = list(map(int, sys.stdin.read().split()))
lo = min(nums)
hi = max(nums)
rng = hi - lo
cnt = len(nums)
print(rng, cnt)