# the log arrives like a slow dawn
import sys
lines = sys.stdin.read().splitlines()
# each line a step, each word a shadow
errors = [l for l in lines if "ERROR" in l]
# the count: what the night left behind
n = len(errors)
print(n)
# the silence after the storm
# the screen glows with the morning's tally
# only the errors remember the dark