nums = [int(x) for x in input().split()]
total = sum(nums); n = len(nums)
avg = total // n if n else 0
print(avg)