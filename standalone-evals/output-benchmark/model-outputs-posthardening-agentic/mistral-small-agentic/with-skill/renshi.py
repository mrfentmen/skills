import sys

raw = sys.stdin.readline()          # stage 1: read the verse
tokens = raw.split()                # stage 2: split into words
count = len(tokens)                 # stage 3: count the words
print(count)                        # stage 4: print the count