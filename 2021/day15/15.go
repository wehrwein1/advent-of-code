// https://adventofcode.com/2021/day/15
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"

	"gonum.org/v1/gonum/graph/path"
)

var fileLines = util.FileLinesSkipEmpty

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/15_INPUT.txt"))))
}

func computeDay(lines []string) (res int) {
	for _, line := range lines {
		println(line)
	}

	path.DijkstraAllPaths(nil)

	return
}
