import sys
data = list(map(int, sys.stdin.read().split()))
peak = max(data)
spread = peak - min(data)
print(f"peak {peak} spread {spread}")
print("sample size", len(data), "is the joke")