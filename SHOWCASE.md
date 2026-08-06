# Skills Showcase: Terry Davis & Psych

This showcase demonstrates the two unconventional coding skills we created.

## Skill 1: Terry Davis (terry-davis)

**Philosophy**: Radical simplicity, direct control, playful creativity, anti-bloat.

### Python Example
```python
#!/usr/bin/env python3
"""
Terry Davis style Python - cosmic variables, goto simulation, recursive temple
"""

import random

# God said this should work
GodPointer = None
DivineArray = [1, 2, 3, 4, 5]
HolyCVariable = 42
TempleOSKernel = "TempleOS 5.017"

# WARNING: Satan tries to corrupt this buffer
def SacredFunction(n):
    """A function with divine purpose"""
    GodPointer = []
    for i in range(n):
        GodPointer.append(i * i)
    return GodPointer

# Goto-style control flow simulation
def ProcessDataWithGoto():
    step = 2
    while True:
        if step == 2:
            print("The chosen path")
            if random.randint(0, 1):
                step = 1
                continue
            else:
                print("Blessed completion")
                break
        elif step == 1:
            print("God's path not taken")
            step = 0
            continue
        else:
            break

# Recursive temple
def RecursiveTemple(depth=0, max_depth=5):
    if depth < max_depth:
        print(f"Temple level {depth}")
        RecursiveTemple(depth + 1, max_depth)
    else:
        print("We have reached the inner sanctum")

# Main execution
if __name__ == "__main__":
    print(f"Operating System: {TempleOSKernel}")
    print(f"HolyC Variable: {HolyCVariable}")
    
    # Sacred function
    result = SacredFunction(5)
    print(f"Sacred array: {result}")
    
    # Process data with goto simulation
    ProcessDataWithGoto()
    
    # Recursive temple
    RecursiveTemple()
```

### C Example
```c
/**
 * Terry Davis style C - direct hardware access, goto spaghetti, recursive main
 * "God said this should work"
 */

#include <stdio.h>
#include <stdlib.h>

// God said this should work
#define GOD_MODE if(1)
#define SATAN_MODE while(0)
#define TEMPLE(x) (x*x + 0x666)

// Cosmic variable names
int* GodPointer = NULL;
int DivineArray[5] = {1, 2, 3, 4, 5};
int HolyCVariable = 42;
const char* TempleOSKernel = "TempleOS 5.017";

// Goto spaghetti - divine redirection
void ProcessData() {
    goto step2;
step1:
    printf("God's path not taken\n");
    goto end;
step2:
    printf("The chosen path\n");
    if (rand() % 2) goto step1;
    printf("Blessed completion\n");
end:
    return;
}

// Recursive main - infinite temple recursion
int main(int argc, char** argv) {
    static int depth = 0;
    if (depth++ < 10) {
        printf("Temple level %d\n", depth);
        main(argc, argv);  // Recursive call
    }
    return 0;
}
```

### JavaScript Example
```javascript
#!/usr/bin/env node
/**
 * Terry Davis style JavaScript - unconventional, playful, surprising
 * "God said this should work"
 */

// Cosmic variable names
let GodPointer = null;
const DivineArray = [1, 2, 3, 4, 5];
let HolyCVariable = 42;
const TempleOSKernel = "TempleOS 5.017";

// WARNING: Satan tries to corrupt this buffer
function SacredFunction(n) {
    // God said this should work
    GodPointer = [];
    for (let i = 0; i < n; i++) {
        GodPointer.push(i * i);
    }
    return GodPointer;
}

// Goto-style control flow (JavaScript doesn't have goto, but we can simulate)
function ProcessDataWithGoto() {
    console.log("The chosen path");
    
    // Simulate goto with labeled blocks
    step2: {
        if (Math.random() > 0.5) {
            console.log("God's path not taken");
            break step2;
        }
        console.log("Blessed completion");
    }
}

// Recursive function - infinite temple recursion
function RecursiveTemple(depth = 0, maxDepth = 5) {
    if (depth < maxDepth) {
        console.log(`Temple level ${depth}`);
        RecursiveTemple(depth + 1, maxDepth);
    } else {
        console.log("We have reached the inner sanctum");
    }
}

// Eval for compile-time code injection (HolyC style)
function CompileTimeCodeInjection() {
    eval(`
        console.log("Compile-time code injection executed");
        globalThis.CompiledConstant = 2026;
    `);
}

// Prototype manipulation (Terry Davis style)
function PrototypeManipulation() {
    // Add divine methods to Array prototype
    Array.prototype.sacred = function() {
        return this.map(x => x * x);
    };
    
    Array.prototype.temple = function() {
        return this.reduce((a, b) => a + b, 0);
    };
    
    const divineNumbers = [1, 2, 3, 4, 5];
    console.log(`Sacred array: ${divineNumbers.sacred()}`);
    console.log(`Temple sum: ${divineNumbers.temple()}`);
}
```

