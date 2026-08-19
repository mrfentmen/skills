import sys

def main():
    data = sys.stdin.read().strip().split()
    nums = [int(x) for x in data] if data else []
    total = sum(nums)
    cnt = len(nums)
    # Alternating-line choka form with a closing couplet
    print(total)
    print(cnt)
    print(total)
    print(cnt)

if __name__ == "__main__":
    main()
