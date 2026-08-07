import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    total = sum(map(int, data))
    fib_seq = [6, 8]
    while sum(fib_seq) < len(str(total)):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    lines = []
    s = str(total)
    idx = 0
    for count in fib_seq:
        if idx >= len(s):
            break
        lines.append(s[idx:idx+count])
        idx += count
    if idx < len(s):
        lines.append(s[idx:])
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
