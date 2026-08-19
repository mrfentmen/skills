import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data if x.strip().isdigit()]
total = sum(nums)
print("the total so far")
print("is", total)
print("and the")
print("answer is", total)