import sys
d=[int(x)for x in sys.stdin.read().split()]
p=max(d)
s=p-min(d)
print(f"peak {p} spread {s}")
print("sample size",len(d),"is the joke")