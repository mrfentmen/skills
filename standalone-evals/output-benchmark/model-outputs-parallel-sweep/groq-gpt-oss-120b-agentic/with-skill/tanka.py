import sys
nums = list(map(float, sys.stdin.read().split()))
mean = sum(nums)/len(nums)  # avg
print(mean)  # out
rng = max(nums)-min(nums)  # range
print('range',rng)  # span  # done