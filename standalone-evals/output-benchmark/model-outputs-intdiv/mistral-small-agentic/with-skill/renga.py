nums = [int(x) for x in input().split()]
total = sum(nums)
count = len(nums)

print("sum", total)
print("count", count)

avg = total // count
print("avg", avg)