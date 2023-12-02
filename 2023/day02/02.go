// https://adventofcode.com/2023/day/2
package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/wehrwein1/advent-of-code/util"
)

type ProblemPart int

const (
	Part1 ProblemPart = iota
	Part2
)

var sum = util.SumInts
var product = util.ProductInts
var fileLines = util.FileLinesSkipEmpty

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/02_INPUT.txt"), Part1)))
	println(fmt.Sprintf("part 2: %d", computeDay(fileLines("../input/02_INPUT.txt"), Part2)))
}

func computeDay(lines []string, part ProblemPart) int {
	gameValues := []int{}
	for id, game := range lines {
		maxColors := map[string]int{
			"red":   12,
			"green": 13,
			"blue":  14,
		}
		if part == Part2 {
			maxColors = map[string]int{ // note: overwrite, changed semantics
				"red":   0,
				"green": 0,
				"blue":  0,
			}
		}
		gameNumber := id + 1
		isGamePossible := true
		gameSets := strings.Split(strings.Split(game, ":")[1], ";")
		for _, gameSet := range gameSets {
			for _, draw := range strings.Split(strings.TrimSpace(gameSet), ",") {
				tokens := strings.Split(strings.TrimSpace(draw), " ")
				cubeCount, err := strconv.Atoi(tokens[0])
				if err != nil {
					panic(fmt.Sprintf("err parsing '%s' to int: %v", tokens[0], err))
				}
				cubeColor := tokens[1]
				if part == Part1 {
					isDrawPossible := cubeCount <= maxColors[cubeColor]
					isGamePossible = isGamePossible && isDrawPossible
				} else if part == Part2 {
					if cubeCount > maxColors[cubeColor] {
						maxColors[cubeColor] = cubeCount
					}
				}
			}
		}
		if part == Part1 && isGamePossible {
			println(fmt.Sprintf("Game %d possible? %v", gameNumber, isGamePossible))
			gameValues = append(gameValues, gameNumber)
		} else if part == Part2 {
			cubeSetPower := product(maxColors["red"], maxColors["blue"], maxColors["green"])
			println(fmt.Sprintf("Game %d power %d", gameNumber, cubeSetPower))
			gameValues = append(gameValues, cubeSetPower)
		}
	}
	return sum(gameValues...)
}
