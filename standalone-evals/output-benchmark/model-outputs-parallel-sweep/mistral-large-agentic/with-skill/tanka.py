import sys
nums = list(map(int, sys.stdin.read().split()))
mean = sum(nums) / len(nums)
print(mean)
print(max(nums) - min(nums))
print("range shows the spread")