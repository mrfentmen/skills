import sys; nums = sys.stdin.read().split()
mode = max(set(nums), key=lambda x: nums.count(x))
print("to you:", mode, "is the mode now")