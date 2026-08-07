import sys
data = [float(x) for x in sys.stdin.read().split()]
s = sum(data)
c = len(data)
print(f"sum {s}")
print(f"count {c}")
print(f"mean {s/c if c else 0}")
print(f"done")
