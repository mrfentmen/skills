import sys
nums = [int(x) for x in sys.stdin.read().split()]  # 7: the numbers arrive
total = sum(nums)                                  # 7: the tally grows
n = len(nums)                                      # 7: and its count
print(total // n if n else 0)                      # 5: the plain answer
