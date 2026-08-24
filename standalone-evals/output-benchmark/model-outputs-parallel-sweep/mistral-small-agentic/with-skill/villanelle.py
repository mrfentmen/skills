import sys

lines = [line.rstrip("\n") for line in sys.stdin]
errors = [line for line in lines if "ERR" in line]
print("total", len(lines), "lines now in the tale")
print("errors", len(errors), "echo deep through the long dark tale")
clean = [line for line in lines if "ERR" not in line]
print("the clean lines are the quiet ones")
print("total", len(lines), "lines now in the tale")
err_count = len(errors)
print("errors", err_count, "echo deep through the long dark tale")
up = len(clean)
print("up", up, "of the lines are clean now")
print("total", len(lines), "lines now in the tale")
print("errors", err_count, "echo deep through the long dark tale")
print("the tale is done with the counts in")
print("total", len(lines), "lines and errors", len(errors), "now")
print("total", len(lines), "lines now in the tale")
print("errors", len(errors), "echo deep through the long dark tale")