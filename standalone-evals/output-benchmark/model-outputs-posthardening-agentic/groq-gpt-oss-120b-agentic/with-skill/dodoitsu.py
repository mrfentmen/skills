import sys
data = list(map(int, sys.stdin.read().split()))  # read numbers
total = sum(data)                               # sum them up
cnt = len(data)                                 # count items total
print(total//cnt if cnt else 0)