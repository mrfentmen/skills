# the log arrives like a morning walk
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every word a sighting
errors = [l for l in lines if "ERROR" in l]
# the count: what the day actually held
count = len(errors)
print(count)
# the sun rises on the error count
# the log closes like a quiet night
# the errors rest beneath the line
