import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
print("sum", total, "is", "the", "total")
rev = nums[::-1]
total2 = sum(rev)
print("sum", total2, "is", "the", "reverse")
