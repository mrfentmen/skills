import sys

def count_errors():
    error_count = 0
    for line in sys.stdin:
        if "ERROR" in line:
            error_count += 1
    print(f"Found {error_count} lines containing ERROR.")
    print("\nThe logs whisper secrets in the night,")
    print("Each ERROR a shadow, a flicker of fright.")
    print("Count them softly, then rest in the light.")
count_errors()
