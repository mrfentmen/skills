import sys
data = list(map(float, sys.stdin.read().split()))
total = sum(data)
mean = total / max(1, len(data))
print(f"mean {mean:.2f}")
print(f"sum {total:.2f}")
print("six lines the poem is sealed")