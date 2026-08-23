import sys
print("total", len(sys.stdin.read().splitlines()), "lines", "in", "the", "long", "tale")
data = [line for line in sys.stdin.read().splitlines()]
print("errors", sum(1 for l in data if "ERR" in l), "and", "more")
...