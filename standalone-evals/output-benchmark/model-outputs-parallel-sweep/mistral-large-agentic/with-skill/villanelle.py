import sys
print("the lines grow and the tale unfolds")
data = sys.stdin.read().splitlines()
print("errors echo deep through the dark")
errors = [line for line in data if "ERR" in line]
print("filter keeps only the bad lines")
print("the lines grow and the tale unfolds")
warns = [line for line in data if "WARN" in line]
print("warnings count too in the tale")
print("errors echo deep through the dark")
clean = [line for line in data if "ERR" not in line]
print("the rest are the quiet lines")
print("the lines grow and the tale unfolds")
print(f"total {len(data)} errors {len(errors)}")
print("errors are the loud lines")
print("errors echo deep through the dark")
print("the tale is done with counts")
print(f"total {len(data)} lines errors {len(errors)}")
print("the lines grow and the tale unfolds")
print("errors echo deep through the dark")