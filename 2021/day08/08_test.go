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

func TestRuneSet(t *testing.T) {
	s := NewRuneSet()
	assert.Equal(t, "[]", s.String())
	s.PutAll('a', 'b')
	assert.ElementsMatch(t, []rune{'a', 'b'}, s.Keys())
	assert.Contains(t, s.String(), "a") // sets are unordered, could be "[a b]" or "[b a]" depending on impl
	assert.Contains(t, s.String(), "b") // sets are unordered, could be "[a b]" or "[b a]" depending on impl
	s.Remove('a')
	assert.Equal(t, false, s.Has('a'))
	assert.Equal(t, "[b]", s.String())
	s.Remove('b')
	assert.Equal(t, true, s.IsEmpty())
}

func TestPrettyPrintRuneSlice(t *testing.T) {
	assert.Equal(t, "[a b c]", PrettyPrintRuneSlice([]rune{'a', 'b', 'c'}, " ", true))
}

func TestSortedRuneSlice(t *testing.T) {
	assert.Equal(t, []rune{'a', 'b', 'c', 'd'}, RuneSlice([]rune{'d', 'a', 'c', 'b'}).Sorted())
}
