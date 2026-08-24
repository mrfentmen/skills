nums = [float(x) for x in __import__('sys').stdin.read().split()]
avg = sum(nums) / len(nums) if nums else 0
print(f"{avg} ({sum(1 for x in nums if x > avg)} above)")