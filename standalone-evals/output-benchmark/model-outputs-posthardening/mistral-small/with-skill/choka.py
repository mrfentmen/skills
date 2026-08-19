import sys
data = sys.stdin.read().split()                 # 5: the stream arrives
nums = [float(x) for x in data]                 # 7: the numbers form
total = sum(nums)                               # 5: the sum is born
count = len(nums)                               # 5: the count is known
print(f"sum={total}")                           # 7: the sum is spoken
print(f"count={count}")                         # 7: the count is spoken
