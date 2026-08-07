import sys
numbers = [int(x) for x in sys.stdin.read().split()]
total = sum(numbers)
count = len(numbers)
print(total // count)
