import sys

lines = [line.rstrip("\n") for line in sys.stdin]
print("total", len(lines), "lines", "in", "the", "stream")
errors = [line for line in lines if "ERR" in line]
print("errors", len(errors), "and", "more")
lines = [line for line in lines if "WARN" not in line]
print("filtered", "out", "the", "noise", "from", "the", "stream")
print("total", len(lines), "lines", "in", "the", "stream")
errors = [line for line in lines if "ERR" in line]
print("errors", len(errors), "and", "more")
lines = [line.lower() for line in lines if line.strip()]
print("the", "lines", "are", "lower", "and", "trimmed", "now")
print("total", len(lines), "lines", "in", "the", "stream")
errors = [line for line in lines if "err" in line]
print("errors", len(errors), "and", "more")
lines = [line.strip() for line in lines if line]
print("the", "final", "count", "is", "the", "last", "refrain")
print("and", "the", "verse", "ends", "with", "the", "refrain")
print("total", len(lines), "lines", "in", "the", "stream")
errors = [line for line in lines if "ERR" in line]
print("errors", len(errors), "and", "more")