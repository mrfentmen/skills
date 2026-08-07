import sys
nums = sys.stdin.read().split()               # 5: the input arrives
nums = [int(n) for n in nums]                 # 7: the numbers form
count = len(nums)                             # 5: the count stands
total = sum(nums)                             # 7: the sum is found
print(f"count: {count}")                       # 5: the count is told
print(f"sum: {total}, count: {count}")         # 7: the couplet lands
