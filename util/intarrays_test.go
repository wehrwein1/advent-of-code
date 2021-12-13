package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInt2dArrayHasValueAtPos(t *testing.T) {
	grid := [][]int{
		{0, 1, 2, 3},
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
	grid := [][]int{
		{0, 1, 2, 3},
		{4, 5, 6, 7},
		{8, 9, 10, 11}}
	assert.Equal(t, 5, grid[1][1])
	assert.Equal(t, []Int2dArrayNeighbor{
		{Row: 0, Col: 1, Value: 1, Direction: North}, // north of 5
		{Row: 1, Col: 2, Value: 6, Direction: East},  // east of 5
		{Row: 2, Col: 1, Value: 9, Direction: South}, // south of 5
		{Row: 1, Col: 0, Value: 4, Direction: West},  // west of 5
	}, Int2dArrayFindNeighbors(grid, 1, 1, PrimaryFourDirections))
}

func TestInt2dArrayDepthFirstSearch(t *testing.T) {
	grid := [][]int{
		{9, 1, 2, 9},
		{9, 9, 6, 9},
		{9, 9, 10, 11}}
	{
		var isGridPointValueLessThan9 = func(grid [][]int, p Point) bool { return grid[p.X][p.Y] < 9 }
		startPoint := *NewPoint(0, 2)
		assert.ElementsMatch(t,
			[]Point{
				{X: 1, Y: 2},
				{X: 0, Y: 1},
			}, Int2dArrayDepthFirstSearch(grid, startPoint, isGridPointValueLessThan9, PrimaryFourDirections)) // DFS result excludes start point
	}
	{
		var isGridPointValueExactly9 = func(grid [][]int, p Point) bool { return grid[p.X][p.Y] == 9 }
		startPoint := *NewPoint(2, 1)
		assert.ElementsMatch(t,
			[]Point{
				{X: 2, Y: 0},
				{X: 1, Y: 0},
				{X: 0, Y: 0},
				{X: 1, Y: 1},
			}, Int2dArrayDepthFirstSearch(grid, startPoint, isGridPointValueExactly9, PrimaryFourDirections))
	}
}

func TestRowCountAndColCount(t *testing.T) {
	grid := [][]int{
		{1, 2, 3},
		{4, 5, 6}}
	assert.Equal(t, 2, RowCount(grid))
	assert.Equal(t, 3, ColCount(grid))
}

func TestInt2dArrayMap(t *testing.T) {
	grid := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9}}
	Int2dArrayMap(grid, func(grid [][]int, point Point) int { return grid[point.X][point.Y] + 1 })
	assert.Equal(t, [][]int{
		{2, 3, 4},
		{5, 6, 7},
		{8, 9, 10}}, grid)
}
