import sys
from collections import Counter

nums = list(map(int, sys.stdin.read().split())) # read
cnt = Counter(nums) # count now please
print("to you:", Counter(nums).most_common(1)[0][0]) # answer now please