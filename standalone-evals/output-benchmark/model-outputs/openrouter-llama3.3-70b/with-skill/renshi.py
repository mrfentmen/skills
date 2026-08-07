import sys
raw = sys.stdin.read()                # stage 1: read the raw text
tokens = raw.split()                  # stage 2: split into tokens
count = len(tokens)                   # stage 3: count the tokens
print("Token count:", count)          # stage 4: print the count
