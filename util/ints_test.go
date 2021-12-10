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

func TestInt2dArrayHasValueAtPos(t *testing.T) {
	grid := [][]int{{0, 1, 2, 3},
		{4, 5, 6, 7},
		{8, 8, 10, 11}}
	{
		val, isFound := Int2dArrayHasValueAtPos(grid, 0, 0)
		assert.Equal(t, 0, val)
		assert.Equal(t, true, isFound)
	}
	{
		_, isFound := Int2dArrayHasValueAtPos(grid, 5, 5)
		assert.Equal(t, false, isFound)
	}
	{
		_, isFound := Int2dArrayHasValueAtPos(grid, -1, 8)
		assert.Equal(t, false, isFound)
	}
}
