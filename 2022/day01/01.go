// https://adventofcode.com/2022/day/1
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

type ProblemPart int

const (
	Part1 ProblemPart = iota
	Part2
)

var sum = util.SumInts
var fileLines = util.FileLinesIncludeEmpty

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/01_INPUT.txt"), Part1)))
	println(fmt.Sprintf("part 2: %d", computeDay(fileLines("../input/01_INPUT.txt"), Part2)))
}

func computeDay(lines []string, part ProblemPart) (res int) {
	calorieGroups := util.PartitionSliceStrings(lines)

	var counts []int
	for _, group := range calorieGroups {
		groupCalories := sum(util.StringsToInts(group)...)
		counts = append(counts, groupCalories)
		// println(groupCalories)
	}

	// part 1
	if part == Part1 {
		return util.MaxInt(counts...)
	}
	// part 2
	sorted := util.SortedInts(counts...)
	topThree := sorted[(len(sorted) - 3):]
	return sum(topThree...)
}
