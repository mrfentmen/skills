import sys

# 5-7-5: the numbers arrive
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
count = len(nums)
pivot = total

# 7-7: the sum is known
sum_result = f"sum: {pivot}"
count_result = count

# 5-7-5: the count is clear
pivot = count_result
avg = total / pivot
avg_result = f"average: {avg:.2f}"
count_str = str(pivot)

# 7-7: the count and average
print(f"count: {count_str}")
print(f"{sum_result}, {avg_result}")
