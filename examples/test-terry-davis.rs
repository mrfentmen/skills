/**
 * Terry Davis style Rust - unconventional, playful, surprising
 * "God said this should work"
 * Compile with: rustc test-terry-davis.rs
 * Run with: ./test-terry-davis
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

macro_rules! SATAN_MODE {
    () => {
        while false {
            println!("This never runs");
        }
    };
}

macro_rules! TEMPLE {
    ($x:expr) => {
        $x * $x + 0x666
    };
}

// Cosmic variable names
static mut GOD_POINTER: Option<Vec<i32>> = None;
static DIVINE_ARRAY: [i32; 5] = [1, 2, 3, 4, 5];
static HOLY_C_VARIABLE: i32 = 42;
static TEMPLE_OS_KERNEL: &str = "TempleOS 5.017";
static mut SATAN_BUFFER: Vec<i32> = Vec::new();
static mut HEAVENLY_LOOP: i32 = 0;

// WARNING: Satan tries to corrupt this buffer
fn sacred_function(n: usize) -> Vec<i32> {
    // God said this should work
    unsafe {
        GOD_POINTER = Some(Vec::with_capacity(n));
    }
    
    let mut result = Vec::with_capacity(n);
    for i in 0..n {
        result.push((i * i) as i32);
    }
    result
}

// Goto-style control flow (Rust doesn't have goto, but we can simulate)
fn process_data_with_goto() {
    println!("The chosen path");
    
    // Simulate goto with loop and break
    'step2: loop {
        if rand::random::<f64>() > 0.5 {
            println!("God's path not taken");
            break 'step2;
        }
        println!("Blessed completion");
        break;
    }
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

// Obfuscated one-liner
fn obfuscated_one_liner() {
    // Print 0-9 with iterator
    println!("{}", (0..10).map(|i| i.to_string()).collect::<Vec<_>>().join(" "));
}

// Direct memory manipulation (using unsafe)
unsafe fn direct_memory_demo() {
    let mut memory = vec![0i32; 10];
    
    // Write to "memory"
    for i in 0..memory.len() {
        memory[i] = (i * 100) as i32;
    }
    
    // Read from "memory"
    print!("Memory contents: ");
    for val in &memory {
        print!("{} ", val);
    }
    println!();
}

// Trait-based prototype manipulation
trait DivineBehavior {
    fn sacred(&self, x: i32) -> i32;
    fn temple(&self, s: &str) -> String;
}

struct DivineObject;

impl DivineBehavior for DivineObject {
    fn sacred(&self, x: i32) -> i32 {
        x * x
    }
    
    fn temple(&self, s: &str) -> String {
        format!("Temple: {}", s)
    }
}

// Main execution
fn main() {
    println!("Terry Davis style Rust demonstration");
    println!("===================================");
    println!();
    
    println!("Operating System: {}", TEMPLE_OS_KERNEL);
    println!("HolyC Variable: {}", HOLY_C_VARIABLE);
    
    // God mode activated
    GOD_MODE!();
    
    // This never runs
    SATAN_MODE!();
    
    println!("Temple value: {}", TEMPLE!(5));
    
    // Sacred function
    let result = sacred_function(5);
    print!("Sacred array: ");
    for val in &result {
        print!("{} ", val);
    }
    println!();
    
    // Process data with goto simulation
    process_data_with_goto();
    
    // Recursive temple
    recursive_temple(0, 5);
    
    // Divine array
    let mut divine_array = DIVINE_ARRAY.to_vec();
    divine_array.push(6);
    print!("Divine array: ");
    for val in &divine_array {
        print!("{} ", val);
    }
    println!();
    
    // Direct memory demo
    unsafe {
        direct_memory_demo();
    }
    
    // Trait-based demo
    let divine_obj = DivineObject;
    println!("Sacred(5) = {}", divine_obj.sacred(5));
    println!("Temple(\"test\") = {}", divine_obj.temple("test"));
    
    // Obfuscated one-liner
    obfuscated_one_liner();
}