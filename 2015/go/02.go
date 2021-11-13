// https://adventofcode.com/2015/day/2
package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// tests
	assertEquals(minInt(31, 66, 2, 7), 2, "minInt() results different")
	assertEquals(sumInts(3, 66, 2, 7), 78, "sumInts() results different")
	area, ribbon := computeSumAreaAndRibbon([]string{"2x3x4"}) // TODO FIXME one liner?
	assertEquals(area, 58)
	assertEquals(ribbon, 34)
	area, ribbon = computeSumAreaAndRibbon([]string{"1x1x10"}) // TODO FIXME one liner?
	assertEquals(area, 43)
	assertEquals(ribbon, 14)

	// solution
	area, ribbon = computeSumAreaAndRibbon(fileLines("../input/02_INPUT.txt"))
	println(fmt.Sprintf("part 1: square feet of wrapping paper: %d", area))
	println(fmt.Sprintf("part 2: feet of ribbon: %d", ribbon))
}

func computeSumAreaAndRibbon(lines []string) (sumArea int, sumRibbon int) {
	for _, line := range lines {
		// parse line
		var dimensions []int
		for _, dim := range strings.Split(line, "x") {
			val, err := strconv.Atoi(dim)
			check(err)
			dimensions = append(dimensions, val)
		}
		// compute
		l, w, h := dimensions[0], dimensions[1], dimensions[2]
		areaOfSmallestSide := minInt(l*w, l*h, w*h)
		// sum
		sumArea += 2*l*w + 2*w*h + 2*h*l + areaOfSmallestSide
		sort.Ints(dimensions) // stateful change
		sumRibbon += sumInts(dimensions[:2]...)*2 + l*w*h
	}
	return // neat: return implicit values from declared signature
}

func minInt(items ...int) (minItem int) {
	minItem = items[0] // panic if empty slice
	for _, item := range items {
		if item < minItem {
			minItem = item
		}
	}
	return
}

func sumInts(items ...int) (sum int) {
	for _, item := range items {
		sum += item
	}
	return sum
}

func fileLines(filename string) (ret []string) { // whoa! crazy implicit return value syntax https://stackoverflow.com/a/37563128/3633993
	bytes, err := os.ReadFile(filename)
	check(err)
	lines := strings.Split(string(bytes), "\n")
	for _, line := range lines {
		if len(line) > 0 { // ignore empty lines
			ret = append(ret, line)
		}
	}
	return
}

func assertEquals(actual interface{}, expected interface{}, optionalFailMessage ...string) {
	if expected != actual {
		failMessage := ""
		if len(optionalFailMessage) > 0 {
			failMessage = fmt.Sprintf(" : %s", optionalFailMessage[0])
		}
		panic(fmt.Sprintf("assertion fail, expected %v, was %v%s", actual, expected, failMessage))
	}
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}
