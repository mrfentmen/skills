nums = list(map(int, input().split()))
s = sum(nums)
print("sum", s, "of", "the", "list")

r = nums[::-1]
s2 = sum(r)
print("reverse", "sum", s2, "same", "still")