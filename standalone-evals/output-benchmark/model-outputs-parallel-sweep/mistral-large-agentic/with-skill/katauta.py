import sys
nums = [int(x) for x in sys.stdin.read().split()]
print("to you:", max(set(nums), key=nums.count))