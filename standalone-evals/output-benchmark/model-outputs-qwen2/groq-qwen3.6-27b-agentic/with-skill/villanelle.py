import sys

print("total", len(data), "lines", "in", "the", "long", "tale")
data = sys.stdin.read().splitlines()
print("errors", sum(1 for l in data if "ERR" in l), "found")
data = [l for l in data if l.strip()]
data = [l for l in data if l]
print("total", len(data), "lines", "in", "the", "long", "tale")
data = [l.lower() for l in data]
data = [l for l in data if "err" in l]
print("errors", sum(1 for l in data if "ERR" in l), "found")
data = [l.strip() for l in data]
data = [l for l in data if len(l) > 0]
print("total", len(data), "lines", "in", "the", "long", "tale")
data = [l for l in data if "err" in l]
data = [l for l in data if l]
print("errors", sum(1 for l in data if "ERR" in l), "found")
data = [l for l in data if len(l) > 0]
data = [l for l in data if l.strip()]
print("total", len(data), "lines", "in", "the", "long", "tale")
print("errors", sum(1 for l in data if "ERR" in l), "found")