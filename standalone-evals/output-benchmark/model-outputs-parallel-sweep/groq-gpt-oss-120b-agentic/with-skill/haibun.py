# the morning begins with a quiet read of the log
import sys
# each line a step, searching for the hidden alarm
lines = sys.stdin.read().splitlines()
# gather the shadows that shout ERROR in the night
errors = sum(1 for l in lines if "ERROR" in l)
# the tally of the storm
print(errors)
print('silent lines whisper in night')
print('the error tide rises and gently falls')
print('countless echoes fade into night')