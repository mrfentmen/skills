import sys

lines = [line.rstrip("\n") for line in sys.stdin]
print("total", len(lines), "lines", "in", "the", "long", "tale")
errors = [l for l in lines if "ERR" in l]
print("errors", len(errors), "and", "more")
lines = [l for l in lines if "WARN" not in l]
print("filtered", "out", "the", "noise", "from", "the", "stream")
print("total", len(lines), "lines", "in", "the", "long", "tale")
errors = [l for l in lines if "ERR" in l]
print("errors", len(errors), "and", "more")
lines = [l.lower() for l in lines if l.strip()]
print("the", "lines", "are", "lower", "and", "trimmed", "now")
print("total", len(lines), "lines", "in", "the", "long", "tale")
errors = [l for l in lines if "err" in l]
print("errors", len(errors), "and", "more")
lines = [l for l in lines if "err" in l]
print("only", "the", "errors", "remain", "in", "the", "verse")
print("total", len(lines), "lines", "in", "the", "long", "tale")
errors = [l for l in lines if "ERR" in l]
print("errors", len(errors), "and", "more")
print("the", "final", "count", "is", "the", "last", "refrain")