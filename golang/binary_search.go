package main

import "fmt"

func binarySearchRecursion(arr []int, low int, high int, target int) int {
	if target > arr[high] || target < arr[low] || low > high {
		return -1
	}

	mid := (low + high) / 2

	if arr[mid] == target {
		return mid
	} else if arr[mid] < target {
		return binarySearchRecursion(arr, mid + 1, high, target)
	} else if arr[mid] > target {
		return binarySearchRecursion(arr, low, mid - 1, target)
	} else {
		return -1
	}

	return -1
}

func binarySearch(arr []int, target int) int {
	low := 0
	high := len(arr) - 1

	if target > arr[high] || target < arr[low] {
		return -1
	}

	for low <= high {
		mid := (low + high) / 2

		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	target := 6

	index := binarySearch(arr, target)
	if index != -1 {
		fmt.Printf("Target found at index %d\n", index)
	} else {
		fmt.Println("Target not found")
	}

	index = binarySearchRecursion(arr, 0, len(arr) - 1, target)
	if index != -1 {
		fmt.Printf("Target found at index %d\n", index)
	} else {
		fmt.Println("Target not found")
	}
}
