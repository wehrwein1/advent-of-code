package util

import "sort"

func MinInt(items ...int) (minItem int) {
	minItem = items[0] // panic if empty slice
	for _, item := range items {
		if item < minItem {
			minItem = item
		}
	}
	return
}

func SumInts(items ...int) (sum int) {
	for _, item := range items {
		sum += item
	}
	return sum
}

func ProductInts(coords ...int) int {
	product := 1
	for _, coord := range coords {
		product *= coord
	}
	return product
}

func SortedInts(items ...int) []int {
	sort.Ints(items) // stateful change
	return items
}
