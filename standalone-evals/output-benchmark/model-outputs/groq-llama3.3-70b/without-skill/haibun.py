import sys

def count_errors(log):
    error_count = 0
    for line in log:
        if 'ERROR' in line:
            error_count += 1
    return error_count

log = sys.stdin.readlines()
error_count = count_errors(log)

print(f"After reviewing the log, it became clear that errors were a significant issue. The log contained {error_count} lines with the word ERROR, a stark reminder of the problems that needed to be addressed. As the review came to a close, the true extent of the errors became apparent, and it was time to take action to prevent such issues in the future.")

print("Errors abound, a troubling sight")
print("Correcting them, our guiding light")
print("Code perfected, all is right")
