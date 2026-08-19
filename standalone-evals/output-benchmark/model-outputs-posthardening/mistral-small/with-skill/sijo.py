import sys; data = list(map(float, sys.stdin.read().split())) if sys.stdin.readable() else []; avg = sum(data) / len(data) if data else 0
print("average:", avg)
print("above average:", sum(1 for x in data if x > avg), "- the majority hides in plain sight")
