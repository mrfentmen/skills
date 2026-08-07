import sys
data = [int(x) for x in sys.stdin.read().split()]
print("to you:", max(set(data), key = data.count), "is the mode")
