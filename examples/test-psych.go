/**
 * Psych skill - psychedelic programming in Go
 * Mind-bending algorithms, recursion, unconventional control flow
 * Run with: go run test-psych.go
 */

package main

import (
	"fmt"
	"math"
	"math/rand"
	"strings"
	"time"
)

// Pattern 1: Mandelbrot Set - ASCII Art
func mandelbrot(real, imag float64, maxIter int) int {
	zReal, zImag := 0.0, 0.0
	
	for n := 0; n < maxIter; n++ {
		zReal2 := zReal*zReal - zImag*zImag + real
		zImag2 := 2*zReal*zImag + imag
		
		zReal, zImag = zReal2, zImag2
		
		if zReal*zReal + zImag*zImag > 4 {
			return n
		}
	}
	
	return maxIter
}

func generateMandelbrotAscii(width, height int) {
	fmt.Println("Generating Mandelbrot set...")
	
	chars := ".,-~:;=!*#$@"
	
	for y := 0; y < height; y++ {
		line := ""
		for x := 0; x < width; x++ {
			// Map pixel to complex plane
			real := (float64(x) - float64(width)/2.0) * 4.0 / float64(width)
			imag := (float64(y) - float64(height)/2.0) * 4.0 / float64(height)
			
			n := mandelbrot(real, imag, 100)
			
			if n == 100 {
				line += " "
			} else {
				line += string(chars[n%len(chars)])
			}
		}
		fmt.Println(line)
	}
}

// Pattern 2: Conway's Game of Life
func createGrid(rows, cols int) [][]int {
	grid := make([][]int, rows)
	for i := range grid {
		grid[i] = make([]int, cols)
		for j := range grid[i] {
			grid[i][j] = rand.Intn(2)
		}
	}
	return grid
}

func countNeighbors(grid [][]int, x, y int) int {
	neighbors := 0
	for i := -1; i <= 1; i++ {
		for j := -1; j <= 1; j++ {
			if i == 0 && j == 0 {
				continue
			}
			nx, ny := x+i, y+j
			if nx >= 0 && nx < len(grid) && ny >= 0 && ny < len(grid[0]) {
				neighbors += grid[nx][ny]
			}
		}
	}
	return neighbors
}

func nextGeneration(grid [][]int) [][]int {
	rows := len(grid)
	cols := len(grid[0])
	newGrid := make([][]int, rows)
	
	for i := range newGrid {
		newGrid[i] = make([]int, cols)
	}
	
	for x := 0; x < rows; x++ {
		for y := 0; y < cols; y++ {
			neighbors := countNeighbors(grid, x, y)
			if grid[x][y] == 1 {
				if neighbors == 2 || neighbors == 3 {
					newGrid[x][y] = 1
				}
			} else {
				if neighbors == 3 {
					newGrid[x][y] = 1
				}
			}
		}
	}
	return newGrid
}

func printGrid(grid [][]int) {
	for _, row := range grid {
		line := ""
		for _, cell := range row {
			if cell == 1 {
				line += "#"
			} else {
				line += " "
			}
		}
		fmt.Println(line)
	}
}

func runGameOfLife(generations, width, height int) {
	fmt.Println("Conway's Game of Life - emergent complexity")
	grid := createGrid(height, width)
	
	for gen := 0; gen < generations; gen++ {
		fmt.Printf("\nGeneration %d:\n", gen)
		printGrid(grid)
		grid = nextGeneration(grid)
	}
}

// Pattern 3: Recursive Fractal Tree (ASCII)
func drawTreeAscii(length, depth int) {
	if length <= 0 {
		return
	}
	
	// Draw trunk
	line := strings.Repeat(" ", depth) + strings.Repeat("|", length)
	fmt.Println(line)
	
	// Draw branches
	if length > 1 {
		drawTreeAscii(length-1, depth+1)
		drawTreeAscii(length-1, depth+1)
	}
}

// Pattern 4: Genetic Algorithm
func fitness(individual float64) float64 {
	return individual*individual - 4*individual + 4
}

func createIndividual() float64 {
	return rand.Float64()*20 - 10 // -10 to 10
}

func crossover(parent1, parent2 float64) float64 {
	return (parent1 + parent2) / 2
}

func mutate(individual, rate float64) float64 {
	if rand.Float64() < rate {
		return individual + (rand.Float64()-0.5)*2
	}
	return individual
}

