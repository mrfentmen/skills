import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)  # the tally grows
count = len(nums)  # and its count
print(total // count)  # done