import sys
numbers = [int(line) for line in sys.stdin.read().splitlines()]
positive_count = sum(1 for num in numbers if num > 0)
negative_count = sum(1 for num in numbers if num < 0)
print("positive", positive_count, "and", "negative", negative_count, "numbers")
print("total", len(numbers), "numbers", "read")
