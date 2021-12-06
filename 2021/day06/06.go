// https://adventofcode.com/2021/day/6
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

func main() {
	initialAges := util.FileContent("../input/06_INPUT.txt")
	println(fmt.Sprintf("part 1: lanternfish count (80 days) %d", len(simulateLanternfish(initialAges, 80))))
}

func simulateLanternfish(agesCsv string, daysCount int) []int {
	ages := util.StringSplitToInts(agesCsv, ",")
	// println(fmt.Sprintf("Initial state: %v", ages))
	for i := 0; i < daysCount; i++ {
		appendCount := 0
		for j := 0; j < len(ages); j++ {
			if ages[j] == 0 {
				ages[j] = 6
				appendCount += 1
			} else {
				ages[j] = ages[j] - 1
			}
		}
		for c := 0; c < appendCount; c++ {
			ages = append(ages, 8)
		}
		// println(fmt.Sprintf("After %3d days: %v", (i + 1), ages))
	}
	return ages
}
