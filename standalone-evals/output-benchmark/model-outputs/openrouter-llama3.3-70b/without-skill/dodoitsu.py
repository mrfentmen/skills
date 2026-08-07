import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

average = sum(numbers) // len(numbers)
print(f"Numbers were given to me")
print(f"I calculated with great care")
print(f"The average is a wondrous thing")
print(f"{average}")
