import sys
numbers = [int(line) for line in sys.stdin.read().splitlines()]
total = sum(numbers)
count = len(numbers)
print("sum", total, "from", count, "numbers")
print("was", "work")
print("and")
print("now")
print("the answer is not what you expected, it's actually", total)
