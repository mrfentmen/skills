import sys
data = [float(x) for x in sys.stdin.read().split()]
total = sum(data)
count = len(data)
print(total // count if count else "empty")