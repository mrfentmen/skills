import sys;data=sys.stdin.read().split() # verse 1: the breath of numbers
total=sum(int(x)for x in data)          # verse 2: the rolling sum
print(f"the sum is {total}")            # verse 3: the long breath of song
print(f"and ends the verse")            # verse 4: the short refrain
