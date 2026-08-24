import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
print(f"the sum of the numbers is {total}")