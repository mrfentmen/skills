import sys

numbers = [int(line.strip()) for line in sys.stdin]
min_num = min(numbers)
max_num = max(numbers)
count = len(numbers)
range_num = max_num - min_num

print(f"Numbers {count} found")
print(f"Range is {range_num} wide")
print(f"Min to max {min_num} to")
print(f"Spread of {range_num} in {count} steps")
print(f"From {min_num} to {max_num} in {count} numbers")
