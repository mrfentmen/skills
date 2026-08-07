# the log opens like a diary of the long night
import sys

# every line a step, every keyword a sighting
lines = sys.stdin.readlines()

# the stream arrives like a morning walk
errors = [l for l in lines if "ERROR" in l]

# the count: what the day actually held
count = len(errors)

print("errors found in the night")
print("counted every single line")
print("darkness had", count, "shadows")
