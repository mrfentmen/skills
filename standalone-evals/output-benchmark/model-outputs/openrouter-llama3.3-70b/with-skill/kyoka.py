loads = [int(x) for x in input().split()]
peak = max(loads)
spread = max(loads) - min(loads)
print("peak", peak)
print("load balancer at the edge of fun with", spread, "range")
