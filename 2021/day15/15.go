// https://adventofcode.com/2021/day/15
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

var fileLines = util.FileLinesSkipEmpty

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/15_INPUT.txt"))))
}

// Dijkstra example https://golang.hotexamples.com/examples/github.com.gonum.graph.path/-/DijkstraAllPaths/golang-dijkstraallpaths-function-examples.html
func computeDay(lines []string) (res int) {
	for _, line := range lines {
		println(line)
	}
	return
}
