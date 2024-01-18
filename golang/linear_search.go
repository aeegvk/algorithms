package main

import "fmt"

func linearSearch(arr []int, target int) int {
	for i, num := range arr {
		if num == target {
			return i
		}
	}
	return -1
}

func main() {
	nums := []int{4, 2, 7, 1, 9, 5}
	target := 7
	index := linearSearch(nums, target)
	if index != -1 {
		fmt.Printf("Target %d found at index %d\n", target, index)
	} else {
		fmt.Printf("Target %d not found in the array\n", target)
	}
}
