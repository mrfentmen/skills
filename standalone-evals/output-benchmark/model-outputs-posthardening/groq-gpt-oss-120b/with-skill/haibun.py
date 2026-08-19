# the morning opens with a log walk
import sys
# each line a step, searching for the red word
lines = sys.stdin.read().splitlines()
# the trail gathers the shadows that shout ERROR
errors = [l for l in lines if "ERROR" in l]
# the count of cries is the result of the walk
print(len(errors))
print("silent stones echo")
print("the night breathes soft in")
print("dawn counts the sighs")
