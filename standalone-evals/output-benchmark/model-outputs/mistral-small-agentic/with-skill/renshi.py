import sys

raw = sys.stdin.readline()          # stage 1: read the line
tokens = raw.split()                # stage 2: split into tokens
count = len(tokens)                 # stage 3: count the tokens
print(count)                        # stage 4: print the count