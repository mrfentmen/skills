import sys

data = sys.stdin.read().split()
nums = [int(x) for x in data]
count = len(nums)
print("count", count, "numbers", "arrive", "now")

first = f"five {count} numbers"
second = "sum is the next reply"
third = "count and sum"
fourth = "two voices meet"
fifth = "first voice speaks"

print(first, "now", second, third, fourth)
print(fifth, "done", count)

reply = sum(nums)
answer = f"sum {reply}"
mirror = count + reply
result = f"sum {reply} now"
final = f"second voice answers"

print(answer, "with", result, "the", mirror)
print(final, "done", reply)
