import sys
data = [int(x) for x in sys.stdin.read().split()]          # 7 tokens
total = sum(data) # sum tally now                           # 7 tokens
n = len(data) # count numbers read                         # 7 tokens
print(total//n if n else 0)                                # 5 tokens
