nums = [int(x) for x in input().split()]
total = sum(nums); n = len(nums)
print(total // n if n else "empty")