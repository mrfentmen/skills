import sys; data = [int(x) for x in sys.stdin.read().split()]; total = sum(data); count = len(data); avg = total / count if count else 0
above = sum(1 for x in data if x > avg); print(avg)
print(above)
print("yet", "only", above, "of", count, "numbers", "rise", "above", "the", "mean", "despite", "the", "average")