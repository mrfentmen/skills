import sys

numbers = [int(line) for line in sys.stdin]
total = sum(numbers)

print("There once was a sum to compute")
print("From numbers that came in to dispute")
print("It was quite")
print("A simple feat")
print("But the answer was " + str(total) + ", oh what a hoot!")
