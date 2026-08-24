import sys
nums = list(map(int, sys.stdin.read().split()))
count = len(nums)
small = min(nums)
large = max(nums)
print(f"{large-small} {count}")