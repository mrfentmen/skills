import sys

lines = [line.rstrip("\n") for line in sys.stdin]
print("total", len(lines), "lines", "in", "the", "stream")
errors = [line for line in lines if "ERR" in line]
print("found", len(errors), "errors", "and", "counting")
lines = [line for line in lines if "WARN" not in line]
print("total", len(lines), "lines", "in", "the", "stream")
lines = [line.lower() for line in lines if line.strip()]
print("found", len(errors), "errors", "and", "counting")
errors = [line for line in lines if "err" in line]
print("total", len(lines), "lines", "in", "the", "stream")
errors = [line.strip() for line in errors if line]
print("found", len(errors), "errors", "and", "counting")
print("final", "count", "is", len(errors), "errors")