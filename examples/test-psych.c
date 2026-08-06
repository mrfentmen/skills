/**
 * Psych skill - psychedelic programming in C
 * Mind-bending algorithms, recursion, unconventional control flow
 * Compile with: gcc -o psych test-psych.c -lm
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Pattern 1: Mandelbrot Set - ASCII Art
int mandelbrot(double real, double imag, int maxIter) {
    double z_real = 0, z_imag = 0;
    int n;
    
    for (n = 0; n < maxIter; n++) {
        double z_real2 = z_real * z_real - z_imag * z_imag + real;
        double z_imag2 = 2 * z_real * z_imag + imag;
        
        z_real = z_real2;
        z_imag = z_imag2;
        
        if (z_real * z_real + z_imag * z_imag > 4) {
            break;
        }
    }
    
    return n;
}

void generateMandelbrotAscii(int width, int height) {
    printf("Generating Mandelbrot set...\n");
    
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            // Map pixel to complex plane
            double real = (x - width / 2.0) * 4.0 / width;
            double imag = (y - height / 2.0) * 4.0 / height;
            
            int n = mandelbrot(real, imag, 100);
            
            if (n == 100) {
                printf(" ");
            } else {
                const char chars[] = ".,-~:;=!*#$@";
                printf("%c", chars[n % strlen(chars)]);
            }
        }
        printf("\n");
    }
}

// Pattern 2: Conway's Game of Life
#define ROWS 15
#define COLS 30

void createGrid(int grid[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            grid[i][j] = rand() % 2;
        }
    }
}

int countNeighbors(int grid[ROWS][COLS], int x, int y) {
    int neighbors = 0;
    
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if (i == 0 && j == 0) continue;
            
            int nx = x + i;
            int ny = y + j;
            
            if (nx >= 0 && nx < ROWS && ny >= 0 && ny < COLS) {
                neighbors += grid[nx][ny];
            }
        }
    }
    
    return neighbors;
}

void nextGeneration(int grid[ROWS][COLS], int newGrid[ROWS][COLS]) {
    for (int x = 0; x < ROWS; x++) {
        for (int y = 0; y < COLS; y++) {
            int neighbors = countNeighbors(grid, x, y);
            
            if (grid[x][y] == 1) {
                newGrid[x][y] = (neighbors == 2 || neighbors == 3) ? 1 : 0;
            } else {
                newGrid[x][y] = (neighbors == 3) ? 1 : 0;
            }
        }
    }
}

void printGrid(int grid[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            // Use ASCII characters instead of Unicode
            printf("%c", grid[i][j] ? '#' : ' ');
        }
        printf("\n");
    }
}

void runGameOfLife(int generations) {
    printf("Conway's Game of Life - emergent complexity\n");
    
    int grid[ROWS][COLS];
    int newGrid[ROWS][COLS];
    
    createGrid(grid);
    
    for (int gen = 0; gen < generations; gen++) {
        printf("\nGeneration %d:\n", gen);
        printGrid(grid);
        nextGeneration(grid, newGrid);
        
        // Copy newGrid to grid
        memcpy(grid, newGrid, sizeof(grid));
    }
}

// Pattern 3: Recursive Fractal Tree (ASCII)
void drawTreeAscii(int length, int depth) {
    if (length <= 0) return;
    
    // Draw trunk
    for (int i = 0; i < depth; i++) printf(" ");
    for (int i = 0; i < length; i++) printf("|");
    printf("\n");
    
    // Draw branches
    if (length > 1) {
        drawTreeAscii(length - 1, depth + 1);
        drawTreeAscii(length - 1, depth + 1);
    }
}

// Pattern 4: Genetic Algorithm
double fitness(double individual) {
    return individual * individual - 4 * individual + 4;
}

double createIndividual() {
    return ((double)rand() / RAND_MAX) * 20 - 10; // -10 to 10
}

double crossover(double parent1, double parent2) {
    return (parent1 + parent2) / 2.0;
}

double mutate(double individual, double rate) {
    if ((double)rand() / RAND_MAX < rate) {
        return individual + ((double)rand() / RAND_MAX - 0.5) * 2;
    }
    return individual;
}

void geneticAlgorithm(int generations, int popSize) {
    printf("Genetic Algorithm - evolving solutions\n");
    
    double population[popSize];
    for (int i = 0; i < popSize; i++) {
        population[i] = createIndividual();
    }
    
    for (int gen = 0; gen < generations; gen++) {
        // Evaluate fitness
        double scores[popSize];
        for (int i = 0; i < popSize; i++) {
            scores[i] = fitness(population[i]);
        }
        
        // Find best
        int bestIdx = 0;
        for (int i = 1; i < popSize; i++) {
            if (scores[i] > scores[bestIdx]) {
                bestIdx = i;
            }
        }
        
        if (gen % 10 == 0) {
            printf("Gen %d: Best = %.4f, Fitness = %.4f\n", 
                   gen, population[bestIdx], scores[bestIdx]);
        }
        
        // Selection (simple: top half)
        double parents[popSize / 2];
        for (int i = 0; i < popSize / 2; i++) {
            parents[i] = population[i];
        }
        
        // Crossover and mutation
        for (int i = 0; i < popSize; i++) {
            int p1 = rand() % (popSize / 2);
            int p2 = rand() % (popSize / 2);
            population[i] = crossover(parents[p1], parents[p2]);
            population[i] = mutate(population[i], 0.1);
        }
    }
    
    // Find final best
    int bestIdx = 0;
    for (int i = 1; i < popSize; i++) {
        if (fitness(population[i]) > fitness(population[bestIdx])) {
            bestIdx = i;
        }
    }
    
    printf("Final best: %.4f, Fitness: %.4f\n", 
           population[bestIdx], fitness(population[bestIdx]));
}

// Pattern 5: Recursive Fibonacci
long long fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Pattern 6: Higher-order functions (using function pointers)
typedef double (*MathFunc)(double);

double applyTwice(MathFunc f, double x) {
    return f(f(x));
}

double square(double x) {
    return x * x;
}

double addOne(double x) {
    return x + 1;
}

void higherOrderDemo() {
    printf("Higher-order functions demo:\n");
    
    double result1 = applyTwice(square, 3);
    printf("applyTwice(square, 3) = %.0f\n", result1);
    
    double result2 = applyTwice(addOne, 5);
    printf("applyTwice(addOne, 5) = %.0f\n", result2);
    
    // Function composition
    MathFunc functions[] = {square, addOne, square};
    int numFunctions = sizeof(functions) / sizeof(functions[0]);
    
    double x = 2;
    for (int i = 0; i < numFunctions; i++) {
        x = functions[i](x);
    }
    printf("Composed function result: %.0f\n", x);
}

// Pattern 7: Bitwise operations for psychedelic patterns
void bitwisePatterns() {
    printf("Bitwise psychedelic patterns:\n");
    
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if ((i ^ j) & 1) {
                printf("#");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

// Main execution
int main() {
    printf("============================================================\n");
    printf("PSYCHEDELIC PROGRAMMING SHOWCASE - C\n");
    printf("============================================================\n");
    
    // Test 1: Mandelbrot Set
    printf("\n1. Mandelbrot Set - ASCII Art\n");
    generateMandelbrotAscii(40, 15);
    
    // Test 2: Game of Life
    printf("\n2. Conway's Game of Life\n");
    runGameOfLife(3);
    
    // Test 3: Recursive Tree
    printf("\n3. Recursive Fractal Tree\n");
    drawTreeAscii(6, 0);
    
    // Test 4: Genetic Algorithm
    printf("\n4. Genetic Algorithm\n");
    geneticAlgorithm(20, 15);
    
    // Test 5: Recursive Fibonacci
    printf("\n5. Recursive Fibonacci\n");
    printf("Fibonacci(10) = %lld\n", fibonacci(10));
    printf("Fibonacci(20) = %lld\n", fibonacci(20));
    
    // Test 6: Higher-order functions
    printf("\n6. Higher-order Functions\n");
    higherOrderDemo();
    
    // Test 7: Bitwise patterns
    printf("\n7. Bitwise Psychedelic Patterns\n");
    bitwisePatterns();
    
    printf("\n============================================================\n");
    printf("END OF PSYCHEDELIC SHOWCASE - C\n");
    printf("============================================================\n");
    
    return 0;
}