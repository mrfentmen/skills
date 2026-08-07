import sys

data = sys.stdin.read().split()
nums = [int(x) for x in data if x.lstrip('-').isdigit()]

print(len(nums))
print("count the", "numbers", "here")
print("tell me", "how many", "lines", "stand")
print("echo", "the", "length", "now")

total = sum(nums)

print(total)
print("sum the", "numbers", "here")
print("tell me", "how much", "they", "make")
print("echo", "the", "total", "now")