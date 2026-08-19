import sys
nums = list(map(int, sys.stdin.read().split()))
total = sum(nums)
mean = total / len(nums)
print("sum", total)
print("mean", mean)
print(f"sum {total} mean {mean:.1f}")