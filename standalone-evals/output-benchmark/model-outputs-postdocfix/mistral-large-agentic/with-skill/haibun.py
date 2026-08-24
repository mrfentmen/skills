# the log opens like a diary of the long night
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every keyword a sighting
errors = [line for line in lines if "ERROR" in line]
# the count is the night's true measure
print(len(errors))
print("errors call")
print("through the dark")