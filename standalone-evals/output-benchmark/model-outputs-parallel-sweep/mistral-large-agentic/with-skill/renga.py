import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]

sum_all = sum(nums)
print("sum", sum_all)
print("of", "all", "the", "numbers")

count = len(nums)
print("count", count)
print("how", "many", "there", "are")

avg = sum_all / count
print(f"avg {avg:.2f}")