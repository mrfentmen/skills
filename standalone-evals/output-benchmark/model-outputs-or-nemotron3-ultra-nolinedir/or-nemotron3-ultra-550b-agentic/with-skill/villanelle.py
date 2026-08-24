import sys
data = sys.stdin.read().splitlines()
print("total", len(data), "lines", "in", "the", "long", "tale")
errors = [l for l in data if "ERR" in l]
print("errors", len(errors), "found", "in", "the", "dark", "stream")
data = [l for l in data if "WARN" not in l]
print("total", len(data), "lines", "in", "the", "long", "tale")
errors = [l for l in data if "ERR" in l]
data = [l.lower() for l in data]
print("errors", len(errors), "found", "in", "the", "dark", "stream")
data = [l for l in data if l.strip()]
print("total", len(data), "lines", "in", "the", "long", "tale")
errors = [l for l in data if "ERR" in l]
data = [l.strip() for l in data]
print("errors", len(errors), "found", "in", "the", "dark", "stream")
data = [l for l in data if "err" in l]
print("total", len(data), "lines", "in", "the", "long", "tale")
errors = [l for l in data if "ERR" in l]
print("errors", len(errors), "found", "in", "the", "dark", "stream")
print("the", "final", "count", "is", "the", "last", "refrain")
print("total", len(data), "lines", "in", "the", "long", "tale")
print("errors", len(errors), "found", "in", "the", "dark", "stream")