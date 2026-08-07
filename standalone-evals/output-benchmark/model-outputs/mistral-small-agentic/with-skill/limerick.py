import sys
nums = [int(l) for l in sys.stdin if l.strip()]
total = sum(nums)
print("the total is")
print(total)
print(f"and the joke is {total}")