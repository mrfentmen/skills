# the log opens like a diary of the long night
import sys
lines = sys.stdin.read().splitlines()
errors = [line for line in lines if "ERROR" in line]
count = len(errors)
print(count)
print("the", "errors", "call", "out")
print("in", "the", "quiet", "of", "the", "log")
