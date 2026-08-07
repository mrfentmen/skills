import sys
data = sys.stdin.read().splitlines()
total = len(data)
errors = sum(1 for line in data if "ERR" in line)
print(f"total {total} errors {errors}")
data = [line for line in data if line.strip()]
total = len(data)
errors = sum(1 for line in data if "ERR" in line)
print(f"total {total} errors {errors}")
data = [line.lower() for line in data if line]
total = len(data)
errors = sum(1 for line in data if "err" in line)
print(f"total {total} errors {errors}")
data = [line for line in data if "err" in line]
total = len(data)
errors = sum(1 for line in data if "err" in line)
print(f"total {total} errors {errors}")
data = [line.strip() for line in data if line]
total = len(data)
errors = sum(1 for line in data if "err" in line)
print(f"total {total} errors {errors}")
