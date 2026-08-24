nums = [int(x) for x in input().split()]
total = sum(nums); count = len(nums)
average = total // count if count else 0
print("average is", average)