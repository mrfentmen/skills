data = [int(x) for x in input().split()]
total = sum(data)
count = len(data)

print("sum", total)
print("count", count)

avg = total // count
print("avg", avg)