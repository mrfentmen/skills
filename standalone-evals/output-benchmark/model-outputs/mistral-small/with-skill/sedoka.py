import sys

data = list(map(int, sys.stdin.read().split()))
total = sum(data)
print("sum", total, "is", "the", "total")

rev = data[::-1]
rev_total = sum(rev)
print("reverse", "sum", rev_total, "mirrors", "the", "input")
