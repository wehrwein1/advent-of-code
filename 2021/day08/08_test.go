package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, 26, countSelectedDigits(fileLines("../input/08_TEST.txt"), part1CountedDigits...))
}

func SkipTestDayPart2(t *testing.T) {
	testcase := "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
	_, outputValue := decodeSignal(testcase)
	assert.Equal(t, 5353, outputValue)
	assert.Equal(t, 61229, sumOutputValues(fileLines("../input/08_TEST.txt")))
}
