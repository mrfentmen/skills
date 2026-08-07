import sys
from collections import Counter

def most_frequent_number(numbers):
    counter = Counter(numbers)
    return counter.most_common(1)[0][0]

def katauta(number):
    return f"Silent streams {number}\nGentle whispers {number}\nMoonlight shines on {number}"

numbers = [int(line.strip()) for line in sys.stdin]
print(katauta(most_frequent_number(numbers)))
