import sys

def cinquain(word_count):
    lines = [
        str(word_count % 100),
        str(word_count % 1000),
        str(word_count % 10000),
        str(word_count % 100000000),
        str(word_count % 100)
    ]
    return '\n'.join(lines)

word_count = 0
for line in sys.stdin:
    words = line.split()
    word_count += len(words)

print(cinquain(word_count))
