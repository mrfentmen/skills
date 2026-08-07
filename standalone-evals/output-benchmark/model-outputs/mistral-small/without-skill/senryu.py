import sys

def main():
    hours = int(sys.stdin.readline().strip())
    if hours <= 0:
        print("0\n0\nTime's up!")
    else:
        doubled = hours * 2
        print(f"Work {hours} hours\nStill not done\nNow {doubled} hours")

if __name__ == "__main__":
    main()
