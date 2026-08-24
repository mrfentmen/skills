data = [int(x) for x in input().split()]
total = sum(data)
count = len(data)

avg = total // count
print("sum", total)

print("count", count)
print("avg", avg)