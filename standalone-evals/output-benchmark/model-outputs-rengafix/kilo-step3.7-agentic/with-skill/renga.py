# opening: the tally
data = [int(x) for x in input().split()]
total = sum(data)
count = len(data)

# pivot: the average
avg = total // count
print("avg", avg)

# closing: the sums restated
print("sum", total)
print("count", count)
print("total", total)