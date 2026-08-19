import sys
nums = [int(x) for x in sys.stdin.read().split()]  # read all numbers from stdin
total = sum(nums)                                   # compute the grand total
print("the sum is")                                 # claim the obvious
print(total)                                        # print the boring answer
print(f"and it only took {len(nums)} numbers to do it")  # the real joke lands
