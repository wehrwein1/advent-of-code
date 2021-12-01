package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	testcase := toInts([]string{"199", "200", "208", "210", "200", "207", "240", "269", "260", "263"})
	assert.Equal(t, 7, countDepthIncreases(testcase))
	assert.Equal(t, 5, countRollingWindowIncreases(testcase))
	assert.Equal(t, []int{607, 618, 618, 617, 647, 716, 769, 792}, computeWindow(testcase))
}
