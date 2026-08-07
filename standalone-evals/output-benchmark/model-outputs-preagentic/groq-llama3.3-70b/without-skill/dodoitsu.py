import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

average = sum(numbers) // len(numbers)
print(f"Numbers given to me")
print(f"Many, many numbers")
print(f"All added up with care")
print(f"Average is {average}")
