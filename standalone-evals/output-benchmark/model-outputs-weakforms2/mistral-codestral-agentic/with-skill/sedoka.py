nums = [int(x) for x in input().split()]
total = sum(nums); back = nums[::-1]
print("the forward sum is", total)

rev = sum(back)
print("the reverse sum is", rev)
print("the mirror sum is", rev)