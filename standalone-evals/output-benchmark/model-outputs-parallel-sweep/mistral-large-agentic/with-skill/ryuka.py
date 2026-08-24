import sys
nums = list(map(int, sys.stdin.read().split()))
up = sum(1 for n in nums if n > 0)
down = sum(1 for n in nums if n < 0)
print(f"up {up} down {down}")