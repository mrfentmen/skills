import sys

def main():
    total = 0
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            total += int(stripped)
    s_total = str(total)
    length = len(s_total)
    if length == 0:
        print("0")
        print("0")
        print("0")
    else:
        first_part = s_total[:(length + 2) // 3]
        middle_part = s_total[(length + 2) // 3:(length + 1) // 2]
        last_part = s_total[(length + 1) // 2:]
        print(first_part)
        print(middle_part)
        print(last_part)

if __name__ == "__main__":
    main()
