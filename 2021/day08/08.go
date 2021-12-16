// https://adventofcode.com/2021/day/8
package main

import (
	"fmt"
	"strings"

	"github.com/wehrwein1/advent-of-code/util"
)

var fileLines = util.FileLinesSkipEmpty
var part1CountedDigits = []Digit{One, Four, Seven, Eight}

func main() {
	lines := fileLines("../input/08_INPUT.txt")
	println(fmt.Sprintf("part 1: count of (1,4,7,8): %d", countSelectedDigits(lines, part1CountedDigits...)))
	println(fmt.Sprintf("part 2: sum output values: %d", sumOutputValues(lines)))
}

func countSelectedDigits(lines []string, countedDigits ...Digit) (count int) {
	for _, line := range lines {
		tokens := strings.Split(line, " | ")
		outputSignals := tokens[1]
		outputSignalTokens := strings.Split(outputSignals, " ")
		for _, outputSignalToken := range outputSignalTokens {
			outputSignalLen := len(outputSignalToken)
			for _, countedDigit := range countedDigits {
				if countedDigit.SegmentCount() == outputSignalLen {
					count += 1
				}
			}
		}
	}
	return
}

func sumOutputValues(lines []string) (sumOutputValues int) {
	for _, line := range lines {
		_, outputValue := decodeSignal(line)
		sumOutputValues += outputValue
	}
	return
}

func decodeSignal(line string) (signalPatterns map[string]int, outputValue int) {
	signalPatterns = make(map[string]int)
	outputValues := []int{1} // TODO FIXME
	return signalPatterns, util.IntSliceToDigitsValue(outputValues)
}

type Digit int

const (
	Zero Digit = iota
	One
	Two
	Three
	Four
	Five
	Six
	Seven
	Eight
	Nine
)

var digitSegmentCounts = map[Digit]int{
	Zero:  6,
	One:   2, // unique count
	Two:   5,
	Three: 5,
	Four:  4, // unique count
	Five:  5,
	Six:   6,
	Seven: 3, // unique count
	Eight: 7, // unique count
	Nine:  6,
}

func (d Digit) SegmentCount() int {
	return digitSegmentCounts[d]
}
