package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/wehrwein1/advent-of-code/util"
)

func TestDay(t *testing.T) {
	testcase := util.FileLines("../input/03_TEST.txt")
	gamma, epsilon, product := computePowerConsumption(testcase)
	assert.Equal(t, "10110", gamma)
	assert.Equal(t, "01001", epsilon)
	assert.Equal(t, int64(198), product)
}
