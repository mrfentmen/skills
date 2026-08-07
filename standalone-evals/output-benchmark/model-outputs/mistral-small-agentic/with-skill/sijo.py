import sys; data = list(map(float, sys.stdin.read().split()))
avg = sum(data) / len(data)
print(avg, sum(1 for x in data if x > avg))