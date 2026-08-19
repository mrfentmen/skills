import sys

def main():
    data = sys.stdin.read().strip().split()
    total = sum(map(int, data)) if data else 0

    print("I added the numbers you supplied")
    print("Their total came out quite a surprise")
    print("We counted each one")
    print("And added them all up")
    print(f"The sum is {total}, go buy a pie")

if __name__ == "__main__":
    main()
