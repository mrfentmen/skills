import sys

# the log arrives like a slow dawn
lines = sys.stdin.read().splitlines()
# every line a whisper, some shout ERROR
errors = [l for l in lines if "ERROR" in l]
# the count: what the night left behind
n = len(errors)
print('the errors call out')
print('the night holds')
print(n)