import sys
data = sys.stdin.read().split()
nums = [float(x) for x in data if x]
total = sum(nums)
count = len(nums)
print(total, count)
print("the", "third", "line", "turns", "the", "tale", "and")
print("the", "fourth", "resolves", "the", "whole", "affair")