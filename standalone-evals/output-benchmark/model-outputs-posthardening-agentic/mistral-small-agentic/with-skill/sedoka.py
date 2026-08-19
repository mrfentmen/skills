import sys

nums = list(map(int, sys.stdin.read().split()))
total = sum(nums)
print("sum", total)

rev = nums[::-1]
rev_total = sum(rev)
print("reverse", rev_total)