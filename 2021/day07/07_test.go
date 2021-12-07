package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	testcase := parsePositions("16,1,2,0,4,2,7,1,2,14")
	minFuelPos, sumFuel := computeMinFuel(testcase)
	assert.Equal(t, 2, minFuelPos)
	assert.Equal(t, 37, sumFuel)
}
