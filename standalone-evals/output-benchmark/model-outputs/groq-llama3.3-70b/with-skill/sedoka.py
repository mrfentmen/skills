import sys
nums = list(map(int, sys.stdin.read().split()))
forward = "sum " + str(sum(nums))
print(forward, "is", "the", "sum", "now")

rev = nums[::-1]
backward = "sum " + str(sum(rev))
print(backward, "is", "the", "mirror", "sum")
