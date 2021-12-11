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

func Int2dArrayDepthFirstSearch(rowsAndCols [][]int, startAt Point, canTraverse func(grid [][]int, point Point) bool) []Point {
	visited := NewPointSet()
	reachablePoints := NewPointSet()
	queue := NewPointQueue(len(rowsAndCols) * len(rowsAndCols[0])) // safe assumption for now
	queue.push(startAt)
	for queue.length() > 0 {
		point := queue.pop()
		neighbors := Int2dArrayFindNeighbors(rowsAndCols, point.X, point.Y)
		for _, neighbor := range neighbors {
			neighborPoint := *NewPoint(neighbor.Row, neighbor.Col)
			canTraverse := !visited.has(neighborPoint) && canTraverse(rowsAndCols, neighborPoint)
			if canTraverse {
				reachablePoints.put(neighborPoint)
				queue.push(neighborPoint) // continue DFS
			} else {
				visited.put(neighborPoint)
			}
		}
		visited.put(point) // mark current as visited
	}
	i := 0 // all this to read map.keys()
	keys := make([]Point, len(reachablePoints.data))
	for k := range reachablePoints.data {
		keys[i] = k
		i++
	}
	return keys
}

type Int2dArrayNeighbor struct {
	Row       int
	Col       int
	Value     int       // coordinate position value
	Direction Direction // coordinate position relative to external origin
}

type PointQueue struct { // would generalize further if had generics
	data chan Point
}

func NewPointQueue(capacity int) *PointQueue {
	return &PointQueue{data: make(chan Point, 1000)}
}

func (queue PointQueue) push(val Point) {
	queue.data <- val
}

func (queue PointQueue) pop() Point {
	return <-queue.data
}

func (queue PointQueue) length() int {
	return len(queue.data)
}

type PointSet struct { // would generalize further if had generics
	data map[Point]bool
}

func NewPointSet() *PointSet {
	return &PointSet{data: make(map[Point]bool)}
}

func (s PointSet) put(val Point) {
	s.data[val] = true
}

func (s PointSet) has(val Point) bool {
	_, ok := s.data[val]
	return ok
}
