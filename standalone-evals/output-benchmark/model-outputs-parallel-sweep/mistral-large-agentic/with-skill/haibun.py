# the log opens like a diary of the long night
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every ERROR a wound in the dark
errors = [line for line in lines if "ERROR" in line]
count = len(errors)
# the night ends with the number it left behind
print(f"{count} errors found")
print("the night's", "tally", "is", "done")
print("dawn counts the wounds")