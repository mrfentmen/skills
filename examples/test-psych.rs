/**
 * Psych skill - psychedelic programming in Rust
 * Mind-bending algorithms, recursion, unconventional control flow
 * Compile with: rustc test-psych.rs
 * Run with: ./test-psych
 */

use std::collections::HashMap;

// Pattern 1: Mandelbrot Set - ASCII Art
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
            // Map pixel to complex plane
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

// Pattern 2: Conway's Game of Life
fn create_grid(rows: usize, cols: usize) -> Vec<Vec<i32>> {
    use rand::Rng;
    let mut rng = rand::thread_rng();
    (0..rows)
        .map(|_| (0..cols).map(|_| rng.gen_range(0..2)).collect())
        .collect()
}

fn count_neighbors(grid: &[Vec<i32>], x: usize, y: usize) -> i32 {
    let mut neighbors = 0;
    for i in -1..=1 {
        for j in -1..=1 {
            if i == 0 && j == 0 {
                continue;
            }
            let nx = x as i32 + i;
            let ny = y as i32 + j;
            if nx >= 0 && nx < grid.len() as i32 && ny >= 0 && ny < grid[0].len() as i32 {
                neighbors += grid[nx as usize][ny as usize];
            }
        }
    }
    neighbors
}

fn next_generation(grid: &[Vec<i32>]) -> Vec<Vec<i32>> {
    let rows = grid.len();
    let cols = grid[0].len();
    let mut new_grid = vec![vec![0; cols]; rows];
    
    for x in 0..rows {
        for y in 0..cols {
            let neighbors = count_neighbors(grid, x, y);
            if grid[x][y] == 1 {
                new_grid[x][y] = if neighbors == 2 || neighbors == 3 { 1 } else { 0 };
            } else {
                new_grid[x][y] = if neighbors == 3 { 1 } else { 0 };
            }
        }
    }
    new_grid
}

fn print_grid(grid: &[Vec<i32>]) {
    for row in grid {
        let line: String = row.iter().map(|&cell| if cell == 1 { '#' } else { ' ' }).collect();
        println!("{}", line);
    }
}

fn run_game_of_life(generations: usize, width: usize, height: usize) {
    println!("Conway's Game of Life - emergent complexity");
    let mut grid = create_grid(height, width);
    
    for gen in 0..generations {
        println!("\nGeneration {}:", gen);
        print_grid(&grid);
        grid = next_generation(&grid);
    }
}

// Pattern 3: Recursive Fractal Tree (ASCII)
fn draw_tree_ascii(length: usize, depth: usize) {
    if length == 0 {
        return;
    }
    
    // Draw trunk
    let line = " ".repeat(depth) + &"|".repeat(length);
    println!("{}", line);
    
    // Draw branches
    if length > 1 {
        draw_tree_ascii(length - 1, depth + 1);
        draw_tree_ascii(length - 1, depth + 1);
    }
}

// Pattern 4: Genetic Algorithm
fn fitness(individual: f64) -> f64 {
    individual * individual - 4.0 * individual + 4.0
}

fn create_individual() -> f64 {
    use rand::Rng;
    let mut rng = rand::thread_rng();
    rng.gen_range(-10.0..10.0)
}

fn crossover(parent1: f64, parent2: f64) -> f64 {
    (parent1 + parent2) / 2.0
}

fn mutate(individual: f64, rate: f64) -> f64 {
    use rand::Rng;
    let mut rng = rand::thread_rng();
    if rng.gen::<f64>() < rate {
        individual + rng.gen_range(-1.0..1.0)
    } else {
        individual
    }
}

fn genetic_algorithm(generations: usize, pop_size: usize) {
    println!("Genetic Algorithm - evolving solutions");
    let mut population: Vec<f64> = (0..pop_size).map(|_| create_individual()).collect();
    
    for gen in 0..generations {
        // Evaluate fitness
        let scores: Vec<f64> = population.iter().map(|&ind| fitness(ind)).collect();
        
        // Find best
        let best_idx = scores
            .iter()
            .enumerate()
            .max_by(|a, b| a.1.partial_cmp(b.1).unwrap())
            .unwrap()
            .0;
        
        if gen % 10 == 0 {
            println!("Gen {}: Best = {:.4}, Fitness = {:.4}", 
                    gen, population[best_idx], scores[best_idx]);
        }
        
        // Selection (simple: top half)
        let mut parents: Vec<f64> = population[..pop_size/2].to_vec();
        
        // Crossover and mutation
        use rand::seq::SliceRandom;
        let mut rng = rand::thread_rng();
        for i in 0..pop_size {
            let p1 = parents.choose(&mut rng).unwrap();
            let p2 = parents.choose(&mut rng).unwrap();
            population[i] = crossover(*p1, *p2);
            population[i] = mutate(population[i], 0.1);
        }
    }
    
    // Find final best
    let best_idx = population
        .iter()
        .enumerate()
        .max_by(|a, b| fitness(a.1).partial_cmp(&fitness(b.1)).unwrap())
        .unwrap()
        .0;
    
    println!("Final best: {:.4}, Fitness: {:.4}", 
            population[best_idx], fitness(population[best_idx]));
}

// Pattern 5: Recursive Fibonacci
fn fibonacci(n: i64) -> i64 {
    if n <= 1 {
        n
    } else {
        fibonacci(n - 1) + fibonacci(n - 2)
    }
}

// Pattern 6: Higher-order functions
fn apply_twice<F: Fn(f64) -> f64>(f: F, x: f64) -> f64 {
    f(f(x))
}

fn higher_order_demo() {
    println!("Higher-order functions demo:");
    
    let square = |x: f64| x * x;
    let add_one = |x: f64| x + 1.0;
    
    let result1 = apply_twice(square, 3.0);
    println!("apply_twice(square, 3) = {:.0}", result1);
    
    let result2 = apply_twice(add_one, 5.0);
    println!("apply_twice(add_one, 5) = {:.0}", result2);
    
    // Function composition
    let functions: Vec<Box<dyn Fn(f64) -> f64>> = vec![
        Box::new(|x| x * x),
        Box::new(|x| x + 1.0),
        Box::new(|x| x * x),
    ];
    
    let mut x = 2.0;
    for f in &functions {
        x = f(x);
    }
    println!("Composed function result: {:.0}", x);
}

// Main execution
fn main() {
    println!("============================================================");
    println!("PSYCHEDELIC PROGRAMMING SHOWCASE - Rust");
    println!("============================================================");
    
    // Test 1: Mandelbrot Set
    println!("\n1. Mandelbrot Set - ASCII Art");
    generate_mandelbrot_ascii(40, 15);
    
    // Test 2: Game of Life
    println!("\n2. Conway's Game of Life");
    run_game_of_life(3, 30, 15);
    
    // Test 3: Recursive Tree
    println!("\n3. Recursive Fractal Tree");
    draw_tree_ascii(6, 0);
    
    // Test 4: Genetic Algorithm
    println!("\n4. Genetic Algorithm");
    genetic_algorithm(20, 15);
    
    // Test 5: Recursive Fibonacci
    println!("\n5. Recursive Fibonacci");
    println!("Fibonacci(10) = {}", fibonacci(10));
    println!("Fibonacci(20) = {}", fibonacci(20));
    
    // Test 6: Higher-order functions
    println!("\n6. Higher-order Functions");
    higher_order_demo();
    
    println!("\n============================================================");
    println!("END OF PSYCHEDELIC SHOWCASE - Rust");
    println!("============================================================");
}