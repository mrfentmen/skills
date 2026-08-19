import sys
h = int(sys.stdin.read())
print("estimate", h * (1 if h else 2), "hours")
