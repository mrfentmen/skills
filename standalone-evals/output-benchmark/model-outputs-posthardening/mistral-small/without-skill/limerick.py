import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))

total = sum(numbers)

line1 = "There once was a sum so divine,"
line2 = "It added up numbers in line."
line3 = "But the last line's the trick,"
line4 = "It's the sum—oh so slick!"
line5 = f"Total is {total}, that's fine!"

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
