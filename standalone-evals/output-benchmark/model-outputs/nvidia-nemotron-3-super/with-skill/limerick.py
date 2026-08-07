import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
print(f"summing {len(nums)} numbers")
print(f"the total is {total}")
print(f"and the joke is that it worked")
