import sys

def main():
    # Read all words from stdin, split by any whitespace
    words = sys.stdin.read().split()
    
    # Desired pattern lengths for the five lines
    pattern = [2, 4, 6, 8, 2]
    
    idx = 0
    for count in pattern:
        line_words = words[idx:idx + count]
        # If there are not enough words, just use what we have
        print(' '.join(line_words))
        idx += count
        if idx >= len(words):
            # No more words left; remaining lines will be empty
            # Continue printing empty lines for the rest of the pattern
            for remaining in pattern[pattern.index(count)+1:]:
                print()
            break

if __name__ == "__main__":
    main()
