import sys
nums = sys.stdin.read().split()
total = 0
for num in nums:
    total += int(num)
count = len(nums)
print(f"sum {total} and count {count}")
print(f"total {total} over {count} numbers")
