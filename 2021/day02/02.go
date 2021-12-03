// https://adventofcode.com/2021/day/2
package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/wehrwein1/advent-of-code/util"
)

var check = util.Check
var product = util.ProductInts

func computePositionPart1(commands []string) (horizontal int, vertical int) {
	for i, command := range commands {
		tokens := strings.Split(command, " ")
		operation := tokens[0]
		distance, err := strconv.Atoi(tokens[1])
		check(err)
		switch operation {
		case "up":
			vertical -= distance
		case "down":
			vertical += distance
		case "forward":
			horizontal += distance
		default:
			panic(fmt.Sprintf("unhandled case: %s", operation))
		}
		println(fmt.Sprintf("part1/%d    '%s' -> (%d,%d)", i, command, horizontal, vertical))
	}
	return
}

func computePositionPart2(commands []string) (horizontal int, vertical int) {
	aim := 0
	for i, command := range commands {
		tokens := strings.Split(command, " ")
		operation := tokens[0]
		distance, err := strconv.Atoi(tokens[1])
		check(err)
		switch operation {
		case "up":
			// vertical -= distance // part 2 difference
			aim -= distance // part 2
		case "down":
			// vertical += distance // part 2 difference
			aim += distance // part 2
		case "forward":
			horizontal += distance
			vertical += (aim * distance) // part 2
		default:
			panic(fmt.Sprintf("unhandled case: %s", operation))
		}
		println(fmt.Sprintf("part2/%d    '%s' -> (h,v)=(%d,%d), aim=%d", i, command, horizontal, vertical, aim))
	}
	return
}

func main() {
	commands := util.FileLines("../input/02_INPUT.txt")
	println(fmt.Sprintf("part 1: product of position: %d", product(computePositionPart1(commands))))
	println(fmt.Sprintf("part 2: product of position: %d", product(computePositionPart2(commands))))
}
