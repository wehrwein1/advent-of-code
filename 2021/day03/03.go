// https://adventofcode.com/2021/day/3
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

// var check = util.Check
// var product = util.ProductInts
var binToDec = util.BinaryStringToDecimal

type If = util.If

func computePowerConsumption(diagnostics []string) (gamma string, epsilon string, product int64) {
	bits := len(diagnostics[0]) // max # bits
	println(fmt.Sprintf("#bits %d", bits))
	gamma = ""   // ones
	epsilon = "" // zeroes
	for i := 0; i < bits; i++ {
		countOnes, countZeroes := countOnesAndZeroes(diagnostics, i)
		moreOnes := countOnes > countZeroes
		gamma += If(moreOnes).String("1", "0")
		epsilon += If(moreOnes).String("0", "1")
		println(fmt.Sprintf("i=%d ones=%d zeroes=%d, gamma=%s, epsison=%s", i, countOnes, countZeroes, gamma, epsilon))
	}
	product = binToDec(gamma, 32) * binToDec(epsilon, 32)
	return
}


func main() {
	diagnostics := util.FileLines("../input/03_INPUT.txt")
	{
		gamma, epsilon, product := computePowerConsumption(diagnostics)
		println(fmt.Sprintf("part 1: gamma %s epsilon %s power consumption %d", gamma, epsilon, product))
	}
}

func countOnesAndZeroes(diagnostics []string, index int) (countOnes int, countZeroes int) {
	for _, reading := range diagnostics {
		if reading[index] == '0' {
			countZeroes += 1
		} else {
			countOnes += 1
		}
	}
	return
}
