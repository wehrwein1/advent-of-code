// https://adventofcode.com/2021/day/6
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

var parseAges = func(text string) []int { return util.StringSplitToInts(text, ",") }

func main() {
	initialAges := parseAges(util.FileContent("../input/06_INPUT.txt"))
	println(fmt.Sprintf("part 1: lanternfish count (80 days) %d", simulateLanternfish(initialAges, 80)))
}

func simulateLanternfish(testcase []int, daysCount int) (lanternfishCount int) {
	println(fmt.Sprintf("initial ages %v", testcase))
	return
}
