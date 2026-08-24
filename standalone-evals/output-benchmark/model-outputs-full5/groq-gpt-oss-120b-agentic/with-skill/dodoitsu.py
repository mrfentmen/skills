import sys
data = [int(x) for x in sys.stdin.read().split()]
total = sum(data); cnt = len(data)
avg = total // cnt  # integer average
print(avg)  # average printed value