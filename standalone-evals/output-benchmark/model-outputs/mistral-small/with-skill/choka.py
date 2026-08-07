import sys
data = sys.stdin.read().split()                 # 5: the raw stream arrives
nums = list(map(float, data))                   # 7: the numbers take shape
total = sum(nums)                               # 5: the sum is born
count = len(nums)                               # 5: the count is known
print(f"sum={total} count={count}")             # 7+7: the couplet lands the tale
