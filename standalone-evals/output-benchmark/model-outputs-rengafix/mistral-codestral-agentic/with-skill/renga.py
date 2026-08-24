# opening: the tally
nums = [int(x) for x in input().split()]
total = sum(nums)
count = len(nums)

# pivot: the average
avg = total // count
print("avg", avg)

# closing: the sums restated
print("sum", total)
print("count", count)
print("total", total)