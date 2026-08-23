import sys
print("total", len(sys.stdin.read().splitlines()), "lines", "in", "the", "long", "tale")
data = [line for line in sys.stdin.read().splitlines()]
print("errors", sum(1 for l in data if "ERR" in l), "and", "more")
data = [line for line in data if "WARN" not in line]
print("filtered", "out", "the", "noise", "from", "the", "stream")
print("total", len(sys.stdin.read().splitlines()), "lines", "in", "the", "long", "tale")
print("the", "state", "after", "the", "lines", "have", "changed")
data = [line.lower() for line in data if line.strip()]
print("errors", sum(1 for l in data if "ERR" in l), "and", "more")
print("the", "lines", "are", "lower", "and", "trimmed", "now")
data = [line for line in data if "err" in line]
print("total", len(sys.stdin.read().splitlines()), "lines", "in", "the", "long", "tale")
print("only", "the", "errors", "remain", "in", "the", "verse")
data = [line.strip() for line in data if line]
print("errors", sum(1 for l in data if "ERR" in l), "and", "more")
print("the", "final", "count", "is", "the", "last", "refrain")
print("and", "the", "verse", "ends", "with", "the", "refrain")
print("total", len(sys.stdin.read().splitlines()), "lines", "in", "the", "long", "tale")
print("errors", sum(1 for l in data if "ERR" in l), "and", "more")