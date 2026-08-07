import sys
data = sys.stdin.read().split()
nums = [float(x) for x in data]
total = sum(nums)
count = len(nums)
print(f"sum={total}")
print(f"count={count}")
