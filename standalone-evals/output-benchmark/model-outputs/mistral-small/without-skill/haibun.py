import sys

def count_errors_in_log():
    error_count = 0
    for line in sys.stdin:
        if "ERROR" in line:
            error_count += 1
    print(f"Within the log's sprawling scroll, {error_count} lines bear the mark of ERROR—")
    print("a silent tally of the system's woes,")
    print("each one a whisper of a fault below.")

if __name__ == "__main__":
    count_errors_in_log()
