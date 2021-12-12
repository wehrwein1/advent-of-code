package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	testcase := fileLines("../input/09_TEST.txt")
	notUsed := -1
	assert.Equal(t, []LowPoint{
		{Row: 0, Col: 1, Value: 1},
		{Row: 0, Col: 9, Value: 0},
		{Row: 2, Col: 2, Value: 5},
		{Row: 4, Col: 6, Value: 5},
	}, findLowPoints(parseIntGrid(testcase)))
	assert.Equal(t, []int{2, 1, 6, 6}, toRiskLevels([]LowPoint{
		{Row: notUsed, Col: notUsed, Value: 1},
		{Row: notUsed, Col: notUsed, Value: 0},
		{Row: notUsed, Col: notUsed, Value: 5},
		{Row: notUsed, Col: notUsed, Value: 5},
	}))
	assert.Equal(t, 15, sumRiskLevels(testcase))

}

func TestDayPart2(t *testing.T) {
	data := parseIntGrid(fileLines("../input/09_TEST.txt"))
	notUsed := -1
	assert.Equal(t, []int{3}, computeBasinSizes(data, []LowPoint{{Row: 0, Col: 1, Value: notUsed}}))
	assert.Equal(t, []int{9}, computeBasinSizes(data, []LowPoint{{Row: 0, Col: 9, Value: notUsed}}))
	assert.Equal(t, []int{14}, computeBasinSizes(data, []LowPoint{{Row: 2, Col: 2, Value: notUsed}}))
	assert.Equal(t, []int{9}, computeBasinSizes(data, []LowPoint{{Row: 4, Col: 6, Value: notUsed}}))
	assert.Equal(t, []int{3, 9, 14, 9}, computeBasinSizes(data, findLowPoints(data)))
	assert.Equal(t, []int{9, 9, 14}, threeLargest([]int{3, 9, 14, 9}))
	assert.Equal(t, 1134, product(threeLargest(computeBasinSizes(data, findLowPoints(data)))...))
}
