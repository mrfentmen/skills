import sys

data = sys.stdin.read().split()
nums = [int(x) for x in data]
count = len(nums)
print("count", count, "numbers", "arrive", "now")

total = sum(nums)
reply = f"sum {total}"
mirror = total + count
answer = f"sum {total} now"
result = f"{reply} and {answer}"
print(result, "reply", mirror, "done", total)