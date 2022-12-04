package util

import "github.com/wehrwein1/advent-of-code/util/ds"

func Int2dArrayHasValueAtPos(rowsAndCols [][]int, rowIndex int, colIndex int) (foundValue int, isFound bool) {
	rowOk := (0 <= rowIndex) && (rowIndex < RowCount(rowsAndCols))
	colOk := (0 <= colIndex) && (colIndex < ColCount(rowsAndCols))
	if rowOk && colOk {
		return rowsAndCols[rowIndex][colIndex], true
	}
	return 0 /* arbitrary not found value*/, false
}

func Int2dArrayFindNeighbors(rowsAndCols [][]int, rowIndex int, colIndex int, directions []Direction) (neighbors []Int2dArrayNeighbor) {
	for _, direction := range directions {
		row, col := direction.Translate(rowIndex, colIndex)
		value, isFound := Int2dArrayHasValueAtPos(rowsAndCols, row, col)
		if isFound {
			neighbors = append(neighbors, Int2dArrayNeighbor{Row: row, Col: col, Value: value, Direction: direction})
		}
	}
	return
}

func Int2dArrayDepthFirstSearch(rowsAndCols [][]int, startAt Point, canTraverse func(grid [][]int, point Point) bool, searchDirections []Direction) []Point {
	visited := ds.NewSet[Point]()
	reachablePoints := ds.NewSet[Point]()
	queue := ds.NewQueue[Point](len(rowsAndCols) * len(rowsAndCols[0])) // safe assumption for now
	queue.Enqueue(startAt)
	for !queue.IsEmpty() {
		point := queue.Dequeue()
		neighbors := Int2dArrayFindNeighbors(rowsAndCols, point.X, point.Y, searchDirections)
		for _, neighbor := range neighbors {
			neighborPoint := *NewPoint(neighbor.Row, neighbor.Col)
			canTraverse := !visited.Has(neighborPoint) && canTraverse(rowsAndCols, neighborPoint)
			if canTraverse {
				reachablePoints.Put(neighborPoint)
				queue.Enqueue(neighborPoint) // continue DFS
			} else {
				visited.Put(neighborPoint)
			}
		}
		visited.Put(point) // mark current as visited
	}
	keys := reachablePoints.Keys()
	return keys
}

func Int2dArrayMap(rowsAndCols [][]int, mapFunction func(grid [][]int, cellValue int, p Point) int) {
	rowCount := RowCount(rowsAndCols)
	colCount := ColCount(rowsAndCols)
	for r := 0; r < rowCount; r++ {
		for c := 0; c < colCount; c++ {
			rowsAndCols[r][c] = mapFunction(rowsAndCols, rowsAndCols[r][c], *NewPoint(r, c))
		}
	}
}

func Int2dArrayFindPoints(grid [][]int, selector func(g [][]int, cellValue int, p Point) bool) (matchedPoints []Point) {
	rowCount := RowCount(grid)
	colCount := ColCount(grid)
	for r := 0; r < rowCount; r++ {
		for c := 0; c < colCount; c++ {
			p := *NewPoint(r, c)
			if selector(grid, grid[r][c], p) {
				matchedPoints = append(matchedPoints, p)
			}
		}
	}
	return
}

type Int2dArrayNeighbor struct {
	Row       int
	Col       int
	Value     int       // coordinate position value
	Direction Direction // coordinate position relative to external origin
}

func RowCount(grid [][]int) int {
	return len(grid)
}

func ColCount(grid [][]int) int {
	return len(grid[0])
}
