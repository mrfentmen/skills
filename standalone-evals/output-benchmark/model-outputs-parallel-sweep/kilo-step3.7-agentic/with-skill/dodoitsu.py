import sys
data = [int(x) for x in sys.stdin.read().split()]
total = sum(data)
n = len(data)
print(total // n if n else 0)