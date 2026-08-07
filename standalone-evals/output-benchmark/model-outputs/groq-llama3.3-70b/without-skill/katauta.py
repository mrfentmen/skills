from collections import Counter
import sys

def most_frequent_number(numbers):
    counter = Counter(numbers)
    most_common = counter.most_common(1)
    if most_common:
        return most_common[0][0]
    else:
        return None

def katauta_form(number):
    if number is not None:
        return f"Silent streams {number}\nGentle waves crash {number}\nMoonlight shines on {number}"
    else:
        return "No numbers found\nIn the empty space\nSilence remains"

numbers = [int(line.strip()) for line in sys.stdin]
most_frequent = most_frequent_number(numbers)
print(katauta_form(most_frequent))
