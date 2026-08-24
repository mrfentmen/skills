import sys
nums = list(map(int, sys.stdin.read().split()))
peak = max(nums)
spread = max(nums) - min(nums)
print("peak", peak)
print("spread", spread)
print("now the load balancer")
print("sweats at the edge")
print("of fun")