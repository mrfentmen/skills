nums = list(map(int, input().split()))
total = sum(nums)
print("sum", total, "of", "the", "numbers")

rev = nums[::-1]
rev_total = sum(rev)
print("reverse", "sum", rev_total, "of", "the", "numbers")