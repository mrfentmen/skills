nums = [int(x) for x in input().split()]
total = sum(nums)

print("sum", total)
print("count", len(nums))

avg = total // len(nums)
print("avg", avg)