// https://adventofcode.com/2015/day/2
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

func main() {
	// solution
	area, ribbon := computeSumAreaAndRibbon(util.FileLinesSkipEmpty("../input/02_INPUT.txt"))
	println(fmt.Sprintf("part 1: square feet of wrapping paper: %d", area))
	println(fmt.Sprintf("part 2: feet of ribbon: %d", ribbon))
}

func computeSumAreaAndRibbon(lines []string) (sumArea int, sumRibbon int) {
	for _, line := range lines {
		dimensions := util.StringSplitToInts(line, "x")        // parse line
		l, w, h := dimensions[0], dimensions[1], dimensions[2] // compute
		areaOfSmallestSide := util.MinInt(l*w, l*h, w*h)
		sumArea += 2*l*w + 2*w*h + 2*h*l + areaOfSmallestSide // sum
		sumRibbon += util.SumInts(util.SortedInts(dimensions...)[:2]...)*2 + l*w*h
	}
	return // neat: return implicit values from declared signature
}
