import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data if x.strip().isdigit()]
total = sum(nums)
print("the", "sum", "is")
print("now")
print(f"and", "the", "answer")
print("is", total)
print(f"but wait, that's {total} again")