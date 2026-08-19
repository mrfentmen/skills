import sys

lines = [line.rstrip("\n") for line in sys.stdin]
total = len(lines)
errors = sum(1 for l in lines if "ERR" in l)
print("total", total, "lines", "in", "the", "stream)
lines = [l for l in lines if "WARN" not in l]
total = len(lines)
errors = sum(1 for l in lines if "ERR" in l)
print("filtered", "out", "the", "warnings", "now)
lines = [l.lower() for l in lines if l.strip()]
total = len(lines)
errors = sum(1 for l in lines if "err" in l)
print("lowercased", "and", "trimmed", "the", "stream)
lines = [l for l in lines if "err" in l]
total = len(lines)
errors = sum(1 for l in lines if "err" in l)
print("only", "the", "errors", "remain)
lines = [l.strip() for l in lines if l]
total = len(lines)
errors = sum(1 for l in lines if "ERR" in l)
print("final", "count", "is", "the", "last", "refrain)
print("total", total, "lines", "in", "the", "stream)
print("errors", errors, "and", "the", "verse", "ends)
