package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	testcase := []string{"forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"}
	assert.Equal(t, 150, product(computePositionPart1(testcase)))
	assert.Equal(t, 900, product(computePositionPart2(testcase)))
}
