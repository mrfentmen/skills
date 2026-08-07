import sys
total = len(sys.stdin.read().splitlines())
errors = sum(1 for line in sys.stdin.read().splitlines() if "ERR" in line)
print("total", total, "lines")
data = [line for line in sys.stdin.read().splitlines()]
print("errors", errors, "and", "more")
data = [line for line in data if "WARN" not in line]
print("total", total, "lines")
data = [line.lower() for line in data if line.strip()]
print("errors", errors, "and", "more")
data = [line for line in data if "err" in line]
print("total", total, "lines")
print("only", "the", "errors", "remain")
data = [line.strip() for line in data if line]
print("errors", errors, "and", "more")
print("the", "final", "count", "is")
print("total", total, "lines")
print("errors", errors, "and", "more")
