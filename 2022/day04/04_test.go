package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, false, sectionContainsOther([]string{"2-4", "6-8"}))
	assert.Equal(t, false, sectionContainsOther([]string{"2-3", "4-5"}))
	assert.Equal(t, false, sectionContainsOther([]string{"5-7", "7-9"}))
	assert.Equal(t, true, sectionContainsOther([]string{"2-8", "3-7"}))
	assert.Equal(t, true, sectionContainsOther([]string{"6-6", "4-6"}))
	assert.Equal(t, false, sectionContainsOther([]string{"2-6", "4-8"}))
	assert.Equal(t, 2, computeDay(fileLines("../input/04_TEST.txt"), Part1))
}

func TestDayPart2(t *testing.T) {
	assert.Equal(t, false, sectionsOverlapAtAll([]string{"2-4", "6-8"}))
	assert.Equal(t, false, sectionsOverlapAtAll([]string{"2-3", "4-5"}))
	assert.Equal(t, true, sectionsOverlapAtAll([]string{"5-7", "7-9"})) //
	assert.Equal(t, true, sectionsOverlapAtAll([]string{"2-8", "3-7"})) //
	assert.Equal(t, true, sectionsOverlapAtAll([]string{"6-6", "4-6"})) //
	assert.Equal(t, true, sectionsOverlapAtAll([]string{"2-6", "4-8"})) //
	assert.Equal(t, 4, computeDay(fileLines("../input/04_TEST.txt"), Part2))
}
