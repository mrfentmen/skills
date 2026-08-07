import sys
nums = [int(x) for x in sys.stdin.read().split()]
sum_val = sum(nums)
count = len(nums)
print("sum", sum_val, "count", count)
print("avg", sum_val / count, "median", sorted(nums)[count // 2])
turn = "stats"
print("turn", turn, "to", "stats")
print("resolve", "with", "sum", "and", "count")
