# the stream arrives like a morning walk
import sys
lines = sys.stdin.readlines()
# every line a step, every keyword a sighting
errors = [line for line in lines if "ERROR" in line]
# the count: what the day actually held
print(f"{len(errors)} errors")