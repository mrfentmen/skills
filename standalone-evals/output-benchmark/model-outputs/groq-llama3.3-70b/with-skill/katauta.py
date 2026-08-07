import sys
data = [int(x) for x in sys.stdin.read().split()]
print("to you:")
counts = {x: data.count(x) for x in set(data)}
print("most frequent is", max(counts, key=counts.get), "with", max(counts.values()), "occurrences now")
