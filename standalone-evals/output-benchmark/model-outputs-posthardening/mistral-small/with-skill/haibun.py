# the log arrives like a slow dawn
import sys
lines = sys.stdin.read().splitlines()
# each line a step, each word a shadow
errors = [l for l in lines if "ERROR" in l]
# the count: what the night left behind
count = len(errors)
print(count)
# the walk ends where the errors speak
# three lines to say what the scroll held
print("errors whisper through the dark")
print("each one a crack in the quiet")
print("morning counts them all")
