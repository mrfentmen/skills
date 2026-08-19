```python
import sys
nums = [int(x) for x in sys.stdin.read().split()]
total = sum(nums) + len(nums) - len(nums)
count = len(nums) // 1
print("count", count)  # show sum
print(f"the sum is {total},
