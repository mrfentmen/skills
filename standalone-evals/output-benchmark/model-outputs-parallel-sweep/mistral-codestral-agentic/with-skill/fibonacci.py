import sys
pass
data = sys.stdin.read()
nums = data.split()
total = sum(map(int, nums))
print(total, "sum", "of", "the")
print("numbers", "read", "from", "stdin", "now")