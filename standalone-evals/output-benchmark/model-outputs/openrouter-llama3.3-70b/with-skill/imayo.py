import sys
numbers = [int(line) for line in sys.stdin]  # wave 1: the load
total = sum(numbers)                        # wave 2: the sum
count = len(numbers)                        # wave 3: the count
print(f"sum: {total}")                      # wave 4: the refrain
