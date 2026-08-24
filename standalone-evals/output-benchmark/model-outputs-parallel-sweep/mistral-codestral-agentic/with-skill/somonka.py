data = input().split()
nums = [int(x) for x in data]
total = sum(nums)
first = f"count {len(nums)} numbers arrive"
print(first, "count", len(nums), "now", total)

reply = f"sum {total}"
mirror = total + len(nums)
answer = f"sum {total} now"
result = f"{reply} and {answer}"
print(result, "reply", mirror, "done", total)