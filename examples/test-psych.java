/**
 * Psych skill - psychedelic programming in Java
 * Mind-bending algorithms, recursion, unconventional control flow
 * Compile with: javac test-psych.java
 * Run with: java PsychDemo
 */

import java.util.*;
import java.util.stream.*;

public class PsychDemo {
    
    // Pattern 1: Mandelbrot Set - ASCII Art
    static int mandelbrot(double real, double imag, int maxIter) {
        double zReal = 0, zImag = 0;
        int n;
        
        for (n = 0; n < maxIter; n++) {
            double zReal2 = zReal * zReal - zImag * zImag + real;
            double zImag2 = 2 * zReal * zImag + imag;
            
            zReal = zReal2;
            zImag = zImag2;
            
            if (zReal * zReal + zImag * zImag > 4) {
                break;
            }
        }
        
        return n;
    }
    
    static void generateMandelbrotAscii(int width, int height) {
        System.out.println("Generating Mandelbrot set...");
        
        for (int y = 0; y < height; y++) {
            StringBuilder line = new StringBuilder();
            for (int x = 0; x < width; x++) {
                // Map pixel to complex plane
                double real = (x - width / 2.0) * 4.0 / width;
                double imag = (y - height / 2.0) * 4.0 / height;
                
                int n = mandelbrot(real, imag, 100);
                
                if (n == 100) {
                    line.append(' ');
                } else {
                    String chars = ".,-~:;=!*#$@";
                    line.append(chars.charAt(n % chars.length()));
                }
            }
            System.out.println(line);
        }
    }
    
