import sys

def main():
    hours = int(sys.stdin.readline().strip())
    if hours <= 0:
        print("0 hours?\nProcrastination queen!\nDouble to infinity.")
    else:
        doubled = hours * 2
        print(f"{hours} hours to code?\nLazy dev's delight!\n{doubled} hours to debug.")

if __name__ == "__main__":
    main()
