// https://adventofcode.com/2021/day/3
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/lang"
)

// var check = util.Check
// var product = util.ProductInts
var binToDec = util.BinaryStringToDecimal

func computePowerConsumption(diagnostics []string) (gamma, epsilon string, product int64) {
	bits := len(diagnostics[0]) // max # bits
	println(fmt.Sprintf("#bits %d", bits))
	gamma = ""   // ones
	epsilon = "" // zeroes
	for i := 0; i < bits; i++ {
		countOnes, countZeroes := countOnesAndZeroes(diagnostics, i)
		moreOnes := countOnes > countZeroes
		gamma += lang.If(moreOnes, "1", "0")
		epsilon += lang.If(moreOnes, "0", "1")
		println(fmt.Sprintf("i=%d ones=%d zeroes=%d, gamma=%s, epsison=%s", i, countOnes, countZeroes, gamma, epsilon))
	}
	product = binToDec(gamma, 32) * binToDec(epsilon, 32)
	return
}

var oxygenSelector = func(countOnes, countZeroes int) rune { return lang.If(countOnes >= countZeroes, '1', '0') }
var co2Selector = func(countOnes, countZeroes int) rune { return lang.If(countOnes >= countZeroes, '0', '1') }

func computeRatings(diagnostics []string) (oxygen, co2 string, product int64) {
	bits := len(diagnostics[0]) // max # bits
	println(fmt.Sprintf("#bits %d", bits))
	oxygen = computeRating(diagnostics, "mostCommon/oxygen", oxygenSelector)
	co2 = computeRating(diagnostics, "leastCommon/co2", co2Selector)
	product = binToDec(oxygen, 32) * binToDec(co2, 32)
	return
}

func computeRating(diagnostics []string, selectionName string, selector func(int, int) rune) (rating string) {
	bits := len(diagnostics[0]) // max # bits
	for i := 0; i < bits; i++ {
		countOnes, countZeroes := countOnesAndZeroes(diagnostics, i)
		selection := selector(countOnes, countZeroes)
		diagnostics = util.StringsFilter(diagnostics, func(s string) bool { return s[i] == byte(selection) })
		println(fmt.Sprintf("%s i=%d remaining = %v", selectionName, i, diagnostics))
		if len(diagnostics) == 1 {
			return diagnostics[0]
		}
	}
	panic(fmt.Sprintf("what to do? multiple remain: %v", diagnostics))
}

func main() {
	diagnostics := util.FileLinesSkipEmpty("../input/03_INPUT.txt")
	{
		gamma, epsilon, product := computePowerConsumption(diagnostics)
		println(fmt.Sprintf("part 1: gamma %s epsilon %s power consumption %d", gamma, epsilon, product))
	}
	{
		oxygen, co2, product := computeRatings(diagnostics)
		println(fmt.Sprintf("part 2: oxygen %s co2 %s life support %d", oxygen, co2, product))
	}
}

func countOnesAndZeroes(diagnostics []string, index int) (countOnes, countZeroes int) {
	for _, reading := range diagnostics {
		if reading[index] == '0' {
			countZeroes += 1
		} else {
			countOnes += 1
		}
	}
	return
}
