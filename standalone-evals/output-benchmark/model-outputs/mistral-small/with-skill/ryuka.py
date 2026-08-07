import sys
nums = [int(x) for x in sys.stdin.read().split()]  # read all numbers from stdin
pos = sum(1 for n in nums if n > 0)               # count positive numbers
neg = sum(1 for n in nums if n < 0)               # count negative numbers
print(f"positive {pos} negative {neg}")           # landing line
