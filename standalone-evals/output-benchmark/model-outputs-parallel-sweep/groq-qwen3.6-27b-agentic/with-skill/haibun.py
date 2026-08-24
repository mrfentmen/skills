# the night log opens like a diary of the long walk
import sys
# every line a step through the dark records
lines = sys.stdin.read().splitlines()
# the errors call out from the quiet pages
errors = [l for l in lines if "ERROR" in l]
# the count: what the night actually held
n = len(errors)
print("errors found:", n)
# the walk ends at dawn
print("the errors call out now")
print("from the dark pages of the night")
print("dawn counts them all now")