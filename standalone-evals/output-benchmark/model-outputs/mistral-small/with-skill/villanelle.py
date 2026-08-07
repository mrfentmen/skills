import sys
lines = [line.rstrip('\n') for line in sys.stdin]
print("total", len(lines), "lines", "in", "the", "stream")
errors = sum(1 for l in lines if "ERR" in l)
print("errors", errors, "and", "trouble")
lines = [l for l in lines if "WARN" not in l]
print("total", len(lines), "lines", "in", "the", "stream")
errors = sum(1 for l in lines if "ERR" in l)
print("errors", errors, "and", "trouble")
lines = [l.lower() for l in lines if l.strip()]
print("total", len(lines), "lines", "in", "the", "stream")
errors = sum(1 for l in lines if "err" in l)
print("errors", errors, "and", "trouble")
lines = [l for l in lines if "err" in l]
print("total", len(lines), "lines", "in", "the", "stream")
errors = sum(1 for l in lines if "ERR" in l)
print("errors", errors, "and", "trouble")
lines = [l.strip() for l in lines if l]
print("total", len(lines), "lines", "in", "the", "stream")
errors = sum(1 for l in lines if "ERR" in l)
print("errors", errors, "and", "trouble")
