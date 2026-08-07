import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

max_num = max(numbers)
print(f"Numbers flowing free")
print(f"Maximum found within {max_num}")
print(f"Answer is {max_num} now")
