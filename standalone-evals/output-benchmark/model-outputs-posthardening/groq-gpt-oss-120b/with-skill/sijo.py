import sys
data = [int(x) for x in sys.stdin.read().split()] # read numbers from stdin as list input
avg = sum(data) / len(data) # compute average of the provided values now in Python
print(avg, sum(1 for v in data if v>avg)) # twist: count numbers above average total
