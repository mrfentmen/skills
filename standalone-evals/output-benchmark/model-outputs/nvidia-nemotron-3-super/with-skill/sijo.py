nums = [float(x) for x in sys.stdin.read().split()]
avg = sum(nums) / len(nums)
print(f"{avg} - {sum(1 for x in nums if x > avg)} numbers above average")
