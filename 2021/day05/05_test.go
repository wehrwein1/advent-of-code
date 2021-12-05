package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/wehrwein1/advent-of-code/util"
)

var NewVector = util.NewVector

func TestDay(t *testing.T) {
	testcase := parseLines("../input/05_TEST.txt")
	assert.Equal(t, 5, countOverlaysPart1(testcase))
	assert.Equal(t, 12, countOverlaysPart2(testcase))
}
