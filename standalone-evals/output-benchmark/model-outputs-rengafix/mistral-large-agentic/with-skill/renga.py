# opening: the tally
data = [int(x) for x in input().split()]
total = sum(data)
count = len(data)

# pivot: the average
avg = total // count
print("sum", total)

# closing: the sums restated
print("count", count)
print("avg", avg)
print("total", total)