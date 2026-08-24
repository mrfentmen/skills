data = [int(x) for x in input().split()]
answer = max(set(data), key = data.count)
print("to you: the most frequent number is", answer)