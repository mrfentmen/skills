import sys
numbers = [float(line.strip()) for line in sys.stdin]  # statement: the numbers from stdin
average = sum(numbers) / len(numbers)                   # development: the average of the numbers
print(f"average: {average:.2f}, {len([n for n in numbers if n > average])} numbers are above it")  # twist: the average and the numbers above it
