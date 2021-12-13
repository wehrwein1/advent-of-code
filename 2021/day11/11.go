// https://adventofcode.com/2021/day/11
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

// var sum = util.SumInts
// var product = util.ProductInts
// var all = util.AllTrue
type If = util.If

var fileLines = util.FileLinesSkipEmpty
var AllDirections = util.AllDirections
var parseIntGrid = util.StringsToInt2dArray
var findZeroCellValue = func(g [][]int, cellValue int, p util.Point) bool { return cellValue == 0 }
var incrementCellValue = func(g [][]int, cellValue int, point util.Point) int { return If(cellValue < 9).Int(cellValue+1, 0) }

func main() {
	println(fmt.Sprintf("part 1: count of flashes %d", simulate(parseIntGrid(fileLines("../input/11_INPUT.txt")), 100)))
}

func simulate(grid [][]int, simulationCount int) (flashCount int) {
	for i := 0; i < simulationCount; i++ {
		util.Int2dArrayMap(grid, incrementCellValue)                         // += 1 everywhere
		primaryFlashes := util.Int2dArrayFindPoints(grid, findZeroCellValue) // find primary flashes
		flashCount += len(primaryFlashes)

		// TODO FIXME cascades

	}
	return
}

// func findLowPoints(digitRows [][]int) (lowPoints []LowPoint) {
// 	rowCount := util.RowCount(digitRows)
// 	colCount := util.ColCount(digitRows)
// 	println(fmt.Sprintf("rowCount %d, colCount %d", rowCount, colCount))
// 	for r := 0; r < rowCount; r++ {
// 		for c := 0; c < colCount; c++ {
// 			currentValue := digitRows[r][c]
// 			// println(fmt.Sprintf("row %d col %d => %d", r, c, currentValue))
// 			neighbors := util.Int2dArrayFindNeighbors(digitRows, r, c, AllDirections)
// 			neighborValues := []int{}
// 			for _, neighbor := range neighbors {
// 				neighborValues = append(neighborValues, neighbor.Value)
// 			}
// 			isLowPoint := all(util.MapIntsToBools(neighborValues, func(value int) bool { return currentValue < value })...)
// 			if isLowPoint {
// 				lowPoints = append(lowPoints, LowPoint{Row: r, Col: c, Value: currentValue})
// 			}
// 		}
// 	}
// 	return
// }

var isGridPointValueLessThan9 = func(grid [][]int, p util.Point) bool { return grid[p.X][p.Y] < 9 }

type LowPoint struct {
	Row   int
	Col   int
	Value int
}

func (lp LowPoint) ToPoint() util.Point {
	return *util.NewPoint(lp.Row, lp.Col)
}
