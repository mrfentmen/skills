import sys
data = list(map(int, sys.stdin.read().split()))
peak = max(data)
spread = peak - min(data)
print(f"{peak} {spread}")
print("data science: peak is", "the joke")