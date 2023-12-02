package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, 8, computeDay(fileLines("../input/02_TEST.txt"), Part1))
}

func TestDayPart2(t *testing.T) {
	assert.Equal(t, 2286, computeDay(fileLines("../input/02_TEST.txt"), Part2))
}
