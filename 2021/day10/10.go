// https://adventofcode.com/2021/day/10
package main

import (
	"fmt"
	"sort"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/ds"
	"github.com/wehrwein1/advent-of-code/util/lang"
)

type LineResult int

const (
	Valid      LineResult = iota // 0
	Corrupt                      // 1
	Incomplete                   // 2
)

type If = lang.If

var fileLines = util.FileLinesSkipEmpty
var openCloseChars = []rune{
	'(', ')',
	'[', ']',
	'{', '}',
	'<', '>'}
var invalidCharValues = map[rune]int{
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137}
var completionStringValues = map[rune]int{
	')': 1,
	']': 2,
	'}': 3,
	'>': 4}

func main() {
	println(fmt.Sprintf("part 1: sum syntax error score %d", sumSyntaxErrorScore(fileLines("../input/10_INPUT.txt")...)))
	println(fmt.Sprintf("part 2: middle completion score %d", middleCompletionStringScore(fileLines("../input/10_INPUT.txt")...)))
}

func sumSyntaxErrorScore(lines ...string) (syntaxErrorScore int) {
	for _, line := range lines {
		lineResult, invalidIndex, expectedChar := evaluateLine(line, ds.NewStack[rune]())
		switch lineResult {
		case Valid:
			println(fmt.Sprintf("line valid   '%s'", line))
		case Corrupt:
			illegalChar := line[invalidIndex]
			println(fmt.Sprintf("line corrupt '%s' at index %d: expected: %c, was: %c", line, invalidIndex, expectedChar, illegalChar))
			syntaxErrorScore += invalidCharValues[rune(illegalChar)]
		case Incomplete:
			println(fmt.Errorf("not implemented: %v", lineResult))
		default:
			println(fmt.Errorf("unhandled case: %v", lineResult))
		}
	}
	return
}

func middleCompletionStringScore(lines ...string) (middleScore int) {
	scores := []int{}
	for _, line := range lines {
		closes := ds.NewStack[rune]()
		lineResult, _, _ := evaluateLine(line, closes)
		if lineResult == Incomplete {
			chars := []rune{}
			for !closes.IsEmpty() {
				chars = append(chars, closes.Pop())
			}
			completionString := string(chars)
			scores = append(scores, completionStringScore(completionString))
		}
	}
	sort.Ints(scores)
	return scores[len(scores)/2]
}

func completionStringScore(completionString string) (score int) {
	for _, char := range completionString {
		score *= 5
		score += completionStringValues[char]
	}
	return score
}

func evaluateLine(line string, closes *ds.Stack[rune]) (valid LineResult, invalidIndex int, expectedChar rune) {
	for lineCharIndex, char := range []rune(line) {
		charIndex := indexOf(openCloseChars, char)
		isOpen := charIndex%2 == 0
		if isOpen {
			closeChar := openCloseChars[charIndex+1]
			closes.Push(closeChar)
		} else {
			expectedClose := closes.Pop()
			if char != expectedClose {
				return Corrupt, lineCharIndex, expectedClose
			}
		}
	}
	if closes.IsEmpty() {
		return Valid, -1, -1
	} else {
		return Incomplete, len(line), closes.Peek()
	}
}

func indexOf(items []rune, char rune) int {
	for i := 0; i < len(items); i++ {
		if items[i] == char {
			return i
		}
	}
	return -1
}
