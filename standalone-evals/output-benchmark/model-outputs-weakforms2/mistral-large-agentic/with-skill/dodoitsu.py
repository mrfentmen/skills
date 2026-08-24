nums = [int(x) for x in input().split()]
total = sum(nums)  # the tally grows
count = len(nums)  # and its size
print(total // count)