# the log opens like a diary of the long night
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every keyword a sighting
errors = [l for l in lines if "ERROR" in l]
# the count: what the day actually held
n_errors = len(errors)
n_total = len(lines)
print(f"{n_errors} errors of {n_total} lines")
# the moon counts the night's mistakes
# the dawn forgets the tally
# only the log remembers
