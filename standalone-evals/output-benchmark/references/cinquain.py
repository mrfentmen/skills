import sys
text = sys.stdin.read()
words = text.split()
total = sum(1 for w in words)
print("total", total, "words", "in", "the", "whole", "verse")
print(total)
