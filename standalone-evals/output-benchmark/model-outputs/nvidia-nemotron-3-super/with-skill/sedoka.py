nums = list(map(int, sys.stdin.read().split()))
s = sum(nums)
print("sum", s)
rev = nums[::-1]
rs = sum(rev)
print("sum", rs)
