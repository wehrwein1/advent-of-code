package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	assert.Equal(t, 24000, computeDay(fileLines("../input/01_TEST.txt"), Part1))
	assert.Equal(t, 45000, computeDay(fileLines("../input/01_TEST.txt"), Part2))
}
