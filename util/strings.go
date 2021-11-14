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
