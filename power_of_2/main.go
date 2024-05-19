// DESCRIPTION:
// Complete the function that takes a non-negative integer n as input,
// and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

// Examples
// n = 0  ==> [1]        # [2^0]
// n = 1  ==> [1, 2]     # [2^0, 2^1]
// n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

package main

import "fmt"

func PowersOfTwo(n int) []uint64 {
	list := make([]uint64, n+1)
	for i := 0; i <= n; i++ {
		list[i] = 1 << i
	}
	return list
}

func main() {
	// Test cases
	fmt.Println(PowersOfTwo(0)) // [1]
	fmt.Println(PowersOfTwo(1)) // [1, 2]
	fmt.Println(PowersOfTwo(2)) // [1, 2, 4]
	fmt.Println(PowersOfTwo(3)) // [1, 2, 4, 8]
}
