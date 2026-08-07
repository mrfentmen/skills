import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data if x.lstrip('-').isdigit()]
total = sum(nums)
print(f"the sum is {total}")
