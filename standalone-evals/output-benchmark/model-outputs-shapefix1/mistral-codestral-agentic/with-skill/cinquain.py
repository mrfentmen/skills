import sys
text = sys.stdin.read()
words = text.split()
total = sum(1 for w in words)
print("the", "total", "word", "count", "is", total, "words")
print(total)