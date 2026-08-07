import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

count = len(numbers)
total = sum(numbers)

print(f"Sum of numbers is {total}, count is {count}")
print(f"Total count is {count}, sum is {total}")
print(f"Turn to see the sum {total} and the count {count}")
print(f"Resolve with sum {total} and count {count}")
