nums = list(map(int, input().split()))
total = sum(nums)
n = len(nums)
print(total // n if n else 0)