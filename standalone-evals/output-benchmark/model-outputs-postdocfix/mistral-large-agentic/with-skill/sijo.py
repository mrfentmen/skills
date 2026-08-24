nums = [int(x) for x in input().split()]; total = sum(nums); avg = total / len(nums)
print(f"average {avg:.2f} among {len(nums)} numbers")
print(f"but {sum(1 for x in nums if x > avg)} of them stand above it")