package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func SkipTestDayPart1CascadeCase(t *testing.T) {
	{
		grid := parseIntGrid(fileLines("../input/11_TESTa.txt"))
		assert.Equal(t, [][]int{
			{1, 1, 1, 1, 1},
			{1, 9, 9, 9, 1},
			{1, 9, 1, 9, 1},
			{1, 9, 9, 9, 1},
			{1, 1, 1, 1, 1},
		}, grid) // grid initial
		assert.Equal(t, 9, countFlashes(grid, 1)) // cascade case, stateful, total steps 1
		assert.Equal(t, [][]int{
			{3, 4, 5, 4, 3},
			{4, 0, 0, 0, 4},
			{5, 0, 0, 0, 5},
			{4, 0, 0, 0, 4},
			{3, 4, 5, 4, 3},
		}, grid) // grid after step 1
		assert.Equal(t, 9, countFlashes(grid, 1)) // another step, 2 total
		assert.Equal(t, [][]int{
			{4, 5, 6, 5, 4},
			{5, 1, 1, 1, 5},
			{6, 1, 1, 1, 6},
			{5, 1, 1, 1, 5},
			{4, 5, 6, 5, 4},
		}, grid) // grid after step 2
	}
}

func SkipTestDayPart1(t *testing.T) {
	assert.Equal(t, 1656, countFlashes(parseIntGrid(fileLines("../input/11_TEST.txt")), 100))
}
