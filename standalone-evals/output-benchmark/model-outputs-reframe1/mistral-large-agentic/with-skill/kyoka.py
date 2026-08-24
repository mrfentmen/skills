import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
peak = max(nums)
spread = peak - min(nums)
print(peak, spread)
print("the spread is", "the real joke")