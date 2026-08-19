import sys
nums = list(map(int, sys.stdin.read().split()))
small = min(nums)
large = max(nums)
span = large - small
print(f"{span} range, {len(nums)} count")