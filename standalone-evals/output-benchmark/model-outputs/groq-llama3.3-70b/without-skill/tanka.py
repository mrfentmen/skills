import sys

numbers = [float(line.strip()) for line in sys.stdin]
mean = sum(numbers) / len(numbers)
print(mean)

min_num = min(numbers)
max_num = max(numbers)
range_val = max_num - min_num

print(f"Mean found with gentle care")
print(f"Range {range_val} whispers low")
print(f"Numbers dance in secret night")
print(f"Mean and range in harmony")
print(f"Statistics' subtle delight")
