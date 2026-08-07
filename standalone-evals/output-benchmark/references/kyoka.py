import sys
loads = [int(x) for x in sys.stdin.read().split()]
spread = max(loads) - min(loads)
peak = max(loads)
print("peak", peak, "spread", spread, "now")
print("and", "the", "spread", "is", "the", "joke")
