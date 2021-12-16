package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSumInts(t *testing.T) {
	assert.Equal(t, SumInts(3, 66, 2, 7), 78, "sumInts() results different")
}

func TestIntSliceContains(t *testing.T) {
	assert.Equal(t, false, IntSliceContains([]int{1, 2, 3}, 4))
	assert.Equal(t, true, IntSliceContains([]int{1, 2, 3}, 2))
}

func TestIntSliceIndexOf(t *testing.T) {
	assert.Equal(t, -1, IntSliceIndexOf([]int{1, 2, 3}, func(val int) bool { return val == 5 }))
	assert.Equal(t, 0, IntSliceIndexOf([]int{1, 2, 3}, func(val int) bool { return val == 1 }))
	assert.Equal(t, 1, IntSliceIndexOf([]int{1, 2, 3}, func(val int) bool { return val == 2 }))
	assert.Equal(t, 2, IntSliceIndexOf([]int{1, 2, 3}, func(val int) bool { return val == 3 }))
}

func TestIntSliceToDigitsValue(t *testing.T) {
	assert.Equal(t, 5432, IntSliceToDigitsValue([]int{5, 4, 3, 2}))
	assert.Equal(t, 90210, IntSliceToDigitsValue([]int{9, 0, 2, 1, 0}))
}

func TestProductInts(t *testing.T) {
	assert.Equal(t, 150, ProductInts(15, 10))
	assert.Equal(t, 720, ProductInts(1, 2, 3, 4, 5, 6))
}

func TestMinInt(t *testing.T) {
	assert.Equal(t, 2, MinInt(31, 66, 2, 7), "minInt() results different")
}

func TestMaxInt(t *testing.T) {
	assert.Equal(t, 66, MaxInt(31, 66, 2, 7), "minInt() results different")
}

func TestMapInts(t *testing.T) {
	assert.Equal(t, []int{11, 21, 31}, MapInts([]int{10, 20, 30}, IncrementInt))
	assert.Equal(t, []int{20, 40, 60}, MapInts([]int{10, 20, 30}, func(i int) int { return i * 2 }))
}

func TestMapIntsToBools(t *testing.T) {
	assert.Equal(t, []bool{}, MapIntsToBools([]int{}, func(n int) bool { return false }))
	assert.Equal(t, []bool{true, true, false, false, true}, MapIntsToBools([]int{1, 5, 10, 15, 0}, func(n int) bool { return n < 10 }))
}

func TestSortedInts(t *testing.T) {
	assert.Equal(t, []int{1, 2, 3, 4, 5}, SortedInts(4, 1, 2, 5, 3))
}
