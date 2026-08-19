import sys
data = sys.stdin.read().split()
nums = [int(n) for n in data]
total = sum(nums)
print(f"sum: {total}")