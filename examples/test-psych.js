#!/usr/bin/env node
/**
 * Psych skill - psychedelic programming in JavaScript
 * Mind-bending algorithms, recursion, unconventional control flow
 */

// Pattern 1: Mandelbrot Set - ASCII Art
function mandelbrot(c, maxIter = 100) {
    let z = 0;
    for (let n = 0; n < maxIter; n++) {
        if (Math.abs(z) > 2) return n;
        z = z * z + c;
    }
    return maxIter;
}

function generateMandelbrotAscii(width = 60, height = 20) {
    console.log("Generating Mandelbrot set...");
    for (let y = 0; y < height; y++) {
        let line = '';
        for (let x = 0; x < width; x++) {
            // Map pixel to complex plane
            const real = (x - width / 2.0) * 4.0 / width;
            const imag = (y - height / 2.0) * 4.0 / height;
            const c = { real, imag };
            
            // Calculate membership (simplified for object)
            let z = { real: 0, imag: 0 };
            let n = 0;
            while (n < 100 && (z.real * z.real + z.imag * z.imag) <= 4) {
                const newReal = z.real * z.real - z.imag * z.imag + c.real;
                const newImag = 2 * z.real * z.imag + c.imag;
                z = { real: newReal, imag: newImag };
                n++;
            }
            
            // Print character
            if (n === 100) {
                line += ' ';
            } else {
                const chars = '.,-~:;=!*#$@';
                line += chars[n % chars.length];
            }
        }
        console.log(line);
    }
}

// Pattern 2: Conway's Game of Life
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

function printGrid(grid) {
    grid.forEach(row => {
        console.log(row.map(cell => cell ? '█' : ' ').join(''));
    });
}

function runGameOfLife(generations = 5, width = 30, height = 15) {
    console.log("Conway's Game of Life - emergent complexity");
    let grid = createGrid(height, width);
    
    for (let gen = 0; gen < generations; gen++) {
        console.log(`\nGeneration ${gen}:`);
        printGrid(grid);
        grid = nextGeneration(grid);
    }
}

// Pattern 3: Recursive Fractal Tree (ASCII)
function drawTreeAscii(length, depth = 0) {
    if (length <= 0) return [];
    
    const lines = [];
    // Draw trunk
    lines.push(' '.repeat(depth) + '|'.repeat(length));
    
    // Draw branches
    if (length > 1) {
        const leftBranch = drawTreeAscii(length - 1, depth + 1);
        const rightBranch = drawTreeAscii(length - 1, depth + 1);
        lines.push(...leftBranch);
        lines.push(...rightBranch);
    }
    
    return lines;
}

// Pattern 4: Genetic Algorithm
function fitness(individual) {
    return individual * individual - 4 * individual + 4;
}

function createIndividual() {
    return Math.random() * 20 - 10; // -10 to 10
}

function crossover(parent1, parent2) {
    return (parent1 + parent2) / 2;
}

function mutate(individual, rate = 0.1) {
    if (Math.random() < rate) {
        return individual + (Math.random() - 0.5) * 2;
    }
    return individual;
}

function geneticAlgorithm(generations = 30, popSize = 20) {
    console.log("Genetic Algorithm - evolving solutions");
    let population = Array.from({ length: popSize }, createIndividual);
    
    for (let gen = 0; gen < generations; gen++) {
        // Evaluate fitness
        const scored = population.map(ind => [ind, fitness(ind)]);
        scored.sort((a, b) => b[1] - a[1]);
        
        // Show best
        if (gen % 10 === 0) {
            const [bestInd, bestFit] = scored[0];
            console.log(`Gen ${gen}: Best = ${bestInd.toFixed(4)}, Fitness = ${bestFit.toFixed(4)}`);
        }
        
        // Selection
        const parents = scored.slice(0, popSize / 2).map(([ind]) => ind);
        
        // Crossover and mutation
        const children = [];
        while (children.length < popSize) {
            const p1 = parents[Math.floor(Math.random() * parents.length)];
            const p2 = parents[Math.floor(Math.random() * parents.length)];
            let child = crossover(p1, p2);
            child = mutate(child);
            children.push(child);
        }
        
        population = children;
    }
    
    // Return best
    const best = population.reduce((a, b) => fitness(a) > fitness(b) ? a : b);
    return [best, fitness(best)];
}

