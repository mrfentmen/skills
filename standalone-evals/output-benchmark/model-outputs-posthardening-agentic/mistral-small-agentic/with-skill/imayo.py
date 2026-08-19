import sys;data=sys.stdin.read().split() # verse one: the breath of numbers
total=sum(int(x)for x in data)          # verse two: the rolling sum
print(f"the sum is {total}")            # verse three: the long breath
print(f"and ends the verse")            # verse four: the short refrain