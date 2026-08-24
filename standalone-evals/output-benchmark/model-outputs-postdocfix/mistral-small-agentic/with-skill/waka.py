import sys
nums = list(map(int, sys.stdin.read().split()))
rng = max(nums) - min(nums)
cnt = len(nums)
print("range", rng, "count", cnt)
print("now", "the", "waka", "is", "done")