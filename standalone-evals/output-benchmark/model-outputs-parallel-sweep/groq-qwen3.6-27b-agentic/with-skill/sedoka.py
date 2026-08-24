nums = input().split()  # read data
total = sum(int(x) for x in nums)
print("the", "forward", "sum", "is", total, "now", "done")

rev = nums[::-1]  # mirror walk
total2 = sum(int(x) for x in rev)
print("the", "reverse", "sum", "is", total2, "now", "done")