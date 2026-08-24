data = [int(x) for x in input().split()]
mean = sum(data) // len(data) # floor mean
print("mean",mean) # show mean now
rng = max(data) - min(data) # range.
print("range",rng) # expanded and spread now value