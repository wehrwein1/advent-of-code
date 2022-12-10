// https://adventofcode.com/2022/day/5
package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/ds"
)

type ProblemPart int

const (
	Part1 ProblemPart = iota
	Part2
)

var fileLines = util.FileLinesIncludeEmpty

func main() {
	println(fmt.Sprintf("part 1: %s", computeDay(fileLines("../input/05_INPUT.txt"), 9, Part1)))
	println(fmt.Sprintf("part 2: %s", computeDay(fileLines("../input/05_INPUT.txt"), 9, Part2)))
}

func computeDay(lines []string, stacksCount int, part ProblemPart) string {
	for _, line := range lines {
		println(line)
	}
	// set state
	stacks, moves := parseInitialState(lines, stacksCount)
	// moves
	for _, move := range moves {
		// parse move line
		tokens := strings.Split(move, " ")
		moveCount := parseInt(tokens[1])
		sourceStackNumber := parseInt(tokens[3])
		targetStackNumber := parseInt(tokens[5])
		// do move
		sourceStack := stacks[sourceStackNumber-1]
		targetStack := stacks[targetStackNumber-1]
		i := 0
		if part == Part1 || moveCount == 1 {
			for i < moveCount {
				targetStack.Push(sourceStack.Pop())
				i++
			}
		} else if part == Part2 {
			tempStack := ds.NewStack[rune]()
			for i < moveCount {
				tempStack.Push(sourceStack.Pop())
				i++
			}
			for !tempStack.IsEmpty() {
				targetStack.Push(tempStack.Pop())
			}
		}
	}
	return string(getTopItems(stacks))
}

func parseInitialState(lines []string, stacksCount int) (stacks []*ds.Stack[rune], moves []string) {
	// state
	tempStacks := []*ds.Stack[rune]{}
	for i := 0; i < stacksCount; i++ {
		tempStacks = append(tempStacks, ds.NewStack[rune]())
	}
	// populate state
	lineIndex := 0
	cratePadding := len("] [") + 1
	for _, line := range lines {
		if isCrateDisplayRow(line) {
			break
		}
		crateIndex := 0
		for charIndex := 1; charIndex < len(line)-1; charIndex += cratePadding {
			crate := string(line[charIndex])
			if crate != " " {
				tempStacks[crateIndex].Push(rune(crate[0]))
			}
			crateIndex += 1
		}
		lineIndex += 1
	}
	lineIndex += 1 // skip the display line
	// parse moves
	for i := lineIndex; i < len(lines); i++ {
		if lines[i] != "" {
			moves = append(moves, lines[i])
		}
	}

	// unpack state / build stacks
	for i := 0; i < stacksCount; i++ {
		stacks = append(stacks, ds.NewStack[rune]())
	}
	// populate stacks
	for i := 0; i < stacksCount; i++ {
		for !tempStacks[i].IsEmpty() {
			stacks[i].Push(tempStacks[i].Pop())
		}
	}
	return stacks, moves
}

func isCrateDisplayRow(line string) bool {
	_, err := strconv.Atoi(strings.TrimSpace(line[1:3]))
	is_number := err == nil
	return is_number
}

func getTopItems(stacks []*ds.Stack[rune]) []rune {
	topItems := []rune{}
	for _, stack := range stacks {
		topItems = append(topItems, stack.Peek())
	}
	return topItems
}

func parseInt(text string) int {
	val, err := strconv.Atoi(text)
	if err != nil {
		panic(err)
	}
	return val
}
