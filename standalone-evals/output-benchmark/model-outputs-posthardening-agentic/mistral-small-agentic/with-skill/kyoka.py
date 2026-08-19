import sys
data = list(map(int, sys.stdin.read().split()))
peak = max(data)
spread = max(data) - min(data)
print("peak", peak)
print("spread", spread)
print("load", "balancer", "at", "the", "edge")
print("of", "fun", "and", "zero", "grace")