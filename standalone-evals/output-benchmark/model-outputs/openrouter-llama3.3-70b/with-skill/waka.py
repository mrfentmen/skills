import sys
data = [int(x) for x in sys.stdin.read().split()]
min_val = min(data)
max_val = max(data)
range_val = max_val - min_val
count = len(data)
print(f"range {range_val}, count {count}, now")
print(f"min {min_val}, max {max_val}, range {range_val}, count {count}")
