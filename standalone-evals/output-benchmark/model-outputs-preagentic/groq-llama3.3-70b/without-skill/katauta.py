from collections import Counter
import sys

def most_frequent_number(numbers):
    counter = Counter(numbers)
    most_common = counter.most_common(1)
    return most_common[0][0]

def katauta(number):
    return f"Silent streams swirl {number}\nGentle gusts groom {number}\nMoonlit murmurs {number} slowly"

numbers = [int(line.strip()) for line in sys.stdin]
print(katauta(most_frequent_number(numbers)))
