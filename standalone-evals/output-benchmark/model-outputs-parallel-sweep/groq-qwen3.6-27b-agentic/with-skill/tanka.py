import sys; data = sys.stdin.read().split()
nums = [float(x) for x in data]
mean = sum(nums) / len(nums)
rng = max(nums) - min(nums)
print("mean", mean, "range", rng, "now")