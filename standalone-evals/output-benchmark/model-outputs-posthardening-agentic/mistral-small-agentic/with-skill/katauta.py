import sys
from collections import Counter
nums = [int(x) for x in sys.stdin.read().split()]
print("to you:", Counter(nums).most_common(1)[0][0])