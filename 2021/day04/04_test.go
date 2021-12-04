package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, false, isBingo([][]bool{{false, false, false}, {false, false, false}, {false, false, false}}))
	assert.Equal(t, true, isBingo([][]bool{{false, false, false}, {true, true, true}, {false, false, false}}))
	assert.Equal(t, true, isBingo([][]bool{{false, true, false}, {false, true, false}, {false, true, false}}))
	assert.Equal(t, 4512, computeWinningScorePart1(loadBingoData("../input/04_TEST.txt")))
	assert.Equal(t, 1924, computeWinningScorePart2(loadBingoData("../input/04_TEST.txt")))
}
