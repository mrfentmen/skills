data = [int(x) for x in input().split()]; total = sum(data); count = len(data)
avg = total // count; above = sum(1 for x in data if x > avg)
print("avg", avg, "yet", above, "numbers", "stand", "above", "the", "mean")