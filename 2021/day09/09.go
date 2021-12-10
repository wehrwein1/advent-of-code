// https://adventofcode.com/2021/day/6
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

var sum = util.SumInts
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
}

func sumRiskLevels(digitLines []string) int {
	return sum(toRiskLevels(findLowPoints(parseLines(digitLines)))...)
}

func toRiskLevels(lowPoints []int) []int {
	return util.MapInts(lowPoints, util.IncrementInt)
}

func findLowPoints(digitRows [][]int) (lowPoints []int) {
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
				lowPoints = append(lowPoints, currentValue)
			}
		}
	}
	return
}
