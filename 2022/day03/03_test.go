package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, 16, priority('p'))
	assert.Equal(t, 38, priority('L'))
	assert.Equal(t, 42, priority('P'))
	assert.Equal(t, 22, priority('v'))
	assert.Equal(t, 20, priority('t'))
	assert.Equal(t, 19, priority('s'))
	assert.Equal(t, 157, computeDay(fileLines("../input/03_TEST.txt"), Part1))
}

func TestDayPart2(t *testing.T) {
	assert.Equal(t, 18, priority('r'))
	assert.Equal(t, 52, priority('Z'))
	assert.Equal(t, 'b', getCommonItem("abc", "xy_b_z"))
	assert.Equal(t, 'b', getCommonItem("abc", "xy_b_z", "fgz_b_gH"))
	assert.Equal(t, 70, computeDay(fileLines("../input/03_TEST.txt"), Part2))
}
