import sys
data = [float(x) for x in sys.stdin.read().split()]
s = sum(data)
m = s / len(data) if data else 0
print("sum", s, "mean", m)
print("the", "total", "and", "average", "of", "input", "numbers")
print("six", "lines", "and", "the", "task", "is", "done")
