// https://adventofcode.com/2021/day/6
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

var parsePositions = func(positionsCsv string) []int { return util.StringSplitToInts(positionsCsv, ",") }

func main() {
	positions := parsePositions(util.FileContent("../input/07_INPUT.txt"))
	_, sumFuel := computeMinFuel(positions)
	println(fmt.Sprintf("part 1: sum fuel %d", sumFuel))
}

func computeMinFuel(positions []int) (int, int) {
	minFuelPos := 0
	sumFuel := 0
	return minFuelPos, sumFuel
}
