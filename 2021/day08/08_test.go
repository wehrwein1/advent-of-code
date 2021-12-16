package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/wehrwein1/advent-of-code/util/ds"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, 26, countSelectedDigits(fileLines("../input/08_TEST.txt"), part1CountedDigits...))
}

func SkipTestDayPart2(t *testing.T) {
	testcase := "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
	signalOutputPatterns, _ := decodeSignal(testcase)
	assert.InDeltaMapValues(t, map[string]int{
		"d": 0,
		"e": 1,
		"a": 2,
		"f": 3,
		"g": 4,
		"b": 5,
		"c": 6,
	}, signalOutputPatterns, 0)
	// assert.Equal(t, 5353, outputValue)
	// assert.Equal(t, 61229, sumOutputValues(fileLines("../input/08_TEST.txt")))
}

func TestRuneSetUnion(t *testing.T) {
	assert.ElementsMatch(t, []rune{}, runeSetUnion(*ds.NewRuneSet(), *ds.NewRuneSet('a', 'b', 'c')).Keys())
	assert.ElementsMatch(t, []rune{'b', 'd'}, runeSetUnion(*ds.NewRuneSet('b', 'd'), *ds.NewRuneSet('a', 'b', 'c', 'd')).Keys())
}
