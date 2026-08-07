nums = [int(x) for x in input().split()]
mean = sum(nums) / len(nums)
print(mean)
range_val = max(nums) - min(nums)
print("range", range_val)
print("mean and range", mean, range_val)
