# the log arrives like a slow morning walk
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every word a sighting
errors = [l for l in lines if "ERROR" in l]
count = len(errors)
print("the errors call out")
print("through the quiet lines")
print("dawn counts the night")