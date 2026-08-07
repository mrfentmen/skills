import sys
nums = list(map(int, sys.stdin.read().split()))
total = sum(nums)
print(f"sum {total} forward")
rev = nums[::-1]
total2 = sum(rev)
print(f"reverse {total2} same")
print("numbers mirrored")
