import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
print(f"sum {total}")
print(f"count {len(nums)}")
