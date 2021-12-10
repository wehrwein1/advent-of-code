package util

func Int2dArrayHasValueAtPos(rowsAndCols [][]int, rowIndex int, colIndex int) (foundValue int, isFound bool) {
	rowCount := len(rowsAndCols)
	colCount := len(rowsAndCols[0])
	rowOk := (0 <= rowIndex) && (rowIndex < rowCount)
	colOk := (0 <= colIndex) && (colIndex < colCount)
	if rowOk && colOk {
		return rowsAndCols[rowIndex][colIndex], true
	}
	return 0 /* arbitrary not found value*/, false
}

func Int2dArrayFindNeighbors(rowsAndCols [][]int, rowIndex int, colIndex int) (neighbors []Int2dArrayNeighbor) {
	directions := []Direction{North, East, South, West}
	for _, direction := range directions {
		row, col := direction.Translate(rowIndex, colIndex)
		value, isFound := Int2dArrayHasValueAtPos(rowsAndCols, row, col)
		if isFound {
			neighbors = append(neighbors, Int2dArrayNeighbor{Row: row, Col: col, Value: value, Direction: direction})
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
