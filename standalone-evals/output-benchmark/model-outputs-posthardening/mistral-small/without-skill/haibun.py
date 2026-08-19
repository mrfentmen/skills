import sys

def count_errors_in_log():
    error_count = 0
    for line in sys.stdin:
        if "ERROR" in line:
            error_count += 1
    print(f"The log contains {error_count} lines with ERROR.")
    print("\nA silent scream in logs so vast,")
    print("Each ERROR blooms—a shadow cast.")
    print("The count is tallied, shadows passed.")
count_errors_in_log()
