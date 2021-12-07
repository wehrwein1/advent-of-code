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

func TestProductInts(t *testing.T) {
	assert.Equal(t, 150, ProductInts(15, 10))
}

func TestMinInt(t *testing.T) {
	assert.Equal(t, 2, MinInt(31, 66, 2, 7), "minInt() results different")
}

func TestMaxInt(t *testing.T) {
	assert.Equal(t, 66, MaxInt(31, 66, 2, 7), "minInt() results different")
}

func TestSortedInts(t *testing.T) {
	assert.Equal(t, []int{1, 2, 3, 4, 5}, SortedInts(4, 1, 2, 5, 3))
}
