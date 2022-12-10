package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, "CMZ", computeDay(fileLines("../input/05_TEST.txt"), 3, Part1))
}

func TestDayPart2(t *testing.T) {
	assert.Equal(t, "MCD", computeDay(fileLines("../input/05_TEST.txt"), 3, Part2))
}
