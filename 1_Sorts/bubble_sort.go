package main

import (
	"fmt"
)

func sort(unsorted []int) []int {
	for i := 0; i <= len(unsorted)-1; i++ {
		for j := 0; j <= len(unsorted)-2; j++ {
			if unsorted[j] > unsorted[j+1] {
				first := unsorted[j]
				second := unsorted[j+1]
				unsorted[j] = second
				unsorted[j+1] = first
			}
			fmt.Print(j)
		}
	}
	return unsorted
}

func main() {
	array := []int{2, 11, 5, 3, 1, 8}
	// i = 0, j =1 - 2, 5, 11 , 3, 1, 8
	// i = 0, j =2 - 2, 5, 3, 11, 1, 8
	fmt.Println(sort(array))
}
