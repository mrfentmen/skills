import sys; data = sys.stdin.read().split()
nums = [int(x) for x in data]
total = sum(nums)  # sum
cnt = len(nums)  # number of items
mean = total / cnt  # avg
print(f"mean {mean}, sum {total}") # final result
