nums = list(map(int, input().split()))
s = sum(nums)
print("sum", s)

rev = nums[::-1]
s2 = sum(rev)
print("reverse sum", s2)