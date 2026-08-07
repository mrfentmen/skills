import sys
data = sys.stdin.read().split()          # 5: the numbers march in
nums = [int(x) for x in data]             # 7: the integers rise
total = sum(nums)                          # 5: the sum unfolds

count = len(nums)                          # 7: the count is known
n = count                                   # 7: the total count

mean = total / n                            # 5: the average dawns
print("sum", total)                         # 7: the sum is told
print("count", count)                       # 7: the count is shared

print("average", mean)                      # 5: the average shines
