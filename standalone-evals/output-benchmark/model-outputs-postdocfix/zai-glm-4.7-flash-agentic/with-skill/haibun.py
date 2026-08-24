# the log opens like a diary of the long night
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every keyword a sighting
errors = [line for line in lines if "ERROR" in line]
# the count: what the day actually held
print(len(errors))
print('the errors call out')
print('in the night')