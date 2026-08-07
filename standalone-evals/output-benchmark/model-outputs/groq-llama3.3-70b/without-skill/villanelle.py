import sys

def read_lines():
    lines = sys.stdin.readlines()
    error_lines = [line for line in lines if 'error' in line.lower()]
    return lines, error_lines

def villanelle(lines, error_lines):
    total_lines = len(lines)
    error_count = len(error_lines)
    refrain1 = f"In {total_lines} lines, a tale is spun"
    refrain2 = f"With {error_count} errors, the story's undone"
    poem = [
        "In the depths of code, a story's told",
        refrain1,
        "Of loops and functions, young and old",
        refrain2,
        "The programmer's art, a delicate hold",
        refrain1,
        "With each line written, a dream takes gold",
        refrain2,
        "But errors creep, like thieves in the cold",
        refrain1,
        "And crash the program, with a fatal fold",
        refrain2,
        "The coder's quest, to debug and mold",
        refrain1,
        "The perfect code, a symphony to behold",
        refrain2,
        "With every fix, a story's retold",
        refrain1,
        "And in the end, a masterpiece to hold",
        refrain2,
        "The villanelle's refrain, a story's been told",
        refrain1,
        refrain2
    ]
    return '\n'.join(poem)

lines, error_lines = read_lines()
print(villanelle(lines, error_lines))
