# Stage 1: Read input from stdin
import sys
text = sys.stdin.readline().strip()

# Stage 2: Split text into tokens
tokens = text.split()

# Stage 3: Count and print tokens
token_count = len(tokens)
print(token_count)
