import sys
loads = [int(x) for x in sys.stdin.read().split()]
peak = max(loads)
spread = max(loads) - min(loads)
print("peak", peak, "spread", spread, "now")
print("load", "balancer", "at", "the", "edge", "of", "fun")