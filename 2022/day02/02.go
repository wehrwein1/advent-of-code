// https://adventofcode.com/2022/day/2
package main

import (
	"fmt"
	"strings"

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
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/02_INPUT.txt"), Part1)))
	println(fmt.Sprintf("part 2: %d", computeDay(fileLines("../input/02_INPUT.txt"), Part2)))
}

func computeDay(lines []string, part ProblemPart) (res int) {
	roundScores := []int{}
	for _, line := range lines {

		// parse line
		tokens := strings.Split(line, " ")
		opponentShape, yourShape := tokens[0], tokens[1]

		// evaluate round
		roundScore := computeRound(opponentShape, yourShape, part)
		println(fmt.Sprintf("%s -> %d", line, roundScore))
		roundScores = append(roundScores, roundScore)
	}
	return sum(roundScores...)
}

func computeRound(opponentShape string, yourShape string, part ProblemPart) int {
	// evaluate round score
	opponentScore := 0
	if opponentShape == "A" {
		opponentScore = 1 // TODO FIXME better: enum
	} else if opponentShape == "B" {
		opponentScore = 2
	} else if opponentShape == "C" {
		opponentScore = 3
	}

	is_win, is_draw := false, false
	yourScore := 0
	if part == Part1 {
		// part 1
		if yourShape == "X" {
			yourScore = 1
		} else if yourShape == "Y" {
			yourScore = 2
		} else if yourShape == "Z" {
			yourScore = 3
		}
		is_win, is_draw = evaluateScore(opponentScore, yourScore)
	} else {
		// part 2
		need_lose := yourShape == "X"
		need_draw := yourShape == "Y"
		need_win := yourShape == "Z"
		if need_draw {
			yourScore = opponentScore
			is_win, is_draw = false, true
		} else if need_lose {
			if opponentScore == 1 {
				yourScore = 3 // opponent rock beats scissors
			} else if opponentScore == 2 {
				yourScore = 1 // opponent paper beats rock
			} else if opponentScore == 3 {
				yourScore = 2 // opponent scissors beats paper
			}
			is_win, is_draw = false, false
		} else if need_win {
			if opponentScore == 1 {
				yourScore = 2 // your paper beats rock
			} else if opponentScore == 2 {
				yourScore = 3 // your scissors beats paper
			} else if opponentScore == 3 {
				yourScore = 1 // your rock beats scissors
			}
			is_win, is_draw = true, false
		}
	}

	lineScore := yourScore
	if is_win {
		lineScore += 6
	} else if is_draw {
		lineScore += 3
	}
	return lineScore
}

func evaluateScore(opponentScore, yourScore int) (is_win, is_draw bool) {
	if yourScore == 1 && opponentScore == 3 { // special case: your rock beats scissors
		is_win = true
	} else if yourScore == 3 && opponentScore == 1 { // special case: opponent rock beats scissors
		is_win = false
	} else {
		is_win = yourScore > opponentScore
	}
	if !is_win {
		is_draw = yourScore == opponentScore
	}
	return is_win, is_draw
}
