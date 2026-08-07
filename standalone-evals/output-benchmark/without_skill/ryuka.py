import sys
nums = [int(x) for x in sys.stdin.read().split()]
print("up", sum(n > 0 for n in nums), "down", sum(n < 0 for n in nums))
