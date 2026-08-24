data = [int(x) for x in input().split()]
total = sum(data); count = len(data)
average = total // count if count else 0
print("the average is", average)