package util

import (
	"strconv"
	"strings"
)

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
		intval, err := strconv.Atoi(item)
		Check(err)
		ints = append(ints, intval)
	}
	return
}
