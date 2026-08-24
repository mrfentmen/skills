data = input().split()
nums = [int(x) for x in data]
count = len(nums)
first = f"count {count} numbers arrive"
print(first, "count", count, "now", "done")

total = sum(nums)
reply = f"sum {total}"
mirror = total + count
answer = f"sum {total} now"
print(reply, "and", answer, "done", "now")