import sys
lines = sys.stdin.read().splitlines()
words = sum(len(line.split()) for line in lines)
print(words)