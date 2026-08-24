import sys
nums = [float(x) for x in sys.stdin.read().split()]
total = sum(nums)
mean = total / len(nums)
print("mean", mean, "and", "the", "sum", "is", total)
print("six", "lines", "and", "the", "poem", "is", "done")