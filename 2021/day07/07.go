// https://adventofcode.com/2021/day/7
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/lang"
)

var min = util.MinInt
var indexOf = util.IntSliceIndexOf

var parsePositions = func(positionsCsv string) []int { return util.StringSplitToInts(positionsCsv, ",") }

func main() {
	positions := parsePositions(util.FileContent("../input/07_INPUT.txt"))
	_, sumFuelPart1 := computeMinFuel(positions, constantFuelUse)
	println(fmt.Sprintf("part 1: sum fuel %d", sumFuelPart1))
	_, sumFuelPart2 := computeMinFuel(positions, linearIncreaseFuelUse)
	println(fmt.Sprintf("part 2: sum fuel %d", sumFuelPart2))
}

var constantFuelUse = func(crabPos int, pos int) int { return lang.If(crabPos > pos, crabPos-pos, pos-crabPos) }

func linearIncreaseFuelUse(crabPos int, pos int) (total int) {
	distance := constantFuelUse(crabPos, pos)
	inc := 1
	for i := 0; i < distance; i++ {
		total += inc
		inc++
	}
	return
}

func computeMinFuel(crabPositions []int, fuelUseFunc func(crabPos int, pos int) int) (int, int) {
	minPos := util.MinInt(crabPositions...)
	maxPos := util.MaxInt(crabPositions...)
	println(fmt.Sprintf("initial crab positions range [%d,%d]", minPos, maxPos))
	println(fmt.Sprintf("initial crab positions %v", crabPositions))
	minFuelAtPos := make([]int, maxPos+1)
	for i := range minFuelAtPos {
		minFuelAtPos[i] = -1
	}
	for pos := minPos; pos < maxPos+1; pos++ {
		if minFuelAtPos[pos] > 0 {
			continue // already did this positions
		}
		sumFuel := 0
		for i := 0; i < len(crabPositions); i++ {
			crabPos := crabPositions[i]
			fuel := fuelUseFunc(crabPos, pos)
			// println(fmt.Sprintf("Move %d -> %d = %d fuel", crabPos, pos, fuel))
			sumFuel += fuel
		}
		minFuelAtPos[pos] = sumFuel
		// println(fmt.Sprintf("Sum fuel at pos=%d -> %d", pos, sumFuel))
	}

	minValue := min(minFuelAtPos...)
	minFuelPos := indexOf(minFuelAtPos, func(val int) bool { return val == minValue })
	return minFuelPos, minValue
}
