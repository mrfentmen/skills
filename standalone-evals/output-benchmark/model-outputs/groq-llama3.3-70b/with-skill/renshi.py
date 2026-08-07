import sys

# stage 1: read the raw text
raw = sys.stdin.read()
lines = raw.splitlines()

# stage 2: extract the first line and split into tokens
first_line = lines[0] if lines else ''
tokens = first_line.split()

# stage 3: count the tokens
count = len(tokens)

# stage 4: print the token count
print(f"Token count: {count}")
