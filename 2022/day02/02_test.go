package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, 4, computeRound("A", "X", Part1)) // draw (rock) (1+3)
	assert.Equal(t, 8, computeRound("A", "Y", Part1)) // example case: your paper beats rock (2+6)
	assert.Equal(t, 3, computeRound("A", "Z", Part1)) // your scissors loses to rock (3+0)
	assert.Equal(t, 1, computeRound("B", "X", Part1)) // example case: your rock loses to paper (1+0)
	assert.Equal(t, 5, computeRound("B", "Y", Part1)) // draw (paper) (2+3)
	assert.Equal(t, 9, computeRound("B", "Z", Part1)) // your scissor beats paper (3+6)
	assert.Equal(t, 7, computeRound("C", "X", Part1)) // your rock beats scissors (1+6)
	assert.Equal(t, 2, computeRound("C", "Y", Part1)) // your paper loses to scissors (2+0)
	assert.Equal(t, 6, computeRound("C", "Z", Part1)) // example case, draw (scissors) (3+3)
	assert.Equal(t, 15, computeDay(fileLines("../input/02_TEST.txt"), Part1))
}

func TestDayPart2(t *testing.T) {
	// X = lose
	// Y = draw
	// Z = win
	assert.Equal(t, 3, computeRound("A", "X", Part2)) // opponent rock, need lose (scissors), (3+0)
	assert.Equal(t, 4, computeRound("A", "Y", Part2)) // example case: opponent Rock, need draw (rock), (1+3)
	assert.Equal(t, 8, computeRound("A", "Z", Part2)) // opponent rock, need win (paper) (2+6)
	assert.Equal(t, 1, computeRound("B", "X", Part2)) // example case: opponent paper, need lose (rock) (1+0)
	assert.Equal(t, 5, computeRound("B", "Y", Part2)) // opponent paper, need draw (paper) (2+3)
	assert.Equal(t, 9, computeRound("B", "Z", Part2)) // opponent paper, need win (scissors) (3+6)
	assert.Equal(t, 2, computeRound("C", "X", Part2)) // opponent scissors, need lose (paper) (2+0)
	assert.Equal(t, 6, computeRound("C", "Y", Part2)) // opponent scissors, need draw (scissors) (3+3)
	assert.Equal(t, 7, computeRound("C", "Z", Part2)) // example case: opponent scissors, need win (rock) (1+6)
	assert.Equal(t, 12, computeDay(fileLines("../input/02_TEST.txt"), Part2))
}
