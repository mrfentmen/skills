import sys; nums = [float(x) for x in sys.stdin.read().split() if x.strip() and x != '']
avg = sum(nums) / len(nums); print(f"the average of all the numbers here is {avg:.2f}")
print(f"but {sum(1 for n in nums if n > avg)} numbers rise above it")