import sys

def main():
    hours = int(sys.stdin.readline().strip())
    print("Work piles high,")
    print("Yet idle hands make double the")
    print(f"tasks in half the time: {hours * 2}")

if __name__ == "__main__":
    main()
