import sys
nums = [int(n) for n in sys.stdin.read().split()]
total = sum(nums)
print(f"the sum of the numbers is {total}")