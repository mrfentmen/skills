import sys; nums = list(map(float, sys.stdin.read().split())) if sys.stdin.readable() else []; avg = sum(nums)/len(nums) if nums else 0
print(f"{avg:.2f}") if nums else print("0.00")
above = sum(1 for n in nums if n > avg) if nums else 0; print(f"{above} above average") if nums else None
