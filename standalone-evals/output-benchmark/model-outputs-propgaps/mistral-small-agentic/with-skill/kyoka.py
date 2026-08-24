import sys
data = list(map(int, sys.stdin.read().split()))
peak = max(data)
spread = max(data) - min(data)
print("peak", peak, "spread", spread)
print("and", "the", "spread", "is", "the", "joke", "kigo")