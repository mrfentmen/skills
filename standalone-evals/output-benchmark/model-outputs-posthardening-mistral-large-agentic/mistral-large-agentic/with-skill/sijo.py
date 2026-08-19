nums = [float(x) for x in open(0).read().split()]          # statement: the numbers from stdin
avg = sum(nums) / len(nums)                                # development: the average
print(avg, "with", sum(1 for x in nums if x > avg), "above")  # twist: how many exceed it