import sys

nums = [int(x) for x in sys.stdin.read().split()]  # 5: the numbers march in

total = sum(nums)  # 7: the tally swells
count = len(nums)  # 5: and its count
mean = total / count  # 7: the center appears

print(total)  # 7: the sum is spoken
print(count)  # 7: the count is told
print(f"{mean:.2f}")  # 5: the average lands
