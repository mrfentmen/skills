import sys
pos_count = 0
neg_count = 0
for line in sys.stdin:
    for num in line.split():
        if float(num) > 0:
            pos_count += 1
        elif float(num) < 0:
            neg_count += 1
print(f"positive {pos_count} and")
print(f"negative {neg_count} and")
print(f"counted {pos_count + neg_count} numbers")
print(f"done {pos_count}")
