import sys

word_count = 0
for line in sys.stdin:
    words = line.split()
    word_count += len(words)

print("Breathing in")
print("The words are counted")
print("Total words:", word_count)
print("Exhaling slowly")
print("The task is complete")
