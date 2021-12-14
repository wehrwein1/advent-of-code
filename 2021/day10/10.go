// https://adventofcode.com/2021/day/10
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

// var sum = util.SumInts
// var product = util.ProductInts
// var all = util.AllTrue
var fileLines = util.FileLinesSkipEmpty

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/10_INPUT.txt"))))
}

func computeDay(lines []string) (res int) {
	allChars := []rune{
		'(', ')',
		'[', ']',
		'{', '}',
		'<', '>'}

	for _, line := range lines {
		// println(line)
		isLineValid := true
		scanCounts := map[rune]int{}
		for _, char := range allChars {
			scanCounts[char] = 0
		}
		for lineCharIndex, char := range []rune(line) {
			scanCounts[char] += 1
			// charIndex := indexOf(allChars, char)
			// isOpen := charIndex%2 == 0

			// var openChar, closeChar rune
			// if isOpen {
			// 	openChar = char
			// 	closeChar = allChars[charIndex+1]
			// } else {
			// 	openChar = allChars[charIndex-1]
			// 	closeChar = char
			// }
			// any close > open count
			for j := 0; j < len(allChars); j += 2 {
				openChar := allChars[j]
				closeChar := allChars[j+1]
				openCount := scanCounts[openChar]
				closeCount := scanCounts[closeChar]
				if closeCount > openCount {
					println(fmt.Sprintf("line invalid '%s' at index %d: closed '%c' (%d) > open '%c' (%d)", line, lineCharIndex, closeChar, closeCount, openChar, openCount))
					isLineValid = false
					break
				}
			}

			// 	scanCounts[char] += 1
			// } else {
			// 	scanCounts[char] += 1
			// }

			if !isLineValid {
				break
			}

		}
		if isLineValid {
			println(fmt.Sprintf("line valid   '%s'", line))
		}
	}

	charValues := map[rune]int{
		')': 3,
		']': 57,
		'}': 1197,
		'>': 25137,
	}
	return charValues[')']

	// return
}

func indexOf(items []rune, char rune) int {
	for i := 0; i < len(items); i++ {
		if items[i] == char {
			return i
		}
	}
	return -1
}
