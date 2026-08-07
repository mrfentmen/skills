import sys

def main():
    lines = [line.rstrip('\n') for line in sys.stdin]
    total_lines = len(lines)
    error_lines = 0

    if total_lines != 19:
        error_lines += 1

    if total_lines >= 1:
        refrain1 = lines[0]
        refrain2 = lines[1]
        expected_refrain_positions = [0, 1, 6, 12, 18]
        for i in expected_refrain_positions:
            if i < total_lines:
                if lines[i] != refrain1 and lines[i] != refrain2:
                    error_lines += 1
            else:
                error_lines += 1

    print(f"{total_lines} {error_lines}")

if __name__ == "__main__":
    main()
