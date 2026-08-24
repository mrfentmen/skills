import sys
from collections import Counter
nums = list(map(int, sys.stdin.read().split()))
cnt = Counter(nums)
print("to you:", cnt.most_common(1)[0][0])