import sys
text = sys.stdin.read()
words = text.split()
total = len(words)
print("word", "count", "is", total, "in", "this", "verse", "now")
print(total)
