import sys

def etheree(token_count):
    lines = []
    for i in range(1, 11):
        line = ' '.join(str(token_count) for _ in range(i))
        lines.append(line)
    return '\n'.join(lines)

tokens = sys.stdin.read().split()
token_count = len(tokens)
print(etheree(token_count))
