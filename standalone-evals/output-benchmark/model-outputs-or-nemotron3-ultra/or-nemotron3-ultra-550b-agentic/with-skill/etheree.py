import sys
sys.stdin
data=[]
data += sys.stdin.read().split()
n = len(data)
total = sum(map(len, data))
avg = total / max(1, n)
long = max(map(len, data), default = 0)
summary = ("count", n, "total", total, "average", avg)
report = (*summary, "score", n + total, "ok")
print("report", report, "items", len(report), "score", n+total, "status", "ok", "done", "valid")