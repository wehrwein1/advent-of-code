package util

import (
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestStringToInt(t *testing.T) {
	assert.Equal(t, 56, StringToInt("56"))
	var panicError error
	defer func() { // defer() has stack semantics, push first = run second
		assert.Equal(t, "strconv.Atoi: parsing \"not-a-number\": invalid syntax", panicError.Error(), "panic() msg different")
	}()
	defer func() { // defer() has stack semantics, push last = run first. Intent: basically try/catch
		panicInfo := recover()
		panicError = panicInfo.(error)
	}()
	StringToInt("not-a-number") // trigger panic -> both defer functions
}

func TestStringSplitToInts(t *testing.T) {
	assert.Equal(t, StringSplitToInts("2x3x4", "x"), []int{2, 3, 4})
}

func TestStringsToInts(t *testing.T) {
	assert.Equal(t, []int{2, 3, 4, 6}, StringsToInts([]string{"2", "3", "4", "6"}))
}

func TestStringsFilter(t *testing.T) {
	assert.Equal(t, []string{"br", "bo", "ba"}, StringsFilter([]string{"aa", "ab", "br", "cc", "bo", "ba", "xt", "zz"}, func(s string) bool { return strings.HasPrefix(s, "b") }))
}

func TestPartitionSliceStrings(t *testing.T) {
	testcase1 := []string{"one", "two", "", "three", "four", "", "five", "six", ""}
	testcase2 := []string{"one", "two", "", "three", "four", "", "five", "six"} // no final delim
	assert.Equal(t, [][]string{{"one", "two"}, {"three", "four"}, {"five", "six"}}, PartitionSliceStrings(testcase1))
	assert.Equal(t, [][]string{{"one", "two"}, {"three", "four"}, {"five", "six"}}, PartitionSliceStrings(testcase2))
}
