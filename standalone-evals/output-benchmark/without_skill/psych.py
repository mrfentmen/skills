grid = [[(r + c) % 3 for c in range(4)] for r in range(4)]
for row in grid:
    print("".join(str(cell) for cell in row))
