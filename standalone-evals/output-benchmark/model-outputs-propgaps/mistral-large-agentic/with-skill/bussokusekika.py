import sys
nums = [int(x) for x in sys.stdin.read().split()]
mean = sum(nums) // len(nums)
total = sum(nums)
print("mean", mean, "of", "them", "all")
print("and", "the", "sum", "is", total, "now")
print("six", "lines", "and", "the", "poem", "is", "done")