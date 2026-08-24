import sys
nums = list(map(float, sys.stdin.read().split()))
total = sum(nums)
mean = total / len(nums)
print(f"mean {mean:.2f} sum {total:.2f}")
print("the", "mean", "and", "the", "sum", "are")
print("here", "the", "final", "truth", "is")
print("numbers", "yield", "their", "fate")