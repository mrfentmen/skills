import sys; data = list(map(float, sys.stdin.read().split())) if sys.stdin.readable() else []
avg = sum(data) / len(data) if data else 0
print(avg, sum(1 for x in data if x > avg), "above average")
