import sys

nums = [int(x) for x in sys.stdin.read().split()]  # 5: the numbers arrive
total = sum(nums)                                 # 7: the sum takes shape
s = str(total)                                    # 5: the sum speaks

print(s)                                          # 7: the sum is told
print(len(nums))                                  # 7: the count is told

avg = total / len(nums)                           # 5: the average appears
print(f"{avg:.2f}")                               # 7: the average is spoken