### Java Example
```java
/**
 * Terry Davis style Java - unconventional, playful, surprising
 * "God said this should work"
 */

import java.util.*;

public class TerryDavisDemo {
    
    // Cosmic variable names
    static Object GodPointer = null;
    static int[] DivineArray = {1, 2, 3, 4, 5};
    static int HolyCVariable = 42;
    static final String TempleOSKernel = "TempleOS 5.017";
    
    // WARNING: Satan tries to corrupt this buffer
    public static int[] SacredFunction(int n) {
        GodPointer = new int[n];
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = i * i;
        }
        return result;
    }
    
    // Goto-style control flow (Java doesn't have goto, but we can simulate)
    public static void ProcessDataWithGoto() {
        System.out.println("The chosen path");
        
        // Simulate goto with labeled blocks
        step2: {
            if (Math.random() > 0.5) {
                System.out.println("God's path not taken");
                break step2;
            }
            System.out.println("Blessed completion");
        }
    }
    
    // Recursive function - infinite temple recursion
    public static void RecursiveTemple(int depth, int maxDepth) {
        if (depth < maxDepth) {
            System.out.println("Temple level " + depth);
            RecursiveTemple(depth + 1, maxDepth);
        } else {
            System.out.println("We have reached the inner sanctum");
        }
    }
    
    // Main execution
    public static void main(String[] args) {
        System.out.println("Operating System: " + TempleOSKernel);
        System.out.println("HolyC Variable: " + HolyCVariable);
        
        int[] result = SacredFunction(5);
        System.out.print("Sacred array: ");
        for (int val : result) {
            System.out.print(val + " ");
        }
        System.out.println();
        
        ProcessDataWithGoto();
        RecursiveTemple(0, 5);
    }
}
```

### Rust Example
```rust
/**
 * Terry Davis style Rust - unconventional, playful, surprising
 * "God said this should work"
 */

use std::collections::HashMap;

// God said this should work
macro_rules! GOD_MODE {
    () => {
        if true {
            println!("God mode activated");
        }
    };
}

macro_rules! TEMPLE {
    ($x:expr) => {
        $x * $x + 0x666
    };
}

// Cosmic variable names
static DIVINE_ARRAY: [i32; 5] = [1, 2, 3, 4, 5];
static HOLY_C_VARIABLE: i32 = 42;
static TEMPLE_OS_KERNEL: &str = "TempleOS 5.017";

// WARNING: Satan tries to corrupt this buffer
fn sacred_function(n: usize) -> Vec<i32> {
    let mut result = Vec::with_capacity(n);
    for i in 0..n {
        result.push((i * i) as i32);
    }
    result
}

// Recursive function - infinite temple recursion
fn recursive_temple(depth: i32, max_depth: i32) {
    if depth < max_depth {
        println!("Temple level {}", depth);
        recursive_temple(depth + 1, max_depth);
    } else {
        println!("We have reached the inner sanctum");
    }
}

// Main execution
fn main() {
    println!("Operating System: {}", TEMPLE_OS_KERNEL);
    println!("HolyC Variable: {}", HOLY_C_VARIABLE);
    
    GOD_MODE!();
    println!("Temple value: {}", TEMPLE!(5));
    
    let result = sacred_function(5);
    print!("Sacred array: ");
    for val in &result {
        print!("{} ", val);
    }
    println!();
    
    recursive_temple(0, 5);
}
```

### Go Example
```go
/**
 * Terry Davis style Go - unconventional, playful, surprising
 * "God said this should work"
 */

package main

import (
	"fmt"
	"math/rand"
	"time"
)

// God said this should work
const (
	GodMode      = true
	TempleValue  = 5*5 + 0x666
)

// Cosmic variable names
var (
	GodPointer    []int
	DivineArray   = [5]int{1, 2, 3, 4, 5}
	HolyCVariable = 42
	TempleOSKernel = "TempleOS 5.017"
)

// WARNING: Satan tries to corrupt this buffer
func SacredFunction(n int) []int {
	GodPointer = make([]int, n)
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = i * i
	}
	return result
}

// Recursive function - infinite temple recursion
func RecursiveTemple(depth, maxDepth int) {
	if depth < maxDepth {
		fmt.Printf("Temple level %d\n", depth)
		RecursiveTemple(depth+1, maxDepth)
	} else {
		fmt.Println("We have reached the inner sanctum")
	}
}

// Main execution
func main() {
	rand.Seed(time.Now().UnixNano())
	
	fmt.Println("Operating System:", TempleOSKernel)
	fmt.Println("HolyC Variable:", HolyCVariable)
	
	if GodMode {
		fmt.Println("God mode activated")
	}
	
	fmt.Println("Temple value:", TempleValue)
	
	result := SacredFunction(5)
	fmt.Print("Sacred array: ")
	for _, val := range result {
		fmt.Print(val, " ")
	}
	fmt.Println()
	
	RecursiveTemple(0, 5)
}
```

