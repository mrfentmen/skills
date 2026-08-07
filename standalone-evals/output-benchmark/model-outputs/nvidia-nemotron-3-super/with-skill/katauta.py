import sys
d = [int(x) for x in sys.stdin.read().split()]
m = max(set(d), key=d.count)
print("to you:", m)
