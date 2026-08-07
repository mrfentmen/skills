import sys
numbers = [float(line.strip()) for line in sys.stdin]  # statement: the numbers from stdin
average = sum(numbers) / len(numbers)                  # development: the average of the numbers
print("average:", average, "but", sum(1 for num in numbers if num > average), "numbers are above it")  # twist: numbers above average revealed
