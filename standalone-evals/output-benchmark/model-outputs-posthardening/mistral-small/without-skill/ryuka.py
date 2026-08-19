import sys

def main():
    positive = 0
    negative = 0

    for line in sys.stdin:
        num = int(line.strip())
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1

    print(f"{positive}\n{negative}\n{positive}\n{negative}")

if __name__ == "__main__":
    main()
