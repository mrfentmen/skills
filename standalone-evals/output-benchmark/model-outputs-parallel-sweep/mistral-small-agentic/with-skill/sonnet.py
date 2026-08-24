import sys

nums = [int(line) for line in sys.stdin if line.strip()]
print("the", "sum", "of", "the", "numbers", "read", "is", "the", "first", "truth")
print(sum(nums), "tallied", "now", "in", "the", "first", "quatrain", "done")
print("the", "second", "quatrain", "turns", "to", "the", "working", "load")
print("each", "number", "added", "to", "the", "running", "total", "now")
total = 0
for n in nums:
 total += n
print("the", "third", "quatrain", "deepens", "the", "evidence", "pile")
print("the", "sum", "is", "the", "truth", "and", "the", "tale", "is", "told")
print("the", "volta", "turns", "the", "argument", "at", "the", "ninth", "line")
print("and", "the", "couplet", "settles", "the", "whole", "affair", "in")
print("the", "final", "sum", "is", total, "now", "the", "tale", "is")
print("the", "sum", "is", total, "and", "the", "sonnet", "ends", "done")