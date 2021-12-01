// https://adventofcode.com/2021/day/1
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

var toInts = util.StringsToInts

func countDepthIncreases(measurements []int) (count int) {
	for i := 1; i < len(measurements); i++ {
		if measurements[i] > measurements[i-1] {
			count += 1
		}
	}
	return
}

func countRollingWindowIncreases(measurements []int) (count int) {
	rollingMeasurements := computeWindow(measurements)
	return countDepthIncreases(rollingMeasurements)
}

func computeWindow(measurements []int) (windows []int) {
	for i := 0; i < len(measurements)-2; i++ {
		windows = append(windows, measurements[i]+measurements[i+1]+measurements[i+2]) // window length 3
	}
	return
}

func main() {
	data := toInts(util.FileLines("../input/01_INPUT.txt"))
	println(fmt.Sprintf("part 1: # depth increases: %d", countDepthIncreases(data)))
	println(fmt.Sprintf("part 2: # window increases: %d", countRollingWindowIncreases(data)))
}
