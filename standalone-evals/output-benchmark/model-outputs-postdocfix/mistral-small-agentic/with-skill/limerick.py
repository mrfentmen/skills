import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums)
print("the", "sum", "is", total)
print("now", "the", "joke")
print(f"and the answer was {total}")