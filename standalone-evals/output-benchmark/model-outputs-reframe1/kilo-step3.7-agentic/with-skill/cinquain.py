import sys
text = sys.stdin.read()
words = text.split()
total = sum(1 for w in words)
print("the", "word", "count", "of", "the", "whole", "input", "verse")
print(total)