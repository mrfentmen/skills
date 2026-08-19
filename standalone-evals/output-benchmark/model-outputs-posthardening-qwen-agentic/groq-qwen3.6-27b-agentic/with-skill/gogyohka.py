import sys
text = sys.stdin.read()
words = text.split()
count = len(words)
message = f"total word count: {count}"
print(message)