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
print("Range's soft caress falls")
print("Numbers' soothing hush")
print("Mean and range entwined slow")
print("Statistics' peaceful night")
