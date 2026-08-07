import sys
nums = [int(x) for x in sys.stdin.read().split()]
mean = sum(nums) / len(nums)
count = len(nums)
total = sum(nums)
print("mean", mean)
print("count", count, "total", total)
print("numbers", count, "sum", total, "mean", mean)
print("total sum", total, "count", count, "mean is", mean)
print("sum and count", total, count, "mean settles", mean)
print("final mean", mean, "sum", total, "count", count, "sealed")
