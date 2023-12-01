// https://adventofcode.com/2023/day/1
package main

import (
	"fmt"
	"strconv"

	"github.com/wehrwein1/advent-of-code/util"
)

type ProblemPart int

const (
	Part1 ProblemPart = iota
	Part2
)

var sum = util.SumInts
var fileLines = util.FileLinesSkipEmpty

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/01_INPUT.txt"), Part1)))
	println(fmt.Sprintf("part 2: %d", computeDay(fileLines("../input/01_INPUT.txt"), Part2)))
}

func computeDay(lines []string, part ProblemPart) int {
	calibrationValues := []int{}
	digitsSpelled := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
	for _, line := range lines {
		ints := []int{}
		for i, c := range line {
			intVal, err := strconv.Atoi(string(c))
			isNumericDigit := err == nil
			isWordDigit := false
			if !isNumericDigit && part == Part2 {
				for word, wordVal := range digitsSpelled {
					if util.StringStartsWith(line[i:], word) {
						isWordDigit = true
						intVal = wordVal
						i += len(word) - 1
						break
					}
				}
			}
			if isNumericDigit || isWordDigit {
				ints = append(ints, intVal)
			}
		}
		calibrationValue := 10*ints[0] + ints[len(ints)-1]
		calibrationValues = append(calibrationValues, calibrationValue)
	}
	return sum(calibrationValues...)
}
