package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	slice := generateSlice(20)
	fmt.Println("\n--- Unsorted --- \n\n", slice)
	selectionsort(slice)
	fmt.Println("\n--- Sorted ---\n\n", slice, "\n")
}

// Generates a slice of size, size filled with random numbers
func generateSlice(size int) []int {

	slice := make([]int, size, size)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < size; i++ {
		slice[i] = rand.Intn(999) - rand.Intn(999)
	}
	return slice
}

func selectionsort(items []int) {
	var n = len(items)
	for i := 0; i < n; i++ {
		var minIdx = i
		for j := i; j < n; j++ {
			if items[j] < items[minIdx] {
				minIdx = j
			}
		}
		items[i], items[minIdx] = items[minIdx], items[i]
	}
}

/*
func selectionsort(a []int) {
    for i, x := range a[:len(a)-1] {
        k := i
        for j, y := range a[i+1 : len(a)] {
            if x > y {
                // out of order
                k = i + 1 + j
                x = y
            }
        }
        a[k], a[i] = a[i], x
    }
}
*/

/*
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
*/
