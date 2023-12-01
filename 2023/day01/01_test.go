package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, 142, computeDay(fileLines("../input/01_TEST.txt"), Part1))
}

func TestDayPart2(t *testing.T) {
	assert.Equal(t, 281, computeDay(fileLines("../input/01_TEST2.txt"), Part2))
}
