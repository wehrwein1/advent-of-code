package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, "CMZ", computeDay(fileLines("../input/05_TEST.txt"), Part1))
}

func TestDayPart2(t *testing.T) {
	assert.Equal(t, -1, computeDay(fileLines("../input/05_TEST.txt"), Part2))
}
