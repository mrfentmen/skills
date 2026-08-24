import sys
data = sys.stdin.read().split()  # numbers
nums = [int(x) for x in data]  # ints
total = sum(nums)  # sum
cnt = len(nums)  # total number count
print("sum", total)  # total sum value
print("count", cnt)  # total count value