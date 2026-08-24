import sys
nums = [int(x) for x in sys.stdin.read().split()]  # verse one: gather the numbers
total = sum(nums)  # verse two: the rolling sum
print(f"the sum is {total}")  # verse three: the long breath ends here
print(total)  # verse four: the short refrain lands the tale