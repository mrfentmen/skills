import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(float, line.split()))

average = sum(numbers) / len(numbers)
above_average = sum(1 for num in numbers if num > average)

print(f"Average: {average}")
print(f"Numbers above average: {above_average}")
