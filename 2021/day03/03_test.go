package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/wehrwein1/advent-of-code/util"
)

func TestDayPart1(t *testing.T) {
	testcase := util.FileLinesSkipEmpty("../input/03_TEST.txt")
	gamma, epsilon, product := computePowerConsumption(testcase)
	assert.Equal(t, "10110", gamma)
	assert.Equal(t, "01001", epsilon)
	assert.Equal(t, int64(198), product)
}

func TestDayPart2(t *testing.T) {
	testcase := util.FileLinesSkipEmpty("../input/03_TEST.txt")
	oxygen, co2, product := computeRatings(testcase)
	assert.Equal(t, "10111", oxygen)
	assert.Equal(t, "01010", co2)
	assert.Equal(t, int64(230), product)
}
