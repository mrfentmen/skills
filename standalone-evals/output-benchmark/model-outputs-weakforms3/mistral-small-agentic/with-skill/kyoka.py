import sys
nums = [int(x) for x in sys.stdin.read().split()]
peak = max(nums)
spread = peak - min(nums)
print("peak", peak)
print("spread", spread)
print("and the spread is the joke")