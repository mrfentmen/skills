import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
mode = max(counts.items(), key=lambda x: x[1])[0]
print("to you:", "the mode is", mode)