import sys;data=sys.stdin.read().split()
nums=[int(x)for x in data if x.isdigit()]
total=sum(nums)
print(f"sum: {total}")