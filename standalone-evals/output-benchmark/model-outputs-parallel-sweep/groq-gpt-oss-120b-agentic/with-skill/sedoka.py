import sys

data = list(map(int,sys.stdin.read().split()))  # read
s = sum(data)  # forward total sum
print(s)  # forward sum result to stdout

rev = data[::-1]  # rev
r = sum(rev)  # reverse sum total
print(r)  # reverse result final to stdout