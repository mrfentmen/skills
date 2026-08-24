import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
print(f"the rolling sum is {total}")