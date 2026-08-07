import sys
nums = list(map(int, sys.stdin.read().split()))
total = sum(nums)
count = len(nums)
mean = total / count if count > 0 else 0
print("sum:", total)
print("count:", count)
print("mean:", mean)
print("stats done")
print("input processed")
print(f"sum {total} over {count} numbers")
print(f"count {count} with mean {mean:.2f}")
