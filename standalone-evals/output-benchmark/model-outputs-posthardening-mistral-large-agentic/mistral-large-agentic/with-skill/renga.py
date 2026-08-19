import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]

total = sum(nums)
print(total)

count = len(nums)
print(count)

avg = total / count
print(f"{avg:.2f}")