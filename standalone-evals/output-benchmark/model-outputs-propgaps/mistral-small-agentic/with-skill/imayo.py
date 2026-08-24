import sys
data = sys.stdin.read().split()  # gather all tokens from the scroll
total = sum(int(x) for x in data)  # turn each into a number and add them all
print("the", "sum", "is", total)  # sing the sum like a rolling refrain