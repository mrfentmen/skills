import sys

data = sys.stdin.read()                              # 5: the numbers arrive
nums = list(map(int, data.split()))                  # 7: the digits become numbers
total = sum(nums)                                   # 5: the sum is born
print(total)                                        # 7: the sum is told

count = len(nums)                                   # 5: the tally appears
print(count)                                        # 7: the count is shown

avg = total / count                                 # 5: the mean arrives
print(avg)                                          # 7: the average is spoken
