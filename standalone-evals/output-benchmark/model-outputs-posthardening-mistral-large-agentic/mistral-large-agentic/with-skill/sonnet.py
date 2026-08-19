import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data]
total = sum(nums)
print(f"sum {total}")
count = len(nums)
if count:
    mean = total / count
    print(f"mean {mean:.2f}")
else:
    print("none")
print("the numbers' path now ends")
print(f"sum {total}")