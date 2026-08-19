import sys
loads = list(map(int, sys.stdin.read().split()))
peak = max(loads)
spread = peak - min(loads)
print(f"peak {peak} spread {spread}")
print("load balancer: now serving 1 request")