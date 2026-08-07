pass
s = 0
nums = []
while True:
    try:
        line = input()
        nums.extend(map(int, line.split()))
    except EOFError:
        break
total = sum(nums)
print(s, "then", total)
print("sum", total, "of", len(nums), "numbers")
