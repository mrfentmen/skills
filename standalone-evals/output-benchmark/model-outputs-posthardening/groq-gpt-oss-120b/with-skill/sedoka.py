import sys as s  # alias
data = list(map(int, s.stdin.read().split()))  # read numbers
print("sum", sum(data))  # forward sum

rev = data[::-1]  # reverse
back = sum(rev)  # reverse sum
print("reverse sum", back)  # answer
