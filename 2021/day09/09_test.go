package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	testcase := fileLines("../input/09_TEST.txt")
	assert.Equal(t, []int{1, 0, 5, 5}, findLowPoints(parseLines(testcase)))
	assert.Equal(t, []int{2, 1, 6, 6}, toRiskLevels([]int{1, 0, 5, 5}))
	assert.Equal(t, 15, sumRiskLevels(testcase))
}
