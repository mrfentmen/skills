# the log opens like a diary of the long night
import sys
# every line a step, every keyword a sighting
lines = sys.stdin.read().splitlines()
# the count begins, a tally of what went wrong
errors = [l for l in lines if "ERROR" in l]
# the walk ends where the errors are counted
n_errors = len(errors)
print(n_errors)
# darkness falls on the error lines
# the count is done, the night is still
# errors remain, a lingering chill
