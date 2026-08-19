# the log opens like a diary of the long night
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every word a whisper
errors = [line for line in lines if "ERROR" in line]
count = len(errors)
# the night ends with the number it left behind
print("the errors call out")
print(f"{count} cries in the dark")
print("dawn counts them")