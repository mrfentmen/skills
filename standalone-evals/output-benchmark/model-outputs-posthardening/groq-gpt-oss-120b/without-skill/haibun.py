import sys

def main():
    lines = sys.stdin.read().splitlines()
    error_count = sum(1 for line in lines if "ERROR" in line)

    # Narrative prose body
    print("In the quiet hum of the server's night,")
    print("each line whispered its tale,")
    print(f"and among them, {error_count} shouted 'ERROR', a stark reminder of hidden faults.")
    print()
    print("The count stands as a beacon, guiding the watchful eyes of the keeper.")
    print()

    # Final three-line poetic landing
    print("A glitch in the code,")
    print("Echoes fade into silence,")
    print("Hope rewrites the script.")

if __name__ == "__main__":
    main()
