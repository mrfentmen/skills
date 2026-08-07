import sys
data = [int(x) for x in sys.stdin.read().split()]
if not data: print("0 0"); sys.exit()
mn = min(data); mx = max(data)
print(mx - mn, len(data))
