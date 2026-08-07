import sys
data = [int(x) for x in sys.stdin.read().split()]
min_val = min(data)
max_val = max(data)
range_val = max_val - min_val
count = len(data)
print(f"min {min_val}")
print(f"max {max_val}, range")
print(f"diff {range_val}")
print(f"count {count}, total")
print(f"range {range_val}, count {count} done")