// Pattern 5: Quine (self-replicating program)
function quine() {
    const s = 'const s = %j\\nconsole.log(s.replace(/%j/, JSON.stringify(s)))';
    console.log(s.replace(/%j/, JSON.stringify(s)));
}

// Pattern 6: Psychedelic color cycling
function colorCycle() {
    const colors = ['\x1b[91m', '\x1b[92m', '\x1b[93m', '\x1b[94m', '\x1b[95m', '\x1b[96m'];
    const reset = '\x1b[0m';
    
    console.log("Psychedelic color cycling:");
    let output = '';
    for (let i = 0; i < 30; i++) {
        const color = colors[i % colors.length];
        const char = '█'.repeat(5);
        output += `${color}${char}${reset} `;
    }
    console.log(output);
}

// Pattern 7: Recursive Fibonacci with memoization
function fibonacciMemo() {
    const memo = new Map();
    
    function fib(n) {
        if (n <= 1) return n;
        if (memo.has(n)) return memo.get(n);
        
        const result = fib(n - 1) + fib(n - 2);
        memo.set(n, result);
        return result;
    }
    
    return fib;
}

// Pattern 8: Higher-order functions for psychedelic transformations
function psychedelicTransformations() {
    const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    
    // Map, filter, reduce chain
    const result = numbers
        .map(x => x * x)
        .filter(x => x % 2 === 0)
        .reduce((a, b) => a + b, 0);
    
    console.log(`Psychedelic transformation result: ${result}`);
    
    // Curried function
    const add = a => b => c => a + b + c;
    console.log(`Curried addition: ${add(1)(2)(3)}`);
    
    // Function composition
    const compose = (f, g) => x => f(g(x));
    const double = x => x * 2;
    const increment = x => x + 1;
    const doubleAfterIncrement = compose(double, increment);
    console.log(`Double after increment: ${doubleAfterIncrement(5)}`);
}

// Main execution
if (require.main === module) {
    console.log("=".repeat(60));
    console.log("PSYCHEDELIC PROGRAMMING SHOWCASE - JavaScript");
    console.log("=".repeat(60));
    
    // Test 1: Mandelbrot Set
    console.log("\n1. Mandelbrot Set - ASCII Art");
    generateMandelbrotAscii(40, 15);
    
    // Test 2: Game of Life
    console.log("\n2. Conway's Game of Life");
    runGameOfLife(3, 20, 10);
    
    // Test 3: Recursive Tree
    console.log("\n3. Recursive Fractal Tree");
    const treeLines = drawTreeAscii(6);
    treeLines.slice(0, 12).forEach(line => console.log(line));
    
    // Test 4: Genetic Algorithm
    console.log("\n4. Genetic Algorithm");
    const [bestInd, bestFit] = geneticAlgorithm(20, 15);
    console.log(`Final best: ${bestInd.toFixed(4)}, Fitness: ${bestFit.toFixed(4)}`);
    
    // Test 5: Quine
    console.log("\n5. Quine (self-replicating program)");
    console.log("Output:");
    quine();
    
    // Test 6: Color Cycling
    console.log("\n6. Psychedelic Color Cycling");
    colorCycle();
    
    // Test 7: Recursive Fibonacci
    console.log("\n7. Recursive Fibonacci with Memoization");
    const fib = fibonacciMemo();
    console.log(`Fibonacci(10) = ${fib(10)}`);
    console.log(`Fibonacci(20) = ${fib(20)}`);
    
    // Test 8: Psychedelic Transformations
    console.log("\n8. Psychedelic Transformations");
    psychedelicTransformations();
    
    console.log("\n" + "=".repeat(60));
    console.log("END OF PSYCHEDELIC SHOWCASE - JavaScript");
    console.log("=".repeat(60));
}