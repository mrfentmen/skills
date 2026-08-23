import sys
data = sys.stdin.read().split()
nums = [float(x) for x in data]
total = sum(nums)
count = len(nums)
mean = total / count if count else 0
print("the sum of all the numbers is")
print(total, "is the total we found")
print("the count of values is now")
print(count, "items in the stream")
print("the mean is the sum over count")
print(mean, "is the average value")
print("but the sum is what we need")
print("the sum is", total, "now")