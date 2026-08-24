import sys
data = sys.stdin.read().split()  # read the whole input stream
total = sum(int(x) for x in data)  # fold the numbers to their sum
print(f"the rolling sum is {total}")  # sing the final refrain