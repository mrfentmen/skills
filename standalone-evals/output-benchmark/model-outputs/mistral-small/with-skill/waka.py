import sys
nums = [int(x) for x in sys.stdin.read().split()]  # scene: the numbers
lo = min(nums)                                     # scene: the low
hi = max(nums)                                     # scene: the high
span = hi - lo                                     # the turn: the range
print(f"range {span} count {len(nums)}")           # the resolve: the count
