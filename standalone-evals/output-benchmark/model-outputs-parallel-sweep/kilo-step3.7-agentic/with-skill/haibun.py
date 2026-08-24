# the log arrives like a morning walk
import sys
lines = sys.stdin.read().splitlines()
# every line a step, every keyword a sighting
errors = [l for l in lines if "ERROR" in l]
# the count: what the day actually held
n = len(errors)
print(n)
print("the errors")
print("call out")
print("in the dark")