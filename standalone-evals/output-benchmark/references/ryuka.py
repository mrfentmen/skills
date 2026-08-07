import sys
numbers = [int(x) for x in sys.stdin.read().split()]
up = sum(n > 0 for n in numbers)
down = sum(n < 0 for n in numbers)
print("up", up, "down", down)
