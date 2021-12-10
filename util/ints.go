package util

import "sort"

var IncrementInt = func(n int) int { return n + 1 }

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

func MapInts(items []int, f func(int) int) (results []int) {
	for _, item := range items {
		results = append(results, f(item))
	}
	return
}

func Int2dArrayHasValueAtPos(rowsAndCols [][]int, rowIndex int, colIndex int) (foundValue int, isFound bool) {
	rowCount := len(rowsAndCols)
	colCount := len(rowsAndCols[0])
	rowOk := (0 <= rowIndex) && (rowIndex < rowCount)
	colOk := (0 <= colIndex) && (colIndex < colCount)
	if rowOk && colOk {
		return rowsAndCols[rowIndex][colIndex], true
	}
	return 0 /* arbitrary not found value*/, false
}
