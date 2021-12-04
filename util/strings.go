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
	for _, dim := range strings.Split(text, delim) {
		val, err := strconv.Atoi(dim)
		Check(err)
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

func StringToInt(value string) int {
	intval, err := strconv.Atoi(value)
	Check(err)
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
		isNewPartitition := len(chomp(line)) == 0
		if isNewPartitition {
			partitions = append(partitions, currentPartition)
			currentPartition = []string{}
			continue
		}
		currentPartition = append(currentPartition, chomp(line)) // collect current partition
	}
	if len(currentPartition) > 0 {
		partitions = append(partitions, currentPartition)
	}
	return
}
