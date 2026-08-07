import sys
nums = [int(x) for x in sys.stdin.read().split()]
answer = "count " + str(len(nums))
print(answer, "of", "the", "five")
print("the", "question", "is", "the", "count", "now")
print("reply", "with", "the", "sum", "of", "them")

total = sum(nums)
answer = "sum " + str(total)
print(answer, "and", "the", "reply")
print("the", "sum", "of", "the", "count", "is", "here")
print("and", "the", "answer", "is", "the", "sum")
