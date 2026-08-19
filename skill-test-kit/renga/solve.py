text = open("input/text.txt").read()
tokens = text.split()
vocab = set(tokens)

from collections import Counter
counts = Counter(tokens)

top = counts.most_common(3)
for word, n in top:
    print(f"{word} {n}")
