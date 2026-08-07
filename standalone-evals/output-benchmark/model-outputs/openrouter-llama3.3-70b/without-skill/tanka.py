import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(float, line.split()))

mean = sum(numbers) / len(numbers)
print(mean)

min_num = min(numbers)
max_num = max(numbers)
range_num = max_num - min_num

print("Mean's gentle whisper")
print(f"Range's {range_num} soft sigh")
print("Numbers dance in air")
print(f"Mean and range entwined {mean} {range_num}")
print(f"Statistics' subtle {mean} {range_num} beauty")
