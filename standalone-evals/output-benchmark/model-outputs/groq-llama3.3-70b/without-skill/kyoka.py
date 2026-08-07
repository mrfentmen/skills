import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

if not numbers:
    print("Empty input")
    sys.exit(1)

peak = max(numbers)
spread = max(numbers) - min(numbers)

print(f"Peak so high {peak}")
print(f"Numbers spread {spread} wide")
print(f"Like a mountain")
print(f"Where the peak is high and wide")
print(f"But then I fell and face-planted with pride")
