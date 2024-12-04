// https://adventofcode.com/2022/day/4
package main

import (
	"fmt"
	"strings"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/lang"
)

type ProblemPart int

const (
	Part1 ProblemPart = iota
	Part2
)

var fileLines = util.FileLinesSkipEmpty

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/04_INPUT.txt"), Part1)))
	println(fmt.Sprintf("part 2: %d", computeDay(fileLines("../input/04_INPUT.txt"), Part2)))
}

func computeDay(lines []string, part ProblemPart) (count int) {
	for _, line := range lines {
		sections := strings.Split(line, ",")
		is_overlap := lang.If(part == Part1, sectionContainsOther(sections), sectionsOverlapAtAll(sections))
		println(fmt.Sprintf("%s -> %v --> %t", line, sections, is_overlap))
		if is_overlap {
			count += 1
		}
	}
	return count
}

func sectionContainsOther(sections []string) bool {
	sections1 := util.StringSplitToInts(sections[0], "-")
	sections2 := util.StringSplitToInts(sections[1], "-")
	start1, end1 := sections1[0], sections1[1]
	start2, end2 := sections2[0], sections2[1]
	return (start1 <= start2 && end1 >= end2) ||
		(start2 <= start1 && end2 >= end1)

}

func sectionsOverlapAtAll(sections []string) bool {
	sections1 := util.StringSplitToInts(sections[0], "-")
	sections2 := util.StringSplitToInts(sections[1], "-")
	start1, end1 := sections1[0], sections1[1]
	start2, end2 := sections2[0], sections2[1]
	return start1 <= end2 && end1 >= start2
}
