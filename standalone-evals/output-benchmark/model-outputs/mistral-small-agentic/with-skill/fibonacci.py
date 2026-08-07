import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
total = sum(nums)
print(total)
print("sum", total)
print("is", "the", "total")
print("of", "all", "numbers")
print("final", "answer", total)
print("done")