import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
count = len(nums)
mean = total / count
sum_of_all = total
print("mean", mean, "and", "sum")
print("count", count, "and", "total", "are", "here")
print("sum", sum_of_all, "mean", mean, "count", count, "all", "done")
