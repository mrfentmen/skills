import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
print("max", max(nums), "of", "them", "all")