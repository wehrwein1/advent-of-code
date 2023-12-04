package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, 13, computeDay(fileLines("../input/04_TEST.txt"), Part1))
}

func IgnoreTestDayPart2(t *testing.T) {
	assert.Equal(t, -1, computeDay(fileLines("../input/04_TEST.txt"), Part2))
}
