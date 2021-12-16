package util

import (
	"fmt"
	"log"
	"sort"
	"strconv"
	"strings"
)

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

func IntSliceToDigitsValue(items []int) int {
	removeChars := []string{"[", "]", " "}
	buffer := fmt.Sprintf("%v", items)
	for _, removeChar := range removeChars {
		buffer = strings.Replace(buffer, removeChar, "", -1)
	}
	val, err := strconv.Atoi(buffer)
	if err != nil {
		log.Fatalf("error converting %v to digit value: %v", items, err)
	}
	return val
}

func ProductInts(numbers ...int) int {
	product := 1
	for _, n := range numbers {
		product *= n
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

func MapIntsToBools(items []int, f func(int) bool) []bool {
	boolValues := []bool{}
	for _, item := range items {
		boolValues = append(boolValues, f(item))
	}
	return boolValues
}
