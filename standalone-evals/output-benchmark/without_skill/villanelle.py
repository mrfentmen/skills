import sys
lines = sys.stdin.read().splitlines()
print("total", len(lines), "errors", sum(1 for l in lines if "ERR" in l))
