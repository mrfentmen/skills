nums = [int(x) for x in input().split()]
total = sum(nums)
count = len(nums)
print(total // count if count else "no numbers")