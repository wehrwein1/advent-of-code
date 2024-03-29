package util

import (
	"strconv"
	"strings"
)

// cheat sheet to help remember the APIs
var StringStartsWith = strings.HasPrefix
var StringContains = strings.Contains

// Intent: likely remove these functions when go gets generics

func StringSplitToInts(text string, delim string) (ret []int) {
	return StringSplitToIntsFunc(text, func(s string) []string { return strings.Split(s, delim) })
}

func StringSplitToIntsWhitespace(text string) []int {
	return StringSplitToIntsFunc(text, strings.Fields)
}

// TODO FIXME [Go generics can't come soon enough]
func StringSplitToIntsFunc(text string, splitFn func(string) []string) (ret []int) {
	for _, dim := range splitFn(text) {
		val, err := strconv.Atoi(dim)
		if err != nil {
			panic(err)
		}
		ret = append(ret, val)
	}
	return
}

func StringsToInts(items []string) (ints []int) {
	for _, item := range items {
		ints = append(ints, StringToInt(item))
	}
	return
}

func StringsToInt2dArray(digitStrings []string) (intGrid [][]int) {
	for _, digitLine := range digitStrings {
		intGrid = append(intGrid, StringSplitToInts(digitLine, ""))
	}
	return
}

func StringToInt(value string) int {
	intval, err := strconv.Atoi(value)
	if err != nil {
		panic(err)
	}
	return intval
}

// adapted from https://stackoverflow.com/a/37563128/3633993
func StringsFilter(items []string, retainIf func(string) bool) (result []string) {
	for _, s := range items {
		if retainIf(s) {
			result = append(result, s)
		}
	}
	return
}

func PartitionSliceStrings(lines []string) (partitions [][]string) { // partition on empty lines
	var currentPartition []string
	for _, line := range lines {
		isNewPartitition := len(Chomp(line)) == 0
		if isNewPartitition {
			partitions = append(partitions, currentPartition)
			currentPartition = []string{}
			continue
		}
		currentPartition = append(currentPartition, Chomp(line)) // collect current partition
	}
	if len(currentPartition) > 0 {
		partitions = append(partitions, currentPartition)
	}
	return
}
