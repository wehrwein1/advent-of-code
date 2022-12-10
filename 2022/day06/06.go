// https://adventofcode.com/2022/day/6
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/ds"
	"github.com/wehrwein1/advent-of-code/util/lang"
)

type ProblemPart int

const (
	Part1 ProblemPart = iota
	Part2
)

type If = lang.If

var fileLines = util.FileLinesSkipEmpty

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/06_INPUT.txt"), Part1)))
	println(fmt.Sprintf("part 2: %d", computeDay(fileLines("../input/06_INPUT.txt"), Part2)))
}

func computeDay(lines []string, part ProblemPart) (startOfPacketMarker int) {
	signal := lines[0]
	println(signal)
	markerLength := If(part == Part1).Int(4, 14)
	for i := 0; i < len(signal)-markerLength+1; i++ {
		buffer := signal[i : i+markerLength]
		isMarker := isMarker(buffer)
		println(fmt.Sprintf("buffer[%d] %s -> %t", i, string(buffer), isMarker))
		if isMarker {
			return i + markerLength
		}
	}
	return startOfPacketMarker
}

func isMarker(buffer string) bool {
	chars := ds.NewSet[rune]()
	markerLength := len(buffer)
	for i := 0; i < markerLength; i++ {
		chars.Put(rune(buffer[i]))
	}
	return chars.Len() == markerLength
}
