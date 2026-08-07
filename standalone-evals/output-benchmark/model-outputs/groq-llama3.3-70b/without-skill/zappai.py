import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

max_num = max(numbers)
print(f"Numbers so many {max_num}")
print(f"Floating to the top")
print(f"Maximum is {max_num} found")
