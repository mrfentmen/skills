import sys

nums = [int(x) for x in sys.stdin.read().split()]

total = sum(nums)

count = len(nums)

avg = total / count if count else 0

print(total)

print(count)

print(avg)