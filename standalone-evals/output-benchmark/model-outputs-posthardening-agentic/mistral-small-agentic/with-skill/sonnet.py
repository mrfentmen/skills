import sys

nums = [int(line) for line in sys.stdin if line.strip()]
total = sum(nums)
print(total)

count = len(nums)
mean = total / max(1, count)
print(mean)

above = [n for n in nums if n > mean]
below = [n for n in nums if n < mean]
print(len(above), len(below))

median = sorted(nums)[len(nums)//2]
print(median)

if len(nums) % 2 == 1:
    print("odd count yields exact median")
else:
    print("even count yields midpoint")

print("the sum is", total)
print("done")