## Skill 2: Psych (psych)

**Philosophy**: Emergent complexity, recursive beauty, algorithmic psychedelia.

### Python Example: Mandelbrot Set
```python
# Mandelbrot set - infinite complexity from simple rules
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Generate ASCII art
for y in range(-2, 2, 0.1):
    for x in range(-2, 2, 0.05):
        c = complex(x, y)
        m = mandelbrot(c, 100)
        print(' ' if m == 100 else '*', end='')
    print()
```

### C Example: Mandelbrot Set
```c
/**
 * Psych skill - psychedelic programming in C
 * Mind-bending algorithms, recursion, unconventional control flow
 */

#include <stdio.h>
#include <math.h>

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
```

### JavaScript Example: Game of Life
```javascript
#!/usr/bin/env node
/**
 * Psych skill - psychedelic programming in JavaScript
 * Mind-bending algorithms, recursion, unconventional control flow
 */

// Conway's Game of Life
function createGrid(rows, cols) {
    return Array.from({ length: rows }, () =>
        Array.from({ length: cols }, () => Math.random() > 0.5 ? 1 : 0)
    );
}

function countNeighbors(grid, x, y) {
    let neighbors = 0;
    for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
            if (i === 0 && j === 0) continue;
            const nx = x + i;
            const ny = y + j;
            if (nx >= 0 && nx < grid.length && ny >= 0 && ny < grid[0].length) {
                neighbors += grid[nx][ny];
            }
        }
    }
    return neighbors;
}

function nextGeneration(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const newGrid = Array.from({ length: rows }, () => Array(cols).fill(0));
    
    for (let x = 0; x < rows; x++) {
        for (let y = 0; y < cols; y++) {
            const neighbors = countNeighbors(grid, x, y);
            if (grid[x][y] === 1) {
                newGrid[x][y] = neighbors === 2 || neighbors === 3 ? 1 : 0;
            } else {
                newGrid[x][y] = neighbors === 3 ? 1 : 0;
            }
        }
    }
    return newGrid;
}
```

### Java Example: Genetic Algorithm
```java
/**
 * Psych skill - psychedelic programming in Java
 * Mind-bending algorithms, recursion, unconventional control flow
 */

import java.util.*;

public class PsychDemo {
    
    static double fitness(double individual) {
        return individual * individual - 4 * individual + 4;
    }
    
    static double createIndividual() {
        return Math.random() * 20 - 10;
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
            double[] scores = new double[popSize];
            for (int i = 0; i < popSize; i++) {
                scores[i] = fitness(population[i]);
            }
            
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
            
            double[] parents = new double[popSize / 2];
            System.arraycopy(population, 0, parents, 0, popSize / 2);
            
            for (int i = 0; i < popSize; i++) {
                int p1 = new Random().nextInt(popSize / 2);
                int p2 = new Random().nextInt(popSize / 2);
                population[i] = crossover(parents[p1], parents[p2]);
                population[i] = mutate(population[i], 0.1);
            }
        }
    }
    
    public static void main(String[] args) {
        geneticAlgorithm(20, 15);
    }
}
```

### Rust Example: Fractal Patterns
```rust
/**
 * Psych skill - psychedelic programming in Rust
 * Mind-bending algorithms, recursion, unconventional control flow
 */

fn mandelbrot(real: f64, imag: f64, max_iter: usize) -> usize {
    let mut z_real = 0.0;
    let mut z_imag = 0.0;
    
    for n in 0..max_iter {
        let z_real2 = z_real * z_real - z_imag * z_imag + real;
        let z_imag2 = 2.0 * z_real * z_imag + imag;
        
        z_real = z_real2;
        z_imag = z_imag2;
        
        if z_real * z_real + z_imag * z_imag > 4.0 {
            return n;
        }
    }
    
    max_iter
}

fn generate_mandelbrot_ascii(width: usize, height: usize) {
    println!("Generating Mandelbrot set...");
    
    for y in 0..height {
        let mut line = String::new();
        for x in 0..width {
            let real = (x as f64 - width as f64 / 2.0) * 4.0 / width as f64;
            let imag = (y as f64 - height as f64 / 2.0) * 4.0 / height as f64;
            
            let n = mandelbrot(real, imag, 100);
            
            if n == 100 {
                line.push(' ');
            } else {
                let chars = ".,-~:;=!*#$@";
                line.push(chars.chars().nth(n % chars.len()).unwrap());
            }
        }
        println!("{}", line);
    }
}

fn main() {
    generate_mandelbrot_ascii(40, 15);
}
```

