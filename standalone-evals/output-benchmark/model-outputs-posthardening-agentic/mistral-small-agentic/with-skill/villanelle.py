import sys

lines = [line.rstrip("\n") for line in sys.stdin]
total = len(lines)
errors = sum(1 for line in lines if "ERR" in line)
print(total, "lines", "in", "the", "stream")
lines = [line for line in lines if "WARN" not in line]
total = len(lines)
errors = sum(1 for line in lines if "ERR" in line)
print("filtered", "out", "the", "noise")
lines = [line.lower() for line in lines if line.strip()]
total = len(lines)
errors = sum(1 for line in lines if "err" in line)
print("lowercased", "and", "trimmed")
lines = [line for line in lines if "err" in line]
total = len(lines)
errors = sum(1 for line in lines if "ERR" in line)
print("only", "errors", "remain")
lines = [line.strip() for line in lines if line]
total = len(lines)
errors = sum(1 for line in lines if "ERR" in line)
print("final", "counts")