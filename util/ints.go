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

func MaxInt(items ...int) (maxItem int) {
	maxItem = items[0] // panic if empty slice
	for _, item := range items {
		if item > maxItem {
			maxItem = item
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

func IntSliceContains(items []int, searchedItem int) bool {
	for _, item := range items {
		if item == searchedItem {
			return true
		}
	}
	return false
}

func IntSliceIndexOf(items []int, predicate func(val int) bool) int { // https://stackoverflow.com/a/18203895
	for i := 0; i < len(items); i++ {
		if predicate(items[i]) {
			return i
		}
	}
	return -1
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