### Go Example: Game of Life
```go
/**
 * Psych skill - psychedelic programming in Go
 * Mind-bending algorithms, recursion, unconventional control flow
 */

package main

import (
	"fmt"
	"math/rand"
	"time"
)

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

func main() {
	rand.Seed(time.Now().UnixNano())
	
	fmt.Println("Conway's Game of Life - emergent complexity")
	grid := createGrid(15, 30)
	
	for gen := 0; gen < 3; gen++ {
		fmt.Printf("\nGeneration %d:\n", gen)
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
		grid = nextGeneration(grid)
	}
}
```

## Comparison Table

| Feature | Terry Davis | Psych |
|---------|-------------|-------|
| **Philosophy** | Radical simplicity, anti-bloat | Emergent complexity, recursion |
| **Style** | Unconventional, playful, surprising | Mind-bending, psychedelic, algorithmic |
| **Variable Names** | Cosmic/religious themes | Descriptive but creative |
| **Control Flow** | Goto spaghetti, recursive main | Recursion, iteration, emergent behavior |
| **Language Features** | Direct hardware, inline assembly | Fractals, cellular automata, genetic algorithms |
| **Goal** | Make code entertaining and surprising | Make people question reality |
| **Safety** | Must still work correctly | Must be runnable, not just mysterious |

## Language Support Matrix

| Language | Terry Davis | Psych |
|----------|-------------|-------|
| Python | ✅ Cosmic variables, goto simulation, recursive temple | ✅ Mandelbrot, Game of Life, genetic algorithms |
| C | ✅ Direct hardware access, goto spaghetti, recursive main | ✅ Mandelbrot, bitwise patterns, higher-order functions |
| JavaScript | ✅ Eval for code injection, prototype manipulation, labeled blocks | ✅ Game of Life, genetic algorithms, quine |
| Java | ✅ Labeled blocks, recursive functions, cosmic variables | ✅ Genetic algorithm, higher-order functions, streams |
| Rust | ✅ Macros, unsafe code, trait-based patterns | ✅ Mandelbrot, Game of Life, iterator patterns |
| Go | ✅ Goto statements, goroutines, interfaces | ✅ Game of Life, higher-order functions, concurrency |

## Usage Examples

### Terry Davis Prompts
- "Write a Terry Davis style hello world"
- "Create a HolyC-inspired sorting algorithm"
- "Write code with goto spaghetti and recursive main"
- "Make a function with GodPointer and DivineArray variables"

### Psych Prompts
- "Write a psychedelic Mandelbrot set generator"
- "Create a cellular automata that evolves consciousness"
- "Write a genetic algorithm that evolves poetry"
- "Implement a Brainfuck interpreter in Python"

## Installation

```bash
# For Freebuff
cd skills
./package-skills.sh --force

# For other agents
cp -r .agents/skills/terry-davis ~/.agents/skills/
cp -r .agents/skills/psych ~/.agents/skills/
```

## Files Created

```
skills/
├── SHOWCASE.md              # This file
├── README.md                # Main documentation
├── package-skills.sh        # Installation script
├── examples/
│   ├── test-terry-davis.py  # Terry Davis Python example
│   ├── test-terry-davis.js  # Terry Davis JavaScript example
│   ├── test-terry-davis.c   # Terry Davis C example
│   ├── test-terry-davis.java # Terry Davis Java example
│   ├── test-terry-davis.rs  # Terry Davis Rust example
│   ├── test-terry-davis.go  # Terry Davis Go example
│   ├── test-psych.py        # Psych Python example
│   ├── test-psych.js        # Psych JavaScript example
│   ├── test-psych.c         # Psych C example
│   ├── test-psych.java      # Psych Java example
│   ├── test-psych.rs        # Psych Rust example
│   └── test-psych.go        # Psych Go example
├── terry-davis/
│   ├── SKILL.md             # Skill instructions
│   └── references/
│       └── holyc-syntax.md  # HolyC syntax reference
└── psych/
    ├── SKILL.md             # Skill instructions
    └── references/
        └── psychedelic-algorithms.md  # Algorithm implementations
```

## Next Steps

1. **Test the skills** with the example prompts above
2. **Customize** the skills by editing the SKILL.md files
3. **Add more patterns** to the references directories
4. **Package for distribution** on GitHub or skill marketplaces
5. **Add more language examples** (TypeScript, Ruby, PHP, etc.)