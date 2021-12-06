// https://adventofcode.com/2021/day/6
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

func main() {
	initialAges := util.FileContent("../input/06_INPUT.txt")
	println(fmt.Sprintf("part 1: lanternfish count (80 days) %d", len(simulateLanternfish(initialAges, 80))))
	println(fmt.Sprintf("part 2: lanternfish count (256 days) %d", simulateLanternfishCount(initialAges, 256)))
}

var sum = util.SumInts

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
		// println(fmt.Sprintf("iteration %2d, len(ages)=%d incl added=%d", (i + 1), len(ages), appendCount))
		// println(fmt.Sprintf("After %3d days: %v", (i + 1), ages))
	}
	return ages
}

// part 2 - vastly improved memory usage
func simulateLanternfishCount(agesCsv string, daysCount int) int {
	// populate counts from input
	ageCounts := make([]int, 9)
	for i := range ageCounts {
		ageCounts[i] = 0
	}
	for _, age := range util.StringSplitToInts(agesCsv, ",") {
		ageCounts[age] += 1
	}
	// iterate days
	for i := 0; i < daysCount; i++ {
		newSixesCount := ageCounts[0]   // all 0->6
		newEightsCount := newSixesCount // +1 8 for each 0->6
		// shuffle down
		ageCounts[0] = ageCounts[1]
		ageCounts[1] = ageCounts[2]
		ageCounts[2] = ageCounts[3]
		ageCounts[3] = ageCounts[4]
		ageCounts[4] = ageCounts[5]
		ageCounts[5] = ageCounts[6]
		ageCounts[6] = ageCounts[7] + newSixesCount
		ageCounts[7] = ageCounts[8]
		ageCounts[8] = newEightsCount
		println(fmt.Sprintf("iteration %4d ageCounts= %v", i+1, ageCounts))
	}
	return sum(ageCounts...)
}
