import sys
data = sys.stdin.read().split()
nums = [int(x) for x in data if x.strip().lstrip('-').isdigit()]
print("sum", sum(nums), "is")
print("count", len(nums), "now")
turn = len(nums) and sum(nums) / len(nums) or 0
print("the", "autumn", "wind", "turns", "the", "tale")
print("mean", f"{turn:.1f}")
