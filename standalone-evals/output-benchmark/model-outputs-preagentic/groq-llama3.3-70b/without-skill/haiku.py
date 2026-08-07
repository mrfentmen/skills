import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

max_num = max(numbers)
print(f"Numbers flowing free {len(numbers)}")
print(f"Finding the greatest {max_num} shines")
print(f"Maximum found is {max_num} joy")
