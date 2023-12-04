// https://adventofcode.com/2023/day/4
package main

import (
	"fmt"
	"strings"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/ds"
)

type ProblemPart int

const (
	Part1 ProblemPart = iota
	Part2
)

var sum = util.SumInts
var fileLines = util.FileLinesSkipEmpty

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/04_INPUT.txt"), Part1)))
	// println(fmt.Sprintf("part 2: %d", computeDay(fileLines("../input/04_INPUT.txt"), Part2)))
}

func computeDay(lines []string, part ProblemPart) int {
	scratchcardValues := []int{}
	for i, card := range lines {
		// parse card
		tokens := strings.Split(strings.TrimSpace(strings.Split(card, ":")[1]), "|")
		winningNumberPart := strings.TrimSpace(strings.TrimSpace(tokens[0]))
		yourNumbersPart := strings.TrimSpace(tokens[1])
		winningNumbers := util.StringSplitToIntsWhitespace(winningNumberPart)
		scratchcardNumbers := ds.NewSet(util.StringSplitToIntsWhitespace(yourNumbersPart)...)

		cardSum := 0
		// winValue := 1
		isFirstWin := true
		// println(fmt.Sprintf(" winners: %v", winningNumbers))
		// println(fmt.Sprintf(" cards  : %v", cardNumbers.Keys()))
		for _, winningNumber := range winningNumbers {
			if scratchcardNumbers.Has(winningNumber) {
				if isFirstWin {
					cardSum = 1
					isFirstWin = false
				} else {
					cardSum *= 2
				}
			}
		}
		println(fmt.Sprintf("Card %d points %d", i+1, cardSum))
		scratchcardValues = append(scratchcardValues, cardSum)
	}
	return sum(scratchcardValues...)
}
