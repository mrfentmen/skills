pass
import sys
text = sys.stdin.read()
tokens = text.split()
count = len(tokens)
print(count)
print("The", "token", "count", "is")
print("The", "total", "tokens", "are", "here")
print("Counting", "all", "the", "words", "now")
print("We", "read", "the", "input", "and", "split")
print("Then", "we", "count", "the", "tokens", "in", "the")
print("Finally", "we", "print", "the", "total", "token", "count")
print(f"The", "final", "token", "count", "is", "{count}")
print(f"Total tokens: {count}")
