import sys
data = list(map(int, sys.stdin.read().split()))  # read
peak = max(data)  # top
spread = peak - min(data)
print(f"peak {peak} spread {spread}")  # report
print("all calm, data sings")  # haiku