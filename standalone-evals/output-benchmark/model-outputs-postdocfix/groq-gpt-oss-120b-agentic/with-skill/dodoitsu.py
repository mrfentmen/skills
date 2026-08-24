import sys
data = [int(x) for x in sys.stdin.read().split()]
total = sum(data)  # sum of data
avg = total // len(data) if data else 0
print(avg)  # final average value