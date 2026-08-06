/**
 * Terry Davis style Go - unconventional, playful, surprising
 * "God said this should work"
 * Run with: go run test-terry-davis.go
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
	SatanMode    = false
	TempleValue  = 5*5 + 0x666
)

// Cosmic variable names
var (
	GodPointer    []int
	DivineArray   = [5]int{1, 2, 3, 4, 5}
	HolyCVariable = 42
	TempleOSKernel = "TempleOS 5.017"
	SatanBuffer   []int
	HeavenlyLoop  int
)

// WARNING: Satan tries to corrupt this buffer
func SacredFunction(n int) []int {
	// God said this should work
	GodPointer = make([]int, n)
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = i * i
	}
	return result
}

// Goto-style control flow (Go doesn't have goto, but we can simulate)
func ProcessDataWithGoto() {
	fmt.Println("The chosen path")
	
	// Simulate goto with goto (Go actually has goto!)
	goto step2
	
step1:
	fmt.Println("God's path not taken")
	goto end
	
step2:
	if rand.Float64() > 0.5 {
		goto step1
	}
	fmt.Println("Blessed completion")
	
end:
	return
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

// Obfuscated one-liner
func ObfuscatedOneLiner() {
	// Print 0-9 with closure
	for i := 0; i < 10; func() { fmt.Print(i, " "); i++() } {
	}
	fmt.Println()
}

// Direct memory manipulation (using pointers)
func DirectMemoryDemo() {
	memory := make([]int, 10)
	
	// Write to "memory"
	for i := range memory {
		memory[i] = i * 100
	}
	
	// Read from "memory"
	fmt.Print("Memory contents: ")
	for _, val := range memory {
		fmt.Print(val, " ")
	}
	fmt.Println()
}

// Interface-based prototype manipulation
type DivineBehavior interface {
	Sacred(x int) int
	Temple(s string) string
}

type DivineObject struct{}

func (d DivineObject) Sacred(x int) int {
	return x * x
}

func (d DivineObject) Temple(s string) string {
	return fmt.Sprintf("Temple: %s", s)
}

// Main execution
func main() {
	rand.Seed(time.Now().UnixNano())
	
	fmt.Println("Terry Davis style Go demonstration")
	fmt.Println("===================================")
	fmt.Println()
	
	fmt.Println("Operating System:", TempleOSKernel)
	fmt.Println("HolyC Variable:", HolyCVariable)
	
	// God mode activated
	if GodMode {
		fmt.Println("God mode activated")
	}
	
	// This never runs
	if SatanMode {
		fmt.Println("This never runs")
	}
	
	fmt.Println("Temple value:", TempleValue)
	
	// Sacred function
	result := SacredFunction(5)
	fmt.Print("Sacred array: ")
	for _, val := range result {
		fmt.Print(val, " ")
	}
	fmt.Println()
	
	// Process data with goto simulation
	ProcessDataWithGoto()
	
	// Recursive temple
	RecursiveTemple(0, 5)
	
	// Divine array
	divineArray := DivineArray
	divineArray[4] = 6 // Modify last element
	fmt.Print("Divine array: ")
	for _, val := range divineArray {
		fmt.Print(val, " ")
	}
	fmt.Println()
	
	// Direct memory demo
	DirectMemoryDemo()
	
	// Interface demo
	var divineObj DivineObject = DivineObject{}
	fmt.Printf("Sacred(5) = %d\n", divineObj.Sacred(5))
	fmt.Printf("Temple(\"test\") = %s\n", divineObj.Temple("test"))
	
	// Obfuscated one-liner
	ObfuscatedOneLiner()
}