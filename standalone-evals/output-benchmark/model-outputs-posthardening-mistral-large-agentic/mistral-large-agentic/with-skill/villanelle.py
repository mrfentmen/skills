import sys
data = sys.stdin.read().splitlines()
print("total", len(data))
errors = sum(1 for line in data if "ERR" in line)
print("errors", errors)
data = [line for line in data if "WARN" not in line]
print("total", len(data))
print("filtered", "out", "warnings")
data = [line.lower() for line in data if line.strip()]
errors = sum(1 for line in data if "ERR" in line)
print("errors", errors)
print("lower", "and", "trimmed")
data = [line for line in data if "err" in line]
print("total", len(data))
print("only", "errors", "remain")
data = [line.strip() for line in data if line]
errors = sum(1 for line in data if "ERR" in line)
print("errors", errors)
print("final", "count", "of", "errors")
print("total", len(data))
print("errors", errors)