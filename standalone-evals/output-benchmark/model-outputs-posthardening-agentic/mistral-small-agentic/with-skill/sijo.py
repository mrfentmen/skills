import sys; data = [float(x) for x in sys.stdin.read().split()] if sys.stdin.readable() else []; avg = sum(data)/len(data) if data else 0
above = sum(1 for x in data if x > avg); print(avg if data else 0)
print("above average:", above if data else 0)