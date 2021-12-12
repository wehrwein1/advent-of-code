// https://adventofcode.com/2021/day/9
package main

import (
	"fmt"
	"sort"

	"github.com/wehrwein1/advent-of-code/util"
)

var sum = util.SumInts
var product = util.ProductInts
var all = util.AllTrue
var fileLines = util.FileLinesSkipEmpty
var NESW = util.PrimaryFourDirections
var parseIntGrid = util.StringsToInt2dArray

func main() {
	println(fmt.Sprintf("part 1: rum risk levels %d", sumRiskLevels(fileLines("../input/09_INPUT.txt"))))
	grid := parseIntGrid(fileLines("../input/09_INPUT.txt"))
	println(fmt.Sprintf("part 2: product basin sizes %d", product(threeLargest(computeBasinSizes(grid, findLowPoints(grid)))...)))
}

func sumRiskLevels(digitLines []string) int {
	return sum(toRiskLevels(findLowPoints(parseIntGrid(digitLines)))...)
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
			neighbors := util.Int2dArrayFindNeighbors(digitRows, r, c, NESW)
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

var isGridPointValueLessThan9 = func(grid [][]int, p util.Point) bool { return grid[p.X][p.Y] < 9 }

func computeBasinSizes(grid [][]int, lowPoints []LowPoint) (basinSizes []int) {
	for _, lowPoint := range lowPoints {
		basinPoints := util.Int2dArrayDepthFirstSearch(grid, lowPoint.ToPoint(), isGridPointValueLessThan9, NESW)
		basinSizes = append(basinSizes, len(basinPoints)+1) // (+1 for DFS start point = low point = omitted from DFS results)
		println(fmt.Sprintf("lowPoint %v basinSize %d", lowPoint, basinSizes[len(basinSizes)-1]))
	}
	return
}

func threeLargest(numbers []int) []int {
	sort.Ints(numbers)
	return numbers[len(numbers)-3:]
}

type LowPoint struct {
	Row   int
	Col   int
	Value int
}

func (lp LowPoint) ToPoint() util.Point {
	return *util.NewPoint(lp.Row, lp.Col)
}
