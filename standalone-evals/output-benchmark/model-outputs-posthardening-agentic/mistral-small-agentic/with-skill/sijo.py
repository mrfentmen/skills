import sys; data = [float(x) for x in sys.stdin.read().split()]  # read all numbers from stdin into a list
avg = sum(data) / len(data) if data else 0.0  # compute the average, handling empty input safely
print(len([x for x in data if x > avg]), "numbers above the average")  # twist: reveal the count above the average