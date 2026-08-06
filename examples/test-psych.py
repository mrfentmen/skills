#!/usr/bin/env python3
"""
Test of psych skill - Python version
This demonstrates psychedelic programming patterns
"""

import random
import math

# Pattern 1: Mandelbrot Set - infinite complexity from simple rules
def mandelbrot(c, max_iter):
    """Calculate Mandelbrot set membership"""
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot_ascii(width=80, height=40):
    """Generate ASCII art of Mandelbrot set"""
    print("Generating Mandelbrot set...")
    for y in range(height):
        for x in range(width):
            # Map pixel to complex plane
            real = (x - width/2.0) * 4.0/width
            imag = (y - height/2.0) * 4.0/height
            c = complex(real, imag)
            
            # Calculate membership
            m = mandelbrot(c, 100)
            
            # Print character
            if m == 100:
                print(' ', end='')
            else:
                # Use different characters for different escape times
                chars = '.,-~:;=!*#$@'
                print(chars[m % len(chars)], end='')
        print()

# Pattern 2: Conway's Game of Life - emergent complexity
def create_grid(rows, cols):
    """Create random grid"""
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def count_neighbors(grid, x, y):
    """Count live neighbors"""
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                neighbors += grid[nx][ny]
    return neighbors

def next_generation(grid):
    """Calculate next generation"""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1:
                new_grid[x][y] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[x][y] = 1 if neighbors == 3 else 0
    return new_grid

def print_grid(grid):
    """Print grid with ASCII art"""
    for row in grid:
        print(''.join(['█' if cell else ' ' for cell in row]))

def run_game_of_life(generations=10, width=40, height=20):
    """Run Game of Life simulation"""
    print("Conway's Game of Life - emergent complexity")
    grid = create_grid(height, width)
    
    for gen in range(generations):
        print(f"\nGeneration {gen}:")
        print_grid(grid)
        grid = next_generation(grid)

# Pattern 3: Recursive Fractal Tree
def draw_tree_ascii(length, angle, depth=0):
    """Draw ASCII fractal tree recursively"""
    if length <= 0:
        return []
    
    lines = []
    # Draw trunk
    lines.append(' ' * depth + '|' * length)
    
    # Draw branches
    if length > 1:
        left_branch = draw_tree_ascii(length - 1, angle, depth + 1)
        right_branch = draw_tree_ascii(length - 1, angle, depth + 1)
        lines.extend(left_branch)
        lines.extend(right_branch)
    
    return lines

# Pattern 4: Genetic Algorithm
def fitness(individual):
    """Fitness function: maximize x^2 - 4x + 4"""
    return individual**2 - 4*individual + 4

def create_individual():
    """Create random individual"""
    return random.uniform(-10, 10)

def crossover(parent1, parent2):
    """Crossover two parents"""
    return (parent1 + parent2) / 2

def mutate(individual, rate=0.1):
    """Mutate individual"""
    if random.random() < rate:
        return individual + random.gauss(0, 1)
    return individual

def genetic_algorithm(generations=50, pop_size=20):
    """Run genetic algorithm"""
    print("Genetic Algorithm - evolving solutions")
    population = [create_individual() for _ in range(pop_size)]
    
    for gen in range(generations):
        # Evaluate fitness
        scored = [(ind, fitness(ind)) for ind in population]
        scored.sort(key=lambda x: x[1], reverse=True)
        
        # Show best
        if gen % 10 == 0:
            best_ind, best_fit = scored[0]
            print(f"Gen {gen}: Best = {best_ind:.4f}, Fitness = {best_fit:.4f}")
        
        # Selection
        parents = [ind for ind, fit in scored[:pop_size//2]]
        
        # Crossover and mutation
        children = []
        while len(children) < pop_size:
            p1, p2 = random.sample(parents, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            children.append(child)
        
        population = children
    
    # Return best
    best = max(population, key=fitness)
    return best, fitness(best)

# Pattern 5: Quine (self-replicating program)
def quine():
    """Python quine - program that prints itself"""
    s = 's = %r\\nprint(s %% s)'
    print(s % s)

# Pattern 6: Psychedelic color cycling
def color_cycle():
    """Terminal color cycling"""
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    reset = '\033[0m'
    
    print("Psychedelic color cycling:")
    for i in range(30):
        color = colors[i % len(colors)]
        char = '█' * 5
        print(f'{color}{char}{reset}', end=' ')
    print()

# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("PSYCHEDELIC PROGRAMMING SHOWCASE")
    print("=" * 60)
    
    # Test 1: Mandelbrot Set
    print("\n1. Mandelbrot Set - ASCII Art")
    generate_mandelbrot_ascii(60, 20)
    
    # Test 2: Game of Life
    print("\n2. Conway's Game of Life")
    run_game_of_life(5, 30, 15)
    
    # Test 3: Recursive Tree
    print("\n3. Recursive Fractal Tree")
    tree_lines = draw_tree_ascii(8, 30)
    for line in tree_lines[:15]:  # Limit output
        print(line)
    
    # Test 4: Genetic Algorithm
    print("\n4. Genetic Algorithm")
    best_ind, best_fit = genetic_algorithm(30, 20)
    print(f"Final best: {best_ind:.4f}, Fitness: {best_fit:.4f}")
    
    # Test 5: Quine
    print("\n5. Quine (self-replicating program)")
    print("Output:")
    quine()
    
    # Test 6: Color Cycling
    print("\n6. Psychedelic Color Cycling")
    color_cycle()
    
    print("\n" + "=" * 60)
    print("END OF PSYCHEDELIC SHOWCASE")
    print("=" * 60)