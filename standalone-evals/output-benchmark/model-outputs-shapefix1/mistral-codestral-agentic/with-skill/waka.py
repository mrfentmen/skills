import sys
nums = [int(x) for x in sys.stdin.read().split()]
spread = max(nums) - min(nums)
count = len(nums)
print("range", spread, "count", count, "now")
print("five", "lines", "and", "the", "poem", "is", "done")