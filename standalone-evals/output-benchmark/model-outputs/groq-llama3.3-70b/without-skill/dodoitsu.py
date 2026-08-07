import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

average = sum(numbers) // len(numbers)
print(f"Numbers given to me")
print(f"Average calculated slow")
print(f"Result is now quite clear")
print(f"{average}")
