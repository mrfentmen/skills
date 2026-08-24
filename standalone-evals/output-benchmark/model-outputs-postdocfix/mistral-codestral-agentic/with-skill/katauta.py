data = [int(x) for x in input().split()]
answer = max(set(data), key = data.count)
print("you are the most frequent", answer)