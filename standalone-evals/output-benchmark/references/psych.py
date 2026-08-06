# feedback of color, a tiny living grid
size = 4
for step in range(2):
    grid = [[(row + col + step) % 3 for col in range(size)] for row in range(size)]
    for row in grid:
        print("".join("#*+"[cell] for cell in row))
    print("---")
