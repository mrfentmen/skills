import sys

def main():
    error_count = 0
    for line in sys.stdin:
        if "ERROR" in line:
            error_count += 1
    print(f"Through the silent stream of logs, I traced each line with quiet care,")
    print(f"Where ERROR lurked like shadowed thought, I counted every snare.")
    print(f"{error_count}")

if __name__ == "__main__":
    main()
