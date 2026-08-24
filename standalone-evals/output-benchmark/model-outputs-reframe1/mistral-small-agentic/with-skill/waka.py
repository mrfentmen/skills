import sys
nums = list(map(int, sys.stdin.read().split()))
r = max(nums) - min(nums)
c = len(nums)
print("range", r, "count", c)
print("five", "lines", "and", "the", "poem", "is", "done")