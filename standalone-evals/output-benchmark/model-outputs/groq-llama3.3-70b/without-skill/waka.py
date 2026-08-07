import sys

numbers = [int(line.strip()) for line in sys.stdin]
min_num = min(numbers)
max_num = max(numbers)
count = len(numbers)
range_num = max_num - min_num

print(f"Numbers {count} found")
print(f"Range is {range_num} wide now")
print(f"Min {min_num} to max")
print(f"Count is {count} numbers")
print(f"Range {range_num} with {count} numbers")
