nums = [int(x) for x in input().split()]
total = sum(nums)
print("sum", total, "of", "the", "tale")

rev = nums[::-1]
total2 = sum(rev)
print("mirror", "sum", total2, "still", "same")