import sys
nums = [int(x) for x in sys.stdin.read().split()]  # read all numbers from stdin
total = sum(nums)                                  # compute the grand total
print("the", "sum", "is")                         # claim the punchline is near
print("now", "here", "it", "comes")               # build the suspense
print(f"and the answer is {total}")                # final line: the comic reveal
