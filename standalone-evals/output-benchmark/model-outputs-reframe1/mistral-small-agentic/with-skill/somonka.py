import sys

data = sys.stdin.read().split()
nums = [int(x) for x in data]
count = len(nums)
print("count", count, "numbers arrive")
print("the", "first", "voice", "speaks", "now")
print("five", "seven", "five", "seven", "seven")

total = sum(nums)
print("sum", total, "is", "the", "answer")
print("the", "second", "voice", "replies", "now")

data = sys.stdin.read().split()
nums = [int(x) for x in data]
count = len(nums)
total = sum(nums)
print("sum", total, "and", "the", "count")
print("the", "reply", "is", "complete", "now")
print("the", "sum", "answers", "the", "call")