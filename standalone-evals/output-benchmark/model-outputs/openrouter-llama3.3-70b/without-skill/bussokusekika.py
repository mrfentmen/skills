import sys

numbers = [float(line.strip()) for line in sys.stdin]
mean = sum(numbers) / len(numbers)
total = sum(numbers)

print(f"Numbers {len(numbers)}")
print(f"Mean is {mean:.2f} now")
print(f"Sum of all {total:.2f} found")
print(f"Mean and sum in gentle hush")
print(f"Numbers whispering {mean:.2f} free")
print(f"Total sum {total:.2f} in silence")
