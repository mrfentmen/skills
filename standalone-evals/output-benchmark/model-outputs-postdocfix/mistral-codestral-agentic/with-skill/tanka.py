data = [int(x) for x in input().split()]
mean = sum(data) // len(data)
print("the mean", mean)
spread = max(data) - min(data)
print("range", spread, "is the spread")