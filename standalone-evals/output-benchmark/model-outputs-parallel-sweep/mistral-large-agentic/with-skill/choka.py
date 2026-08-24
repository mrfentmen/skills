import sys
nums = sys.stdin.read().split()
vals = [int(n) for n in nums]
total = sum(vals)
count = len(vals)
print("sum:", total)
print("count:", count, "numbers")