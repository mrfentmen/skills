from collections import Counter
import sys
data = sys.stdin.read().split()
print(Counter(data).most_common(1)[0][0])
