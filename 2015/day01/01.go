// https://adventofcode.com/2015/day/1
package main

import (
	"strings"

	"github.com/wehrwein1/advent-of-code/util"
)

func main() {
	steps := util.FileContent("../input/01_INPUT.txt")
	UP, DOWN := "(", ")"
	println("part 1: Santa ends on floor:", strings.Count(steps, UP)-strings.Count(steps, DOWN))
	floor := 0
	i := 0
	for floor >= 0 {
		delta := 0
		if string(steps[i]) == UP {
			delta = 1
		} else {
			delta = -1
		}
		floor += delta
		i += 1
	}
	println("part 2: Santa first goes to basement on step:", i)
}
