package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInt2dArrayHasValueAtPos(t *testing.T) {
	grid := [][]int{{0, 1, 2, 3},
		{4, 5, 6, 7},
		{8, 9, 10, 11}}
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

func TestInt2dArrayFindNeighbors(t *testing.T) {
	grid := [][]int{{0, 1, 2, 3},
		{4, 5, 6, 7},
		{8, 9, 10, 11}}
	assert.Equal(t, 5, grid[1][1])
	assert.Equal(t, []Int2dArrayNeighbor{
		{Row: 0, Col: 1, Value: 1, Direction: North}, // north of 5
		{Row: 1, Col: 2, Value: 6, Direction: East},  // east of 5
		{Row: 2, Col: 1, Value: 9, Direction: South}, // south of 5
		{Row: 1, Col: 0, Value: 4, Direction: West},  // west of 5
	}, Int2dArrayFindNeighbors(grid, 1, 1))
}
