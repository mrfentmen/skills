import sys
data = list(map(int, sys.stdin.read().split()))
print("to you:", max(set(data), key=data.count))