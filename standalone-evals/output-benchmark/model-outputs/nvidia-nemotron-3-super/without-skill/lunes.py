import sys

def main():
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                total += int(line)
            except ValueError:
                pass
    s = str(total)
    print(s[:5])
    print(s[5:8] if len(s) > 5 else '')
    print(s[8:13] if len(s) > 8 else '')

if __name__ == "__main__":
    main()
