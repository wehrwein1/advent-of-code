package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	testcase := parsePositions("16,1,2,0,4,2,7,1,2,14")
	minFuelPos, sumFuel := computeMinFuel(testcase, constantFuelUse)
	assert.Equal(t, 2, minFuelPos)
	assert.Equal(t, 37, sumFuel)
}

func TestDayPart2(t *testing.T) {
	testcase := parsePositions("16,1,2,0,4,2,7,1,2,14")
	minFuelPos, sumFuel := computeMinFuel(testcase, linearIncreaseFuelUse)
	assert.Equal(t, 5, minFuelPos)
	assert.Equal(t, 168, sumFuel)
}