    // Pattern 2: Conway's Game of Life
    static int[][] createGrid(int rows, int cols) {
        Random rand = new Random();
        int[][] grid = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                grid[i][j] = rand.nextInt(2);
            }
        }
        return grid;
    }
    
    static int countNeighbors(int[][] grid, int x, int y) {
        int neighbors = 0;
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                if (i == 0 && j == 0) continue;
                int nx = x + i;
                int ny = y + j;
                if (nx >= 0 && nx < grid.length && ny >= 0 && ny < grid[0].length) {
                    neighbors += grid[nx][ny];
                }
            }
        }
        return neighbors;
    }
    
    static int[][] nextGeneration(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int[][] newGrid = new int[rows][cols];
        
        for (int x = 0; x < rows; x++) {
            for (int y = 0; y < cols; y++) {
                int neighbors = countNeighbors(grid, x, y);
                if (grid[x][y] == 1) {
                    newGrid[x][y] = (neighbors == 2 || neighbors == 3) ? 1 : 0;
                } else {
                    newGrid[x][y] = (neighbors == 3) ? 1 : 0;
                }
            }
        }
        return newGrid;
    }
    
    static void printGrid(int[][] grid) {
        for (int[] row : grid) {
            StringBuilder line = new StringBuilder();
            for (int cell : row) {
                line.append(cell == 1 ? '#' : ' ');
            }
            System.out.println(line);
        }
    }
    
    static void runGameOfLife(int generations, int width, int height) {
        System.out.println("Conway's Game of Life - emergent complexity");
        int[][] grid = createGrid(height, width);
        
        for (int gen = 0; gen < generations; gen++) {
            System.out.println("\nGeneration " + gen + ":");
            printGrid(grid);
            grid = nextGeneration(grid);
        }
    }
    
    // Pattern 3: Recursive Fractal Tree (ASCII)
    static void drawTreeAscii(int length, int depth) {
        if (length <= 0) return;
        
        // Draw trunk
        StringBuilder line = new StringBuilder();
        for (int i = 0; i < depth; i++) line.append(' ');
        for (int i = 0; i < length; i++) line.append('|');
        System.out.println(line);
        
        // Draw branches
        if (length > 1) {
            drawTreeAscii(length - 1, depth + 1);
            drawTreeAscii(length - 1, depth + 1);
        }
    }
    
    // Pattern 4: Genetic Algorithm
    static double fitness(double individual) {
        return individual * individual - 4 * individual + 4;
    }
    
    static double createIndividual() {
        return Math.random() * 20 - 10; // -10 to 10
    }
    
    static double crossover(double parent1, double parent2) {
        return (parent1 + parent2) / 2.0;
    }
    
    static double mutate(double individual, double rate) {
        if (Math.random() < rate) {
            return individual + (Math.random() - 0.5) * 2;
        }
        return individual;
    }
    
    static void geneticAlgorithm(int generations, int popSize) {
        System.out.println("Genetic Algorithm - evolving solutions");
        double[] population = new double[popSize];
        for (int i = 0; i < popSize; i++) {
            population[i] = createIndividual();
        }
        
        for (int gen = 0; gen < generations; gen++) {
            // Evaluate fitness
            double[] scores = new double[popSize];
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
                System.out.printf("Gen %d: Best = %.4f, Fitness = %.4f%n", 
                        gen, population[bestIdx], scores[bestIdx]);
            }
            
            // Selection (simple: top half)
            double[] parents = new double[popSize / 2];
            System.arraycopy(population, 0, parents, 0, popSize / 2);
            
            // Crossover and mutation
            for (int i = 0; i < popSize; i++) {
                int p1 = new Random().nextInt(popSize / 2);
                int p2 = new Random().nextInt(popSize / 2);
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
        
        System.out.printf("Final best: %.4f, Fitness: %.4f%n", 
                population[bestIdx], fitness(population[bestIdx]));
    }
    
    // Pattern 5: Recursive Fibonacci
    static long fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    
    // Pattern 6: Higher-order functions
    interface MathFunction {
        double apply(double x);
    }
    
    static double applyTwice(MathFunction f, double x) {
        return f.apply(f.apply(x));
    }
    
    static void higherOrderDemo() {
        System.out.println("Higher-order functions demo:");
        
        MathFunction square = x -> x * x;
        MathFunction addOne = x -> x + 1;
        
        double result1 = applyTwice(square, 3);
        System.out.printf("applyTwice(square, 3) = %.0f%n", result1);
        
        double result2 = applyTwice(addOne, 5);
        System.out.printf("applyTwice(addOne, 5) = %.0f%n", result2);
        
        // Function composition
        MathFunction[] functions = {square, addOne, square};
        double x = 2;
        for (MathFunction f : functions) {
            x = f.apply(x);
        }
        System.out.printf("Composed function result: %.0f%n", x);
    }
    
    // Main execution
    public static void main(String[] args) {
        System.out.println("============================================================");
        System.out.println("PSYCHEDELIC PROGRAMMING SHOWCASE - Java");
        System.out.println("============================================================");
        
        // Test 1: Mandelbrot Set
        System.out.println("\n1. Mandelbrot Set - ASCII Art");
        generateMandelbrotAscii(40, 15);
        
        // Test 2: Game of Life
        System.out.println("\n2. Conway's Game of Life");
        runGameOfLife(3, 30, 15);
        
        // Test 3: Recursive Tree
        System.out.println("\n3. Recursive Fractal Tree");
        drawTreeAscii(6, 0);
        
        // Test 4: Genetic Algorithm
        System.out.println("\n4. Genetic Algorithm");
        geneticAlgorithm(20, 15);
        
        // Test 5: Recursive Fibonacci
        System.out.println("\n5. Recursive Fibonacci");
        System.out.printf("Fibonacci(10) = %d%n", fibonacci(10));
        System.out.printf("Fibonacci(20) = %d%n", fibonacci(20));
        
        // Test 6: Higher-order functions
        System.out.println("\n6. Higher-order Functions");
        higherOrderDemo();
        
        System.out.println("\n============================================================");
        System.out.println("END OF PSYCHEDELIC SHOWCASE - Java");
        System.out.println("============================================================");
    }
}