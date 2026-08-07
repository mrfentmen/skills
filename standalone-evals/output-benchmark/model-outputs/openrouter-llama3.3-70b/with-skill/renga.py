import sys
data = sys.stdin.read().split()         # 5: the numbers march in
nums = [int(x) for x in data]           # 7: the integers rise
total = sum(nums)                       # 5: the sum is found

count = len(nums)                       # 7: the count is clear
n = count                               # 7: the number stands

mean = total / n                        # 5: the average shines
print("sum", total)                    # 7: the sum is told
print("count", count)                  # 7: the count is spoken

print("average", mean)                 # 5: the average glows
print("of", "all", "the", "numbers")  # 7: the numbers align
