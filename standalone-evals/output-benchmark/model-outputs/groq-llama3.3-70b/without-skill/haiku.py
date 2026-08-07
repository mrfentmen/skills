import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

max_num = max(numbers)
print(f"Numbers flowing free {max_num}")
print(f"Finding the greatest")
print(f"Maximum is {max_num}")
