package main

import "fmt"

func quicksort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	pivot := arr[len(arr)/2]
	left := make([]int, 0)
	right := make([]int, 0)
	equal := make([]int, 0)

	for _, num := range arr {
		if num < pivot {
			left = append(left, num)
		} else if num > pivot {
			right = append(right, num)
		} else {
			equal = append(equal, num)
		}
	}

	left = quicksort(left)
	right = quicksort(right)

	return append(append(left, equal...), right...)
}

func main() {
	arr := []int{4,3,2,4,4,4,4,1,6,7}
	fmt.Println(quicksort(arr))
}