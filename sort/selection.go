package main

import (
	"fmt"
)

func Selection(list []int) []int {
	for i := 0; i < len(list); i++ {
		minIndex := i
		for j := minIndex + 1; j < len(list); j++ {
			if list[j] < list[minIndex] {
				minIndex = j
			}

		}
		if minIndex != i {
			oldMinValue := list[i]
			list[i] = list[minIndex]
			list[minIndex] = oldMinValue
		}
	}

	return list
}

func main() {
	type Lists struct {
		unsorted []int
		sorted   []int
	}

	l := new(Lists)
	l.unsorted = []int{55, 49, 100, 150, 0}
	fmt.Println("Unsorted: %d", l.unsorted)
	l.sorted = Selection(l.unsorted)
	fmt.Println("Sorted: %d", l.sorted)
}
