import sys

nums = [int(x) for x in sys.stdin.read().split()]  # 5: the numbers arrive

total = sum(nums)  # 7: the sum is born
count = len(nums)  # 5: the count appears
print(total)  # 7: the first tale

avg = total / count  # 7: the middle speaks
print(count)  # 5: the second tale
print(avg)  # 7: the final word
