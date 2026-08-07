import sys
raw = sys.stdin.readline()
clean = raw.rstrip('\n')
tokens = clean.split()

count = len(tokens)
print(count)
