import sys
data = list(map(int, sys.stdin.read().split()))  # read numbers
total = sum(data)  # sum of numbers
avg = total // len(data) if data else 0
print(avg)  # output average plain