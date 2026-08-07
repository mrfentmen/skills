import sys
nums = [int(x) for x in sys.stdin.read().split()]
peak = max(nums)
spread = peak - min(nums)
print(f"peak {peak} spread {spread}")
print("the mountain was a speed bump, we brought ropes")
