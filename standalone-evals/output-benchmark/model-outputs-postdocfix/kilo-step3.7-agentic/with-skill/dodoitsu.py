data = [int(x) for x in input().split()]
total = sum(data)  # the total sum
count = len(data)  # count of numbers
print(total // count)  # result