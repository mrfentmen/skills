nums = [int(x) for x in input().split()]  # the numbers arrive in a single line
avg = sum(nums) / len(nums)  # the average is the sum divided by the count
print(avg, "is the average, and", sum(1 for x in nums if x > avg), "numbers are above it")