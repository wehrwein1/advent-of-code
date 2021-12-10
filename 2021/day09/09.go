// https://adventofcode.com/2021/day/6
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

var sum = util.SumInts
var product = util.ProductInts
var all = util.AllTrue
var fileLines = util.FileLinesSkipEmpty

func parseLines(digitLines []string) (digitRows [][]int) {
	for _, digitLine := range digitLines {
		println(digitLine)
		digitRows = append(digitRows, util.StringSplitToInts(digitLine, ""))
	}
	return
}

func main() {
	println(fmt.Sprintf("part 1: rum risk levels %d", sumRiskLevels(fileLines("../input/09_INPUT.txt"))))
	grid := parseLines(fileLines("../input/09_INPUT.txt"))
	println(fmt.Sprintf("part 2: product basin sizes %d", product(computeBasinSizes(grid, findLowPoints(grid))...)))
}

func sumRiskLevels(digitLines []string) int {
	return sum(toRiskLevels(findLowPoints(parseLines(digitLines)))...)
}

func toRiskLevels(lowPoints []LowPoint) []int {
	lowPointValues := []int{}
	for _, lowPoint := range lowPoints {
		lowPointValues = append(lowPointValues, lowPoint.Value)
	}
	return util.MapInts(lowPointValues, util.IncrementInt)
}

func findLowPoints(digitRows [][]int) (lowPoints []LowPoint) {
	rowCount := len(digitRows)
	colCount := len(digitRows[0])
	println(fmt.Sprintf("rowCount %d, colCount %d", rowCount, colCount))
	for r := 0; r < rowCount; r++ {
		for c := 0; c < colCount; c++ {
			currentValue := digitRows[r][c]
			// println(fmt.Sprintf("row %d col %d => %d", r, c, currentValue))
			neighbors := util.Int2dArrayFindNeighbors(digitRows, r, c)
			neighborValues := []int{}
			for _, neighbor := range neighbors {
				neighborValues = append(neighborValues, neighbor.Value)
			}
			isLowPoint := all(util.MapIntsToBools(neighborValues, func(value int) bool { return currentValue < value })...)
			if isLowPoint {
				lowPoints = append(lowPoints, LowPoint{Row: r, Col: c, Value: currentValue})
			}
		}
	}
	return
}

func computeBasinSizes(grid [][]int, lowPoints []LowPoint) (basinSizes []int) {
	for _, lowPoint := range lowPoints {
		println(fmt.Sprintf("%v", lowPoint))
		basinPoints := util.Int2dArrayDepthFirstSearch(grid, lowPoint.ToPoint(), isGridPointValueLessThan9)
		basinSizes = append(basinSizes, len(basinPoints))
	}
	return
}

var isGridPointValueLessThan9 = func(grid [][]int, p util.Point) bool { return grid[p.X][p.Y] < 9 }

type LowPoint struct {
	Row   int
	Col   int
	Value int
}

func (lp LowPoint) ToPoint() util.Point {
	return *util.NewPoint(lp.Row, lp.Col)
}