func geneticAlgorithm(generations, popSize int) {
	fmt.Println("Genetic Algorithm - evolving solutions")
	population := make([]float64, popSize)
	for i := range population {
		population[i] = createIndividual()
	}
	
	for gen := 0; gen < generations; gen++ {
		// Evaluate fitness
		scores := make([]float64, popSize)
		for i, ind := range population {
			scores[i] = fitness(ind)
		}
		
		// Find best
		bestIdx := 0
		for i := 1; i < popSize; i++ {
			if scores[i] > scores[bestIdx] {
				bestIdx = i
			}
		}
		
		if gen%10 == 0 {
			fmt.Printf("Gen %d: Best = %.4f, Fitness = %.4f\n", 
					gen, population[bestIdx], scores[bestIdx])
		}
		
		// Selection (simple: top half)
		parents := make([]float64, popSize/2)
		copy(parents, population[:popSize/2])
		
		// Crossover and mutation
		for i := 0; i < popSize; i++ {
			p1 := parents[rand.Intn(len(parents))]
			p2 := parents[rand.Intn(len(parents))]
			population[i] = crossover(p1, p2)
			population[i] = mutate(population[i], 0.1)
		}
	}
	
	// Find final best
	bestIdx := 0
	for i := 1; i < popSize; i++ {
		if fitness(population[i]) > fitness(population[bestIdx]) {
			bestIdx = i
		}
	}
	
	fmt.Printf("Final best: %.4f, Fitness: %.4f\n", 
			population[bestIdx], fitness(population[bestIdx]))
}

// Pattern 5: Recursive Fibonacci
func fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

// Pattern 6: Higher-order functions
func applyTwice(f func(float64) float64, x float64) float64 {
	return f(f(x))
}

func higherOrderDemo() {
	fmt.Println("Higher-order functions demo:")
	
	square := func(x float64) float64 { return x * x }
	addOne := func(x float64) float64 { return x + 1 }
	
	result1 := applyTwice(square, 3)
	fmt.Printf("applyTwice(square, 3) = %.0f\n", result1)
	
	result2 := applyTwice(addOne, 5)
	fmt.Printf("applyTwice(addOne, 5) = %.0f\n", result2)
	
	// Function composition
	functions := []func(float64) float64{square, addOne, square}
	x := 2.0
	for _, f := range functions {
		x = f(x)
	}
	fmt.Printf("Composed function result: %.0f\n", x)
}

// Pattern 7: Bitwise operations for psychedelic patterns
func bitwisePatterns() {
	fmt.Println("Bitwise psychedelic patterns:")
	
	for i := 0; i < 8; i++ {
		line := ""
		for j := 0; j < 8; j++ {
			if (i^j)&1 == 1 {
				line += "#"
			} else {
				line += " "
			}
		}
		fmt.Println(line)
	}
}

// Main execution
func main() {
	rand.Seed(time.Now().UnixNano())
	
	fmt.Println("============================================================")
	fmt.Println("PSYCHEDELIC PROGRAMMING SHOWCASE - Go")
	fmt.Println("============================================================")
	
	// Test 1: Mandelbrot Set
	fmt.Println("\n1. Mandelbrot Set - ASCII Art")
	generateMandelbrotAscii(40, 15)
	
	// Test 2: Game of Life
	fmt.Println("\n2. Conway's Game of Life")
	runGameOfLife(3, 30, 15)
	
	// Test 3: Recursive Tree
	fmt.Println("\n3. Recursive Fractal Tree")
	drawTreeAscii(6, 0)
	
	// Test 4: Genetic Algorithm
	fmt.Println("\n4. Genetic Algorithm")
	geneticAlgorithm(20, 15)
	
	// Test 5: Recursive Fibonacci
	fmt.Println("\n5. Recursive Fibonacci")
	fmt.Printf("Fibonacci(10) = %d\n", fibonacci(10))
	fmt.Printf("Fibonacci(20) = %d\n", fibonacci(20))
	
	// Test 6: Higher-order functions
	fmt.Println("\n6. Higher-order Functions")
	higherOrderDemo()
	
	// Test 7: Bitwise patterns
	fmt.Println("\n7. Bitwise Psychedelic Patterns")
	bitwisePatterns()
	
	fmt.Println("\n============================================================")
	fmt.Println("END OF PSYCHEDELIC SHOWCASE - Go")
	fmt.Println("============================================================")
}