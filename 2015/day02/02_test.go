package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	area, ribbon := computeSumAreaAndRibbon([]string{"2x3x4"})
	assert.Equal(t, []int{58, 34}, []int{area, ribbon})
	area, ribbon = computeSumAreaAndRibbon([]string{"1x1x10"})
	assert.Equal(t, []int{43, 14}, []int{area, ribbon})
}
