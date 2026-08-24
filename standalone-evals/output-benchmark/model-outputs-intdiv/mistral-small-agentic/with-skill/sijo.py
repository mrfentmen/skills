import sys; data = list(map(int, sys.stdin.read().split())); total = sum(data); count = len(data)
avg = total // count; above = sum(1 for x in data if x > avg)
print(avg, "yet", above, "of", "them", "rise", "above", "the", "mean")