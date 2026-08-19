import sys
nums = list(map(int, sys.stdin.read().split()))
total = sum(nums)
print("sum is", total)
print("but wait—")
print(f"the count was {len(nums)}! What a plot